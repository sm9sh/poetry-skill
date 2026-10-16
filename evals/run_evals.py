#!/usr/bin/env python3
"""
Run an eval round: generate answers with and without the skills, check them,
judge them blind, write a summary.

    python evals/run_evals.py all --iteration 2
    python evals/run_evals.py all --iteration 2 --ids 5,6 --jobs 2
    python evals/run_evals.py all --iteration 3 --baseline git:v4.1.0   # old skill version as baseline

Stages (each can be run on its own; finished outputs are reused unless --force):
    generate  every eval prompt through `claude -p`, once with the plugin from this
              repo (with_skill/) and once as the baseline (baseline/): no skills, or
              the plugin from a git ref. Each run starts in an empty temp directory.
    check     mechanical checks: check_lyrics.py on every lyrics block of the song
              evals, which skills were triggered (negative controls must trigger none).
    judge     blind A/B judging of each pair by a separate `claude -p` call; the
              A/B order is shuffled with a fixed seed and saved to blind-mapping.json.
    report    summary.md: scores, winners, checks, cost, change vs the previous iteration.

Results go to evals/results/iteration-N/ in the same layout as iteration-1.
Needs the Claude Code CLI (`claude`) logged in. Generation runs may use Read, Glob,
Grep, Skill, Write/Edit inside their temp directory and `python` (to run the skill
scripts). Audio still has to be checked by ear: see evals/README.md.
"""

import argparse
import concurrent.futures
import hashlib
import importlib.util
import json
import pathlib
import random
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile

EVALS_DIR = pathlib.Path(__file__).resolve().parent
REPO = EVALS_DIR.parent
RESULTS = EVALS_DIR / "results"
CHECK_LYRICS = REPO / "skills" / "ukrainian-poetry-to-suno" / "scripts" / "check_lyrics.py"
SONG_SKILL = "ukrainian-poetry-to-suno"
CONDITIONS = ("with_skill", "baseline")
LYRICS_START = re.compile(r"^\[(Intro|Verse|Chorus|Bridge|Outro|Pre-Chorus|Hook)", re.M)
PLUGIN_PARTS = (".claude-plugin", "skills", "commands", "AUTHOR_PROFILE.md")
GEN_TOOLS = ["Read", "Glob", "Grep", "Skill", "Bash(python:*)", "Bash(python3:*)", "Bash(cd:*)", "Bash(ls:*)", "Bash(mkdir:*)"]

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


# --------------------------------------------------------------------------- helpers

def load_evals(ids=None):
    data = json.loads((EVALS_DIR / "evals.json").read_text(encoding="utf-8"))
    evals = data["evals"]
    if ids:
        evals = [e for e in evals if e["id"] in ids]
    return evals


def iteration_dir(n):
    return RESULTS / f"iteration-{n}"


def read_json(path, default):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def normalize_skill(name):
    return name.split(":")[-1].strip().lstrip("/")


def parse_stream(stdout):
    """Final answer, triggered skills, cost and turns from `--output-format stream-json`."""
    run = {"text": "", "skills": [], "tools": [], "cost_usd": 0.0, "duration_ms": 0, "turns": 0, "is_error": False}
    for line in stdout.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("type") == "assistant":
            for block in (event.get("message") or {}).get("content") or []:
                if block.get("type") != "tool_use":
                    continue
                args = block.get("input") or {}
                detail = args.get("file_path") or args.get("command") or args.get("pattern") or args.get("skill") or ""
                run["tools"].append(f"{block.get('name')} {str(detail)[:120]}".strip())
                skill = None
                if block.get("name") == "Skill":
                    skill = args.get("skill") or args.get("command")
                elif block.get("name") == "Read" and str(args.get("file_path", "")).endswith("SKILL.md"):
                    skill = pathlib.PurePath(args["file_path"]).parent.name
                if skill and normalize_skill(skill) not in run["skills"]:
                    run["skills"].append(normalize_skill(skill))
        elif event.get("type") == "result":
            run["text"] = event.get("result") or ""
            run["cost_usd"] = event.get("total_cost_usd") or 0.0
            run["duration_ms"] = event.get("duration_ms") or 0
            run["turns"] = event.get("num_turns") or 0
            run["is_error"] = bool(event.get("is_error"))
    return run


def claude(prompt, cwd, extra_args, timeout):
    """Runs `claude -p` and returns its stdout. Replaced by a fake in tests."""
    cmd = ["claude", "-p", prompt, "--setting-sources", "project", "--no-session-persistence"] + extra_args
    proc = subprocess.run(cmd, cwd=cwd, stdin=subprocess.DEVNULL, capture_output=True, text=True, encoding="utf-8", timeout=timeout)
    if proc.returncode != 0 and not proc.stdout.strip():
        raise RuntimeError(proc.stderr.strip()[-500:] or f"claude exited with {proc.returncode}")
    return proc.stdout


def export_plugin(baseline, workdir):
    """Plugin directory for a condition: this repo, a git ref, or None (no skills)."""
    if baseline == "none":
        return None
    if baseline == "current":
        # A copy, so a run can never edit the repository it is testing.
        target = pathlib.Path(workdir) / "plugin-current"
        if not target.exists():
            ignore = shutil.ignore_patterns("__pycache__", "*.pyc")
            for part in PLUGIN_PARTS:
                src = REPO / part
                if src.is_dir():
                    shutil.copytree(src, target / part, ignore=ignore)
                elif src.exists():
                    target.mkdir(parents=True, exist_ok=True)
                    shutil.copy(src, target / part)
        return target
    if baseline.startswith("git:"):
        ref = baseline[4:]
        safe_ref = re.sub(r"[^\w.-]", "_", ref)
        target = pathlib.Path(workdir) / f"plugin-{safe_ref}"
        if not target.exists():
            archive = pathlib.Path(workdir) / "plugin.tar"
            subprocess.run(["git", "-C", str(REPO), "archive", "--format=tar", "-o", str(archive), ref], check=True)
            with tarfile.open(archive) as tar:
                tar.extractall(target, **({"filter": "data"} if hasattr(tarfile, "data_filter") else {}))
            archive.unlink()
            # Before v4.2.1 the plugin shipped commands named like the skills; they shadowed the
            # skills with a stub. Drop them so the old version is measured by its SKILL.md.
            for skill in target.glob("skills/*/SKILL.md"):
                (target / "commands" / f"{skill.parent.name}.md").unlink(missing_ok=True)
        return target
    raise SystemExit(f"--baseline must be none, current or git:<ref>, got {baseline!r}")


# --------------------------------------------------------------------------- generate

def plugin_name(plugin_dir):
    manifest = pathlib.Path(plugin_dir) / ".claude-plugin" / "plugin.json"
    return json.loads(manifest.read_text(encoding="utf-8"))["name"] if manifest.exists() else None


def run_prompt(ev, plugin_dir, trigger):
    """The eval prompt; with --trigger invoke the expected skill is called explicitly as a slash command."""
    if trigger == "invoke" and plugin_dir is not None and ev["skill"] != "none":
        name = plugin_name(plugin_dir)
        return f"/{name + ':' if name else ''}{ev['skill']} {ev['prompt']}"
    return ev["prompt"]


def generate_one(ev, condition, plugin_dir, args):
    with tempfile.TemporaryDirectory(prefix=f"eval-{ev['id']}-") as cwd:
        for rel in ev.get("files") or []:
            src = EVALS_DIR / rel
            shutil.copy(src, pathlib.Path(cwd) / src.name)
        extra = ["--output-format", "stream-json", "--verbose", "--permission-mode", "acceptEdits",
                 "--allowedTools", *GEN_TOOLS]
        if plugin_dir is not None:
            extra += ["--plugin-dir", str(plugin_dir), "--add-dir", str(plugin_dir)]  # let it run the skill scripts
        if args.model:
            extra += ["--model", args.model]
        if args.max_budget_usd:
            extra += ["--max-budget-usd", str(args.max_budget_usd)]
        prompt = run_prompt(ev, plugin_dir, args.trigger)
        run = parse_stream(claude(prompt, cwd, extra, args.timeout))
    if prompt != ev["prompt"] and ev["skill"] not in run["skills"]:
        run["skills"].insert(0, ev["skill"])  # a slash command loads the skill inline, without a Skill call
    run["invoked"] = prompt != ev["prompt"]
    return run


def cmd_generate(args):
    out = iteration_dir(args.iteration)
    runs_path = out / "runs.json"
    runs = read_json(runs_path, {})
    with tempfile.TemporaryDirectory(prefix="eval-plugins-") as plugins_tmp:
        plugin_for = {"with_skill": export_plugin("current", plugins_tmp),
                      "baseline": export_plugin(args.baseline, plugins_tmp)}
        jobs = []
        for ev in load_evals(args.ids):
            for condition in CONDITIONS:
                path = out / condition / f"eval-{ev['id']}.md"
                if path.exists() and not args.force:
                    continue
                jobs.append((ev, condition, path))
        print(f"generate: {len(jobs)} runs (baseline = {args.baseline})")
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
            futures = {pool.submit(generate_one, ev, cond, plugin_for[cond], args): (ev, cond, path)
                       for ev, cond, path in jobs}
            for fut in concurrent.futures.as_completed(futures):
                ev, cond, path = futures[fut]
                try:
                    run = fut.result()
                except Exception as e:  # keep going; the failed run can be retried
                    print(f"  eval {ev['id']} {cond}: FAILED — {e}")
                    continue
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(run["text"].strip() + "\n", encoding="utf-8")
                meta = {k: v for k, v in run.items() if k != "text"}
                runs.setdefault(str(ev["id"]), {})[cond] = meta
                write_json(runs_path, runs)
                skills = ", ".join(meta["skills"]) or "no skill"
                print(f"  eval {ev['id']} {cond}: {meta['turns']} turns, ${meta['cost_usd']:.2f}, {skills}")
    meta = read_json(out / "meta.json", {})
    meta.update({"baseline": args.baseline, "model": args.model or "default", "trigger": args.trigger})
    write_json(out / "meta.json", meta)


# --------------------------------------------------------------------------- check

def load_check_lyrics():
    spec = importlib.util.spec_from_file_location("check_lyrics", CHECK_LYRICS)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def lyrics_blocks(text):
    blocks = [b for b in re.findall(r"```[\w-]*\n(.*?)```", text, re.S) if LYRICS_START.search(b)]
    if not blocks and LYRICS_START.search(text):
        blocks = [text]
    return blocks


def check_answer(ev, text, check_lyrics, stress_dict):
    platform = "lyria" if re.search(r"lyria|flow", ev["prompt"], re.I) else "suno"
    blocks = lyrics_blocks(text)
    errors, warnings = [], []
    for block in blocks:
        e, w = check_lyrics.check(block, platform=platform, section="[Chorus" not in block,
                                  stress_dict=stress_dict)
        errors += e
        warnings += w
    return {"lyrics_blocks": len(blocks), "errors": errors, "warnings": warnings}


VOWELS = set("аеєиіїоуюяАЕЄИІЇОУЮЯ")
NOT_VERSE = re.compile(r"^\s*(#|[-*>|]|\d+\.|```|\*\*[^*]+\*\*\s*$)")


def verse_lines(text):
    """Sung lines of the lyrics blocks, or the verse lines of a poem (no headings, lists or notes)."""
    blocks = lyrics_blocks(text)
    lines = "\n".join(blocks).splitlines() if blocks else text.split("\n---")[0].splitlines()
    out = []
    for line in lines:
        line = re.sub(r"\[[^\]]*\]", "", line).strip()
        if line and not NOT_VERSE.match(line) and any(c in VOWELS for c in line) and len(line) < 120:
            out.append(line)
    return out


def syllables_per_line(text):
    """Ukrainian syllables = vowels; judges miscount them, so they get the numbers."""
    return [sum(c in VOWELS for c in line) for line in verse_lines(text)]


def cmd_check(args):
    out = iteration_dir(args.iteration)
    runs = read_json(out / "runs.json", {})
    check_lyrics = load_check_lyrics()
    stress_dict = check_lyrics.StressDict.load()
    checks = {}
    for ev in load_evals(args.ids):
        entry = {}
        for condition in CONDITIONS:
            path = out / condition / f"eval-{ev['id']}.md"
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            result = {"skills": runs.get(str(ev["id"]), {}).get(condition, {}).get("skills"),
                      "syllables": syllables_per_line(text)}
            if ev["skill"] == SONG_SKILL:
                result.update(check_answer(ev, text, check_lyrics, stress_dict))
            entry[condition] = result
        if entry:
            checks[str(ev["id"])] = entry
    write_json(out / "checks.json", checks)
    print(f"check: {len(checks)} evals checked" + ("" if stress_dict else " (no stress dictionary)"))


# --------------------------------------------------------------------------- judge

JUDGE_PROMPT = """You are judging two answers to the same request, blind. You are an exacting editor of contemporary Ukrainian poetry and an experienced songwriter who writes for Suno v6 and Lyria 3.5.

Request from the user:
<request>
{prompt}
</request>

What a good answer looks like:
<expected>
{expected}
</expected>

<answer_a>
{a}
</answer_a>

<answer_b>
{b}
</answer_b>
{facts}
Judge as a demanding reader would:
- Meaning first: every line makes literal or clearly decodable sense; no invented or archaic words, Russianisms, or stress broken for a rhyme; rhymes never bought with forced syntax.
- Poetry: concrete images instead of declared feelings, no clichés or moralizing, living rhythm, an ending that stays.
- Songs: would you paste this sheet into the platform as is? Square brackets for sections and delivery cues, round brackets only for words to be sung; stress marks only where the model would otherwise get it wrong; a hook that returns; verse 2 moves the story on; Style and Exclude that would actually steer the sound.
- The brief: does it do what was asked (form, constraints, "keep my words", language)?
Length, formatting and explanations earn nothing by themselves. Quote the lines that decide it.

Reply with JSON only, no other text:
{{"score_a": <0-10, halves allowed>, "score_b": <0-10>, "winner": "A" | "B" | "tie", "reasons": ["<3-5 short reasons with quotes>"], "flaw_a": "<most serious flaw of A>", "flaw_b": "<most serious flaw of B>"}}"""


def judge_id(args):
    """Judge model + prompt version: scores from different judges are not comparable."""
    version = hashlib.sha1(JUDGE_PROMPT.encode("utf-8")).hexdigest()[:8]
    return f"{args.judge_model or 'default'}/{version}" + ("/both-orders" if args.both_orders else "")


def parse_judgement(text):
    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        raise ValueError(f"no JSON in judge reply: {text[:200]!r}")
    data = json.loads(match.group(0), strict=False)  # judges sometimes put raw newlines in strings
    data["score_a"] = float(data["score_a"])
    data["score_b"] = float(data["score_b"])
    if data.get("winner") not in ("A", "B", "tie"):
        data["winner"] = "tie" if data["score_a"] == data["score_b"] else ("A" if data["score_a"] > data["score_b"] else "B")
    return data


def blind_mapping(eval_ids, seed):
    rng = random.Random(seed)
    mapping = {}
    for eid in eval_ids:
        order = list(CONDITIONS)
        rng.shuffle(order)
        mapping[str(eid)] = {"A": order[0], "B": order[1]}
    return mapping


def facts_text(checks, order):
    """Programmatic facts for the judge: syllables per line and check_lyrics errors."""
    if not checks:
        return ""
    lines = ["", "Computed facts (counted by a script; trust them over your own counting):"]
    for label in ("A", "B"):
        c = checks.get(order[label], {})
        if c.get("syllables"):
            lines.append(f"- {label}: syllables per verse line: {', '.join(map(str, c['syllables']))}")
        if "errors" in c:
            lines.append(f"- {label}: check_lyrics.py errors: {len(c['errors'])}" +
                         (f" ({'; '.join(c['errors'][:3])})" if c["errors"] else ""))
    return "\n".join(lines) + "\n" if len(lines) > 2 else ""


def judge_once(ev, answers, order, args, checks=None):
    prompt = JUDGE_PROMPT.format(prompt=ev["prompt"], expected=ev["expected_output"],
                                 a=answers[order["A"]], b=answers[order["B"]], facts=facts_text(checks, order))
    extra = ["--output-format", "json"]
    if args.judge_model:
        extra += ["--model", args.judge_model]
    with tempfile.TemporaryDirectory(prefix="eval-judge-") as cwd:
        stdout = claude(prompt, cwd, extra, args.timeout)
    reply = json.loads(stdout)
    verdict = parse_judgement(reply.get("result") or "")
    verdict["cost_usd"] = reply.get("total_cost_usd") or 0.0
    return verdict


def judge_eval(ev, answers, order, args, checks=None):
    """Scores per condition; with --both-orders the pair is judged twice, swapped, and averaged."""
    orders = [order]
    if args.both_orders:
        orders.append({"A": order["B"], "B": order["A"]})
    scores = {c: [] for c in CONDITIONS}
    verdicts = []
    for o in orders:
        v = judge_once(ev, answers, o, args, checks)
        scores[o["A"]].append(v["score_a"])
        scores[o["B"]].append(v["score_b"])
        verdicts.append(v)
    avg = {c: sum(s) / len(s) for c, s in scores.items()}
    winner = "tie" if avg["with_skill"] == avg["baseline"] else max(avg, key=avg.get)
    return {"order": order, "scores": avg, "winner": winner, "verdicts": verdicts,
            "cost_usd": sum(v["cost_usd"] for v in verdicts)}


def cmd_judge(args):
    out = iteration_dir(args.iteration)
    evals = [e for e in load_evals(args.ids) if e["skill"] != "none"]
    mapping_path = out / "blind-mapping.json"
    mapping = read_json(mapping_path, {})
    for eid, order in blind_mapping([e["id"] for e in evals], args.seed or args.iteration).items():
        mapping.setdefault(eid, order)
    write_json(mapping_path, mapping)

    checks = read_json(out / "checks.json", {})
    verdict_path = out / "verdict.json"
    verdicts = read_json(verdict_path, {})
    todo = []
    for ev in evals:
        answers = {c: (out / c / f"eval-{ev['id']}.md") for c in CONDITIONS}
        if not all(p.exists() for p in answers.values()):
            print(f"  eval {ev['id']}: missing answers, run generate first")
            continue
        if str(ev["id"]) in verdicts and not args.force:
            continue
        todo.append((ev, {c: p.read_text(encoding="utf-8") for c, p in answers.items()}))
    print(f"judge: {len(todo)} pairs" + (" (both orders)" if args.both_orders else ""))
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures = {pool.submit(judge_eval, ev, answers, mapping[str(ev["id"])], args, checks.get(str(ev["id"]))): ev
                   for ev, answers in todo}
        for fut in concurrent.futures.as_completed(futures):
            ev = futures[fut]
            try:
                verdicts[str(ev["id"])] = fut.result()
            except Exception as e:
                print(f"  eval {ev['id']}: FAILED — {e}")
                continue
            write_json(verdict_path, verdicts)
            s = verdicts[str(ev["id"])]["scores"]
            print(f"  eval {ev['id']}: with_skill {s['with_skill']:g} · baseline {s['baseline']:g}")
    write_blind_verdict_md(out, evals, verdicts)
    meta = read_json(out / "meta.json", {})
    meta["judge"] = judge_id(args)
    write_json(out / "meta.json", meta)


def write_blind_verdict_md(out, evals, verdicts):
    lines = [f"# Blind Verdict — {len(verdicts)} evals (A vs B)", ""]
    for ev in evals:
        v = verdicts.get(str(ev["id"]))
        if not v:
            continue
        first = v["verdicts"][0]
        lines += [f"## Eval {ev['id']} — {ev['name']}", "",
                  f"**A: {first['score_a']:g}/10 · B: {first['score_b']:g}/10 · Winner: {first['winner']}**", "",
                  "Reasons:"] + [f"- {r}" for r in first.get("reasons", [])] + [
                  "", "Most serious flaw:", f"- A: {first.get('flaw_a', '')}", f"- B: {first.get('flaw_b', '')}", ""]
    (out / "blind-verdict.md").write_text("\n".join(lines), encoding="utf-8")


# --------------------------------------------------------------------------- report

def previous_scores(iteration):
    """with_skill / baseline scores of an earlier iteration (verdict.json, or the iteration-1 markdown)."""
    prev = iteration_dir(iteration)
    if (prev / "verdict.json").exists():
        return {k: v["scores"] for k, v in read_json(prev / "verdict.json", {}).items()}
    md, mapping = prev / "blind-verdict.md", read_json(prev / "blind-mapping.json", {})
    if not md.exists() or not mapping:
        return {}
    scores = {}
    for eid, a, b in re.findall(r"## Eval (\d+).*?\*\*A: ([\d.]+)/10 · B: ([\d.]+)/10", md.read_text(encoding="utf-8"), re.S):
        if eid in mapping:
            scores[eid] = {mapping[eid]["A"]: float(a), mapping[eid]["B"]: float(b)}
    return scores


def cmd_report(args):
    out = iteration_dir(args.iteration)
    verdicts = read_json(out / "verdict.json", {})
    checks = read_json(out / "checks.json", {})
    runs = read_json(out / "runs.json", {})
    meta = read_json(out / "meta.json", {})
    prev = previous_scores(args.iteration - 1) if args.iteration > 1 else {}
    evals = load_evals(args.ids)

    lines = [f"# Evals — iteration {args.iteration}", "",
             f"Baseline: `{meta.get('baseline', '?')}` · trigger: `{meta.get('trigger', '?')}` · "
             f"generation model: `{meta.get('model', '?')}`", "",
             "| Eval | Task | With skill | Baseline | Winner | Prev. with skill | check_lyrics errors (skill / base) |",
             "|---|---|---|---|---|---|---|"]
    wins = {"with_skill": 0, "baseline": 0, "tie": 0}
    totals = {"with_skill": [], "baseline": []}
    for ev in evals:
        v = verdicts.get(str(ev["id"]))
        if ev["skill"] == "none" or not v:
            continue
        s = v["scores"]
        wins[v["winner"]] += 1
        for c in totals:
            totals[c].append(s[c])
        p = prev.get(str(ev["id"]), {}).get("with_skill")
        c = checks.get(str(ev["id"]), {})
        errs = (f"{len(c.get('with_skill', {}).get('errors', []))} / {len(c.get('baseline', {}).get('errors', []))}"
                if ev["skill"] == SONG_SKILL else "—")
        winner = {"with_skill": "skill", "baseline": "baseline", "tie": "tie"}[v["winner"]]
        lines.append(f"| {ev['id']} | {ev['name']} | {s['with_skill']:g} | {s['baseline']:g} | {winner} | "
                     f"{'—' if p is None else f'{p:g}'} | {errs} |")
    if totals["with_skill"]:
        avg = {c: sum(t) / len(t) for c, t in totals.items()}
        lines += ["", f"**Skill wins {wins['with_skill']}, baseline wins {wins['baseline']}, ties {wins['tie']}. "
                      f"Average: with skill {avg['with_skill']:.2f}, baseline {avg['baseline']:.2f}.**"]
        prev_ws = [prev[k]["with_skill"] for k in prev if "with_skill" in prev[k]]
        if prev_ws:
            lines.append(f"Previous iteration, with skill: {sum(prev_ws) / len(prev_ws):.2f} on {len(prev_ws)} evals.")
            prev_judge = read_json(iteration_dir(args.iteration - 1) / "meta.json", {}).get("judge")
            if prev_judge != meta.get("judge"):
                lines.append(f"Note: the previous iteration had a different judge ({prev_judge or 'unknown'} vs "
                             f"{meta.get('judge', 'unknown')}), so compare wins and the pairs themselves, not absolute scores.")

    lines += ["", "## Triggering", ""]
    for ev in evals:
        run = runs.get(str(ev["id"]), {}).get("with_skill")
        if not run:
            continue
        used = run.get("skills") or []
        if ev["skill"] == "none":
            status = "ok" if not used else "FALSE TRIGGER"
        else:
            status = "invoked" if run.get("invoked") else ("ok" if ev["skill"] in used else "not triggered")
        lines.append(f"- eval {ev['id']} ({ev['name']}): expected `{ev['skill']}`, used {used or 'none'} — {status}")

    cost = sum(r.get("cost_usd", 0) for e in runs.values() for r in e.values())
    cost += sum(v.get("cost_usd", 0) for v in verdicts.values())
    lines += ["", f"Cost of this round: ${cost:.2f}.", "",
              "Next: listen to the song evals in Suno v6-mini / Lyria 3.5, note what lost and why in README.md."]
    text = "\n".join(lines) + "\n"
    (out / "summary.md").write_text(text, encoding="utf-8")
    print(text)


# --------------------------------------------------------------------------- CLI

def parse_ids(value):
    return [int(x) for x in value.split(",") if x.strip()] if value else None


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("stage", choices=["generate", "check", "judge", "report", "all"])
    parser.add_argument("--iteration", type=int, required=True, help="results go to evals/results/iteration-N/")
    parser.add_argument("--ids", type=parse_ids, help="comma-separated eval ids (default: all)")
    parser.add_argument("--baseline", default="none", help="none (no skills, default), current, or git:<ref>")
    parser.add_argument("--trigger", choices=["invoke", "natural"], default="invoke",
                        help="invoke (default): call the expected skill explicitly, to measure quality; "
                             "natural: plain prompt, to measure triggering too. Negative controls always run natural")
    parser.add_argument("--model", help="model for the generation runs (default: the CLI default)")
    parser.add_argument("--judge-model", help="model for the judge (default: the CLI default)")
    parser.add_argument("--both-orders", action="store_true", help="judge each pair twice with A/B swapped")
    parser.add_argument("--seed", type=int, help="A/B shuffle seed (default: the iteration number)")
    parser.add_argument("--jobs", type=int, default=4, help="parallel claude runs")
    parser.add_argument("--timeout", type=int, default=900, help="seconds per claude run")
    parser.add_argument("--max-budget-usd", type=float, help="spending cap per generation run")
    parser.add_argument("--force", action="store_true", help="redo finished generations / verdicts")
    args = parser.parse_args(argv)

    stages = ["generate", "check", "judge", "report"] if args.stage == "all" else [args.stage]
    for stage in stages:
        {"generate": cmd_generate, "check": cmd_check, "judge": cmd_judge, "report": cmd_report}[stage](args)


if __name__ == "__main__":
    main()
