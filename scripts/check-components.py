#!/usr/bin/env python3
"""Checks data/components.toml against what the templates expect. Usage: check-components.py [site root]

Hugo only fails on a few of these (a missing shot, a missing language table on a page); the rest would render a
broken or empty section without a warning. Each component needs a known group and icon, a unique id, the three
language tables with a name and a text, and its shot in assets/images/shots. A card without a page carries no page
fields, and its `with` names a component that has one. `waybar` is only for the bar, as swaydesk-<name>; `unit`
needs a start that includes a snippet; a start_note needs a start. Each [groups.<group>] is a list section with a
text in every language. A missing or unreadable file is an error, never a pass.
"""
import pathlib
import re
import sys
import tomllib

GROUPS = ("bar", "windows", "session", "apps")
LANGS = ("pt-br", "en-us", "es")
PAGE_FIELDS = ("package", "start", "waybar", "unit")
SNIPPETS = "include /usr/share/swaydesk/sway/config.d/"


def check(root):
    data = tomllib.loads((root / "data/components.toml").read_text(encoding="utf-8"))
    icons = set(re.findall(r'(?m)^\s*"([a-z]+)" `', (root / "layouts/_partials/icon.html").read_text(encoding="utf-8")))
    components = data["components"]
    pages = {c["id"] for c in components if c.get("page")}
    errors, seen = [], set()
    for c in components:
        cid = c.get("id", "?")
        if cid in seen:
            errors.append(f"{cid}: the id is used twice")
        seen.add(cid)
        if c.get("group") not in GROUPS:
            errors.append(f"{cid}: unknown group {c.get('group')}")
        if c.get("icon") not in icons:
            errors.append(f"{cid}: unknown icon {c.get('icon')}")
        shot = c.get("shot", "")
        if shot and not (root / f"assets/images/shots/{shot}.webp").is_file():
            errors.append(f"{cid}: assets/images/shots/{shot}.webp doesn't exist")
        for code in LANGS:
            table = c.get(code)
            if not isinstance(table, dict):
                errors.append(f"{cid}: no [components.{code}]")
                continue
            for field in ("name", "text"):
                if not str(table.get(field, "")).strip():
                    errors.append(f"{cid}: {code} {field} is empty")
            if table.get("start_note") and not c.get("start"):
                errors.append(f"{cid}: {code} start_note without a start")
        if not c.get("page"):
            for field in PAGE_FIELDS:
                if c.get(field):
                    errors.append(f"{cid}: {field} on a card without a page")
            target = c.get("with")
            if target and target not in pages:
                errors.append(f"{cid}: with = {target} is not a component with a page")
        waybar = c.get("waybar", "")
        if waybar and c.get("group") != "bar":
            errors.append(f"{cid}: waybar outside the bar group")
        elif waybar and not re.fullmatch(r"swaydesk-[a-z]+(-[a-z]+)*", waybar):
            errors.append(f"{cid}: waybar {waybar} isn't swaydesk-<name>")
        if c.get("unit") and not str(c.get("start", "")).startswith(SNIPPETS):
            errors.append(f"{cid}: unit = true needs a start that includes {SNIPPETS.removeprefix('include ')}")
    for name, group in data.get("groups", {}).items():
        if name not in GROUPS:
            errors.append(f"groups.{name}: unknown group")
        for code in LANGS:
            if not str(group.get(code, {}).get("text", "")).strip():
                errors.append(f"groups.{name}: no {code} text")
    return errors


def main(argv):
    root = pathlib.Path(argv[1] if len(argv) > 1 else ".")
    try:
        errors = check(root)
    except (OSError, KeyError, tomllib.TOMLDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    for line in errors:
        print(line)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
