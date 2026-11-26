#!/usr/bin/env python3
"""Checks data/components.toml against what the templates expect. Usage: check-components.py [site root]

Hugo only fails on a few of these (a missing shot, a missing language table on a page); the rest would render a
broken or empty section without a warning. The file has at least one [[components]] table. Each component has a
non-empty string id used once, a known group, an icon of its own (the icons are the keys of layouts/_partials/icon.html), the
three language tables with a non-empty name and text, and, when `shot` is set, its file in assets/images/shots.
`page` and `unit` are booleans. A card without a page carries none of the page's fields (PAGE_FIELDS, and the
per-language PAGE_NOTES), since the list shows only its name, text and keys; its `with` names a component that has a
page. `waybar` is only for the bar, as swaydesk-<name>; `unit` needs a start that includes a snippet; a start_note
needs a start; start_text (what to do when there's nothing to add to the Sway config) replaces start, in every
language or none. `crop = true` shows the page's own image, assets/images/components/<id>.webp, which must
exist (on a card without a page, as a thumbnail in the list); `more_shots` (at most four names of files in that folder, only on a page) adds thumbnails, each with a
`more_alts` text in every language, and the main image's `shot_caption` in every language. Each [groups.<group>] is a known group with a text in every language. A
missing, unreadable or malformed file is an error, never a pass.
"""
import pathlib
import re
import sys
import tomllib

GROUPS = ("bar", "windows", "session", "apps")
LANGS = ("pt-br", "en-us", "es")
PAGE_FIELDS = ("package", "arch_with", "optional", "start", "start_file", "unit", "waybar")
PAGE_NOTES = ("note", "start_note", "start_text", "arch_note", "waybar_note")
SNIPPETS = "include /usr/share/swaydesk/sway/config.d/"
ICONS = "layouts/_partials/icon.html"
CROPS = "assets/images/components"
MAX_MORE = 4


def text(value):
    return isinstance(value, str) and bool(value.strip())


def check_component(root, c, number, icons, pages, seen, icon_of):
    errors = []
    cid = c.get("id")
    if not text(cid):
        return [f"component {number}: id must be a non-empty string"]
    if cid in seen:
        errors.append(f"{cid}: the id is used twice")
    seen.add(cid)
    for flag in ("page", "unit", "crop"):
        if flag in c and not isinstance(c[flag], bool):
            errors.append(f"{cid}: {flag} must be true or false")
    if c.get("group") not in GROUPS:
        errors.append(f"{cid}: unknown group {c.get('group')}")
    icon = c.get("icon")
    if icons and not (isinstance(icon, str) and icon in icons):
        errors.append(f"{cid}: unknown icon {icon}")
    elif isinstance(icon, str):
        if icon in icon_of:
            errors.append(f"{cid}: icon {icon} is already the icon of {icon_of[icon]}")
        else:
            icon_of[icon] = cid
    shot = c.get("shot", "")
    if not isinstance(shot, str):
        errors.append(f"{cid}: shot must be a string")
    elif shot and not (root / f"assets/images/shots/{shot}.webp").is_file():
        errors.append(f"{cid}: assets/images/shots/{shot}.webp doesn't exist")
    has_page = c.get("page") is True
    if c.get("crop") is True and not (root / f"{CROPS}/{cid}.webp").is_file():
        errors.append(f"{cid}: {CROPS}/{cid}.webp doesn't exist")
    more = c.get("more_shots")
    if more is not None:
        if not (isinstance(more, list) and more and all(text(m) for m in more)):
            errors.append(f"{cid}: more_shots must be a non-empty list of names")
            more = None
        elif len(more) > MAX_MORE:
            errors.append(f"{cid}: more_shots has {len(more)} items, at most {MAX_MORE}")
        else:
            errors += [f"{cid}: {CROPS}/{m}.webp doesn't exist" for m in more if not (root / f"{CROPS}/{m}.webp").is_file()]
        if more is not None and not has_page:
            errors.append(f"{cid}: more_shots on a card without a page")
    start = c.get("start", "")
    for code in LANGS:
        table = c.get(code)
        if not isinstance(table, dict):
            errors.append(f"{cid}: no [components.{code}]")
            continue
        for field in ("name", "text"):
            if not text(table.get(field)):
                errors.append(f"{cid}: {code} {field} must be a non-empty string")
        if table.get("start_note") and not start:
            errors.append(f"{cid}: {code} start_note without a start")
        if table.get("start_text") and start:
            errors.append(f"{cid}: {code} start_text next to a start")
        if not has_page:
            errors += [f"{cid}: {code} {f} on a card without a page" for f in PAGE_NOTES if table.get(f)]
        errors += [f"{cid}: {code} {f} must be a string" for f in PAGE_NOTES if not isinstance(table.get(f, ""), str)]
        caption = table.get("shot_caption")
        if caption is not None and not text(caption):
            errors.append(f"{cid}: {code} shot_caption must be a non-empty string")
        elif caption is not None and not isinstance(c.get("more_shots"), list):
            errors.append(f"{cid}: {code} shot_caption without more_shots")
        elif caption is None and isinstance(c.get("more_shots"), list):
            errors.append(f"{cid}: {code} shot_caption missing (the main image's caption, needed with more_shots)")
        alts = table.get("more_alts")
        if alts is not None and not (isinstance(alts, list) and all(text(a) for a in alts)):
            errors.append(f"{cid}: {code} more_alts must be non-empty strings")
        elif alts is not None and not isinstance(c.get("more_shots"), list):
            errors.append(f"{cid}: {code} more_alts without more_shots")
        elif isinstance(c.get("more_shots"), list) and len(alts or []) != len(c["more_shots"]):
            errors.append(f"{cid}: {code} more_alts has {len(alts or [])} items, more_shots has {len(c['more_shots'])}")
    for field in ("package", "start", "start_file"):
        if not isinstance(c.get(field, ""), str):
            errors.append(f"{cid}: {field} must be a string")
    for field in ("arch_with", "optional"):
        value = c.get(field, [])
        if not (isinstance(value, list) and all(isinstance(v, str) for v in value)):
            errors.append(f"{cid}: {field} must be a list of strings")
    with_text = [code for code in LANGS if isinstance(c.get(code), dict) and c[code].get("start_text")]
    if with_text:
        errors += [f"{cid}: start_text missing in {code}" for code in LANGS if code not in with_text]
    if not has_page:
        errors += [f"{cid}: {field} on a card without a page" for field in PAGE_FIELDS if c.get(field)]
        target = c.get("with")
        if target is not None and not isinstance(target, str):
            errors.append(f"{cid}: with must be a string")
        elif target and target not in pages:
            errors.append(f"{cid}: with = {target} is not a component with a page")
    waybar = c.get("waybar", "")
    if not isinstance(waybar, str):
        errors.append(f"{cid}: waybar must be a string")
    elif waybar and c.get("group") != "bar":
        errors.append(f"{cid}: waybar outside the bar group")
    elif waybar and not re.fullmatch(r"swaydesk-[a-z]+(-[a-z]+)*", waybar):
        errors.append(f"{cid}: waybar {waybar} isn't swaydesk-<name>")
    if c.get("unit") is True and not (isinstance(start, str) and start.startswith(SNIPPETS)):
        errors.append(f"{cid}: unit = true needs a start that includes {SNIPPETS.removeprefix('include ')}")
    return errors


def check(root):
    data = tomllib.loads((root / "data/components.toml").read_text(encoding="utf-8"))
    icons = set(re.findall(r'(?m)^\s*"([a-z0-9-]+)" `', (root / ICONS).read_text(encoding="utf-8")))
    components = data.get("components")
    if not isinstance(components, list) or not components:
        return ["no [[components]] tables"]
    errors = [] if icons else [f"no icons found in {ICONS}"]
    tables = []
    for number, c in enumerate(components, 1):
        if isinstance(c, dict):
            tables.append((number, c))
        else:
            errors.append(f"component {number} is not a table")
    pages = {c.get("id") for _, c in tables if c.get("page") is True and isinstance(c.get("id"), str)}
    seen, icon_of = set(), {}
    for number, c in tables:
        errors += check_component(root, c, number, icons, pages, seen, icon_of)
    groups = data.get("groups", {})
    if not isinstance(groups, dict):
        return errors + ["groups is not a table"]
    for name, group in groups.items():
        if not isinstance(group, dict):
            errors.append(f"groups.{name} is not a table")
            continue
        if name not in GROUPS:
            errors.append(f"groups.{name}: unknown group")
        for code in LANGS:
            table = group.get(code)
            if not (isinstance(table, dict) and text(table.get("text"))):
                errors.append(f"groups.{name}: no {code} text")
    return errors


def main(argv):
    root = pathlib.Path(argv[1] if len(argv) > 1 else ".")
    try:
        errors = check(root)
    except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    for line in errors:
        print(line)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
