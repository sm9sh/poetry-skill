#!/usr/bin/env python3
"""
Tests for evals/run_evals.py with a fake `claude`: parsing, blind mapping,
the full generate → check → judge → report round, and reading iteration-1.
No network and no CLI needed.
"""

import contextlib
import importlib.util
import io
import json
import pathlib
import tempfile
import unittest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("run_evals", PROJECT_ROOT / "evals" / "run_evals.py")
run_evals = importlib.util.module_from_spec(spec)
spec.loader.exec_module(run_evals)

SONG = "[Verse 1]\nрядок\n\n[Chorus]\nдощ у бляшанці\n"


def stream(text, skill=None):
    events = []
    if skill:
        events.append({"type": "assistant", "message": {"content": [
            {"type": "tool_use", "name": "Skill", "input": {"skill": f"poetry-skill:{skill}"}}]}})
    events.append({"type": "result", "result": text, "total_cost_usd": 0.01, "num_turns": 2})
    return "\n".join(json.dumps(e, ensure_ascii=False) for e in events)


def fake_claude(prompt, cwd, extra_args, timeout):
    if "--output-format" in extra_args and extra_args[extra_args.index("--output-format") + 1] == "json":
        # judge: always prefers the answer that mentions the skill
        a = prompt.split("<answer_a>")[1].split("</answer_a>")[0]
        verdict = {"score_a": 8 if "SKILL" in a else 6, "score_b": 6 if "SKILL" in a else 8,
                   "winner": "A" if "SKILL" in a else "B", "reasons": ["r"], "flaw_a": "", "flaw_b": ""}
        return json.dumps({"result": "Verdict:\n" + json.dumps(verdict), "total_cost_usd": 0.02})
    with_plugin = "--plugin-dir" in extra_args
    body = f"```\n{SONG}```" if "пісн" in prompt else "вірш"
    return stream(("SKILL " if with_plugin else "") + body, None)


class TestRunEvals(unittest.TestCase):

    def test_parse_stream(self):
        run = run_evals.parse_stream("noise\n" + stream("Відповідь", "ukrainian-poetry"))
        self.assertEqual(run["text"], "Відповідь")
        self.assertEqual(run["skills"], ["ukrainian-poetry"])
        self.assertEqual(run["turns"], 2)

    def test_run_prompt_invokes_only_positive_evals(self):
        ev = {"skill": "ukrainian-poetry", "prompt": "напиши вірш"}
        self.assertEqual(run_evals.run_prompt(ev, PROJECT_ROOT, "invoke"), "/poetry-skill:ukrainian-poetry напиши вірш")
        self.assertEqual(run_evals.run_prompt(ev, PROJECT_ROOT, "natural"), "напиши вірш")
        self.assertEqual(run_evals.run_prompt(ev, None, "invoke"), "напиши вірш")
        self.assertEqual(run_evals.run_prompt({"skill": "none", "prompt": "x"}, PROJECT_ROOT, "invoke"), "x")

    def test_parse_judgement_and_mapping(self):
        v = run_evals.parse_judgement('Here: {"score_a": "7.5", "score_b": 8, "winner": "?"}')
        self.assertEqual((v["score_a"], v["winner"]), (7.5, "B"))
        v = run_evals.parse_judgement('{"score_a": 6, "score_b": 7, "winner": "B", "reasons": ["line one\nline two"]}')
        self.assertEqual(v["winner"], "B")
        self.assertEqual(run_evals.blind_mapping([1, 2, 3], 2), run_evals.blind_mapping([1, 2, 3], 2))
        for order in run_evals.blind_mapping(range(10), 7).values():
            self.assertEqual(sorted(order.values()), ["baseline", "with_skill"])

    def test_syllable_facts_for_the_judge(self):
        poem = "**Назва**\n\nПіп кропив — а кіт тим часом ковбасу хапає,\n\n---\n- примітка про форму"
        self.assertEqual(run_evals.syllables_per_line(poem), [14])
        song = f"```\n{SONG}```"
        self.assertEqual(run_evals.syllables_per_line(song), [2, 5])
        facts = run_evals.facts_text({"with_skill": {"syllables": [14]}, "baseline": {"errors": []}},
                                     {"A": "baseline", "B": "with_skill"})
        self.assertIn("B: syllables per verse line: 14", facts)
        self.assertIn("A: check_lyrics.py errors: 0", facts)
        self.assertEqual(run_evals.facts_text({}, {"A": "baseline", "B": "with_skill"}), "")

    def test_lyrics_blocks(self):
        self.assertEqual(run_evals.lyrics_blocks(f"Style\n```\ndarkwave\n```\n```text\n{SONG}```"), [SONG])
        self.assertEqual(run_evals.lyrics_blocks("просто вірш"), [])

    def test_reads_iteration_1(self):
        scores = run_evals.previous_scores(1)
        self.assertEqual(len(scores), 8)
        self.assertEqual(scores["5"], {"with_skill": 8.5, "baseline": 5.5})

    def test_full_round_with_fake_claude(self):
        evals = [
            {"id": 1, "skill": "ukrainian-poetry", "name": "poem", "prompt": "напиши вірш", "expected_output": "e"},
            {"id": 2, "skill": "ukrainian-poetry-to-suno", "name": "song", "prompt": "зроби пісню", "expected_output": "e"},
            {"id": 3, "skill": "none", "name": "negative", "prompt": "write a poem", "expected_output": "e"},
        ]
        saved = (run_evals.RESULTS, run_evals.claude, run_evals.load_evals)
        with tempfile.TemporaryDirectory() as tmp:
            try:
                run_evals.RESULTS = pathlib.Path(tmp)
                run_evals.claude = fake_claude
                run_evals.load_evals = lambda ids=None: evals
                with contextlib.redirect_stdout(io.StringIO()):
                    run_evals.main(["all", "--iteration", "7", "--jobs", "1", "--both-orders"])
                out = pathlib.Path(tmp) / "iteration-7"
                verdict = json.loads((out / "verdict.json").read_text(encoding="utf-8"))
                checks = json.loads((out / "checks.json").read_text(encoding="utf-8"))
                summary = (out / "summary.md").read_text(encoding="utf-8")
            finally:
                run_evals.RESULTS, run_evals.claude, run_evals.load_evals = saved

        self.assertEqual(set(verdict), {"1", "2"})                      # negative control is not judged
        for v in verdict.values():
            self.assertEqual(v["winner"], "with_skill")                # unblinded correctly in both orders
            self.assertEqual(len(v["verdicts"]), 2)
        self.assertEqual(checks["2"]["with_skill"]["lyrics_blocks"], 1)
        self.assertNotIn("lyrics_blocks", checks["1"]["with_skill"])  # poems are not lyrics-checked
        self.assertIn("Skill wins 2", summary)
        self.assertIn("invoked", summary)
        self.assertIn("negative", summary)


if __name__ == "__main__":
    unittest.main()
