import pathlib
import re
import sys

# Ensure imports
project_root = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(project_root))

from tests.validator import StyleValidator, MetatagValidator, PoeticValidator

root = project_root
md_files = list(root.glob("**/*.md"))
md_files = [f for f in md_files if not any(p.startswith(".agents") for p in f.parts)]

print(f"Auditing {len(md_files)} markdown files across workspace...")

total_tags = 0
invalid_tags = []
style_prompts = 0
invalid_style = []
exclude_prompts = 0
invalid_exclude = []

style_re = re.compile(r"(?:-\s*\*\*Style of music[^\n]*\*\*:\s*|Style of music:\s*)```(?:text)?\s*([\s\S]*?)```", re.IGNORECASE)
exclude_re = re.compile(r"(?:-\s*\*\*Exclude\*\*:\s*|Exclude:\s*)`([^`]+)`", re.IGNORECASE)

for f in md_files:
    content = f.read_text(encoding="utf-8", errors="ignore")
    
    # Check metatags
    bracket_matches = re.findall(r"\[([^\]\r\n]+)\]", content)
    for tag in bracket_matches:
        if tag in ("x", " ", "TBD", "TBD/None") or tag.isdigit():
            continue
        if any(keyword in tag.lower() for keyword in ["verse", "chorus", "intro", "outro", "drop", "bridge", "solo", "куплет", "приспів", "інтро", "аутро", "міст", "дроп", "соло", "tempo:", "dynamic:"]):
            total_tags += 1
            valid, reason = MetatagValidator.is_valid_tag(tag)
            if not valid:
                invalid_tags.append((str(f.relative_to(root)), tag, reason))
                
    # Check Style prompts
    for match in style_re.finditer(content):
        prompt = match.group(1).strip()
        if prompt and not prompt.startswith("<") and not prompt.startswith("[Genre") and not prompt.startswith("["):
            style_prompts += 1
            res = StyleValidator.validate_style_prompt(prompt, max_chars=180)
            if not res.is_valid:
                invalid_style.append((str(f.relative_to(root)), prompt, res.errors))
                
    # Check Exclude prompts
    for match in exclude_re.finditer(content):
        exc = match.group(1).strip()
        if exc and not exc.startswith("<"):
            exclude_prompts += 1
            res = StyleValidator.validate_exclude_field(exc, max_chars=150)
            if not res.is_valid:
                invalid_exclude.append((str(f.relative_to(root)), exc, res.errors))

print(f"Total metatags audited: {total_tags}, Invalid: {len(invalid_tags)}")
if invalid_tags:
    for f, t, r in invalid_tags:
        print(f"  [TAG ERROR] {f} -> [{t}] ({r})")

print(f"Total Style prompts audited: {style_prompts}, Invalid: {len(invalid_style)}")
if invalid_style:
    for f, p, e in invalid_style:
        print(f"  [STYLE ERROR] {f} -> {p} ({e})")

print(f"Total Exclude prompts audited: {exclude_prompts}, Invalid: {len(invalid_exclude)}")
if invalid_exclude:
    for f, ex, e in invalid_exclude:
        print(f"  [EXCLUDE ERROR] {f} -> {ex} ({e})")
