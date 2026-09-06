"""
Verification test script for Milestone 4 (Prompt Playground) examples.
Validates all 6 files in examples/success/ and examples/failures/ against
the ecosystem validators: MetatagValidator, SunoValidator, PoeticValidator.
"""

import re
import sys
from pathlib import Path

# Add tests/ to sys.path
sys.path.insert(0, str(Path(__file__).parent))

from validator.metatag_validator import MetatagValidator
from validator.poetic_validator import PoeticValidator
from validator.suno_validator import SunoValidator


def test_files_exist_and_non_empty():
    expected_files = [
        "examples/success/suno-darkwave-postpunk.md",
        "examples/success/udio-triphop-downtempo.md",
        "examples/success/flowmusic-cinematic-ambient.md",
        "examples/failures/lyrics-rushing-fix.md",
        "examples/failures/robotic-vocals-fix.md",
        "examples/failures/true-peak-clipping-fix.md",
    ]
    for rel_path in expected_files:
        p = Path(rel_path)
        assert p.exists(), f"Missing expected file: {rel_path}"
        content = p.read_text(encoding="utf-8")
        assert len(content) > 1500, f"File {rel_path} has suspiciously short content ({len(content)} chars)"
        print(f"[OK] {rel_path} exists ({len(content)} chars)")


def test_suno_darkwave_validation():
    p = Path("examples/success/suno-darkwave-postpunk.md")
    content = p.read_text(encoding="utf-8")
    
    # Check Style Prompt
    m2_style = "ukrainian post-punk, darkwave, 132 bpm, driving chorus bassline, melancholic baritone male vocal, sharp cutting telecaster, analog synths, lo-fi tape hiss"
    assert m2_style in content
    style_res = SunoValidator.validate_suno_style(m2_style)
    assert style_res.is_valid, f"Style validation errors: {style_res.errors}"
    assert 80 <= len(m2_style) <= 180, f"Style length out of range: {len(m2_style)}"

    # Check Exclude Prompt
    exclude = "cheesy pop brass, polished autotune pop, wedding accordion, bright acoustic strumming, generic euro-pop, metallic highs, muddy sub-bass"
    assert exclude in content
    exc_res = SunoValidator.validate_suno_exclude(exclude)
    assert exc_res.is_valid, f"Exclude validation errors: {exc_res.errors}"

    # Extract Lyrics
    match = re.search(r"(\[Vocal Intro[\s\S]*?\[Cold End\])", content)
    assert match, "Lyrics block not found in Suno example"
    lyrics = match.group(1)
    
    meta_res = MetatagValidator.validate_lyrics_structure(lyrics)
    assert meta_res.is_valid, f"Metatag errors in Suno lyrics: {meta_res.errors}"
    
    surz = PoeticValidator.check_surzhyk_and_russianisms(lyrics)
    assert len(surz) == 0, f"Surzhyk found in Suno lyrics: {surz}"
    
    # Verify stressed vowels capitalized
    stressed_words = ["дорОга", "вИпадок", "чорнОзем", "прИйде", "СердЕнько"]
    for word in stressed_words:
        assert word in lyrics or (word[0].upper() + word[1:]) in lyrics, f"Missing stressed word '{word}' in Suno lyrics"

    print("[OK] Suno Darkwave Post-Punk fully validated")


def test_udio_triphop_validation():
    p = Path("examples/success/udio-triphop-downtempo.md")
    content = p.read_text(encoding="utf-8")
    
    # Check Udio prompt
    udio_prompt = "ukrainian trip-hop, downtempo, 82 bpm, *breathy intimate female vocal*, heavy vinyl dust, hypnotic Rhodes piano, syncopated breakbeat, dub bass, dark cinema atmosphere, vintage tape saturation"
    assert udio_prompt in content
    assert len(udio_prompt) <= 250, f"Udio prompt exceeds 250 chars ({len(udio_prompt)})"
    
    udio_res = SunoValidator.validate_udio_prompt(udio_prompt)
    assert udio_res.is_valid, f"Udio prompt errors: {udio_res.errors}"
    assert udio_res.metrics["has_inpainting_tags"] is True

    # Extract Lyrics
    match = re.search(r"(\[Intro[\s\S]*?\[End\])", content)
    assert match, "Lyrics block not found in Udio example"
    lyrics = match.group(1)
    
    meta_res = MetatagValidator.validate_lyrics_structure(lyrics)
    assert meta_res.is_valid, f"Metatag errors in Udio lyrics: {meta_res.errors}"
    
    surz = PoeticValidator.check_surzhyk_and_russianisms(lyrics)
    assert len(surz) == 0, f"Surzhyk found in Udio lyrics: {surz}"

    print("[OK] Udio Trip-Hop Downtempo fully validated")


def test_flowmusic_ambient_validation():
    p = Path("examples/success/flowmusic-cinematic-ambient.md")
    content = p.read_text(encoding="utf-8")
    
    # Check Flow prompt
    assert "Create an expansive, cinematic Ukrainian ambient soundtrack" in content
    
    # Extract Lyrics
    match = re.search(r"(\[Intro[\s\S]*?\[Silence\])", content)
    assert match, "Lyrics block not found in Flow Music example"
    lyrics = match.group(1)
    
    meta_res = MetatagValidator.validate_lyrics_structure(lyrics)
    assert meta_res.is_valid, f"Metatag errors in Flow lyrics: {meta_res.errors}"
    
    surz = PoeticValidator.check_surzhyk_and_russianisms(lyrics)
    assert len(surz) == 0, f"Surzhyk found in Flow lyrics: {surz}"

    print("[OK] Google Flow Music Ambient fully validated")


def test_failures_guides_validation():
    # 1. lyrics-rushing-fix.md
    p1 = Path("examples/failures/lyrics-rushing-fix.md").read_text(encoding="utf-8")
    assert "half-time feel" in p1
    assert "4–8" in p1 or "4-8" in p1
    assert "Spoken Prosody Test" in p1

    # 2. robotic-vocals-fix.md
    p2 = Path("examples/failures/robotic-vocals-fix.md").read_text(encoding="utf-8")
    assert "Vocal Triple-Stack" in p2
    assert "Character" in p2 and "Delivery" in p2 and "FX" in p2
    assert "robotic autotune" in p2

    # 3. true-peak-clipping-fix.md
    p3 = Path("examples/failures/true-peak-clipping-fix.md").read_text(encoding="utf-8")
    assert "-1.0 dBTP" in p3
    assert "True Peak" in p3
    assert "Split Compression" in p3
    assert "Tchad Blake" in p3

    print("[OK] All 3 failure remediation guides contain expected core methodologies")


if __name__ == "__main__":
    test_files_exist_and_non_empty()
    test_suno_darkwave_validation()
    test_udio_triphop_validation()
    test_flowmusic_ambient_validation()
    test_failures_guides_validation()
    print("\n=================================================")
    print("ALL M4 PLAYGROUND EXAMPLES SUCCESSFULLY VERIFIED!")
    print("=================================================")
