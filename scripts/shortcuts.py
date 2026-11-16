#!/usr/bin/env python3
"""Gera data/shortcuts.json, os atalhos de cada perfil para a página Atalhos, a partir do código do Swaydesk.

    python3 -I scripts/shortcuts.py CODE_DIR [REF]

CODE_DIR é um checkout do sway-desktop. Com REF (um commit ou branch), os arquivos vêm de `git show REF:…`;
sem ele, da pasta. Lê home/.config/sway/keys/base.conf e keys/<perfil>.conf, como o config.d/00-keys.conf
os inclui, e po/pt_BR.po para o português.

É uma cópia em Python do que a Ajuda do Swaydesk faz (rust/help-logic: parse.rs e keys.rs; rust/help: as
seções, o "or", o modo): "### Texto" abre uma seção, "## Texto" descreve o bind logo abaixo e os colados a
ele, um bind com as mesmas teclas depois troca o de antes, `unbindsym` tira. Assim o site mostra o mesmo que a
Ajuda mostra com cada perfil, sem o 50-local.conf de ninguém.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

PROFILES = ["swaydesk", "i3", "hyprland", "niri", "dwm"]
# O que o config principal define antes de incluir os atalhos (home/.config/sway/config)
PRELUDE = "set $mod  Mod4\nset $term kitty\nset $bin  ~/.local/bin\nset $lock $bin/sway-lock\n"

MODS = {"mod4": "Super", "super": "Super", "logo": "Super", "mod1": "Alt", "alt": "Alt", "ctrl": "Ctrl",
        "control": "Ctrl", "shift": "Shift", "mod5": "Mod5", "mod3": "Mod3", "mod2": "Mod2", "lock": "Caps",
        "caps": "Caps"}
MOD_ORDER = ["Super", "Ctrl", "Alt", "Shift", "Mod5", "Mod3", "Mod2", "Caps"]
# Os nomes que a Ajuda traduz (Label::Word); o resto (Label::Text) fica como está
WORDS = {
    "Return": "Enter", "KP_Enter": "Enter", "space": "Space", "BackSpace": "Backspace", "Delete": "Del",
    "Insert": "Ins", "Home": "Home", "End": "End", "Page_Up": "PgUp", "Prior": "PgUp", "Page_Down": "PgDn",
    "Next": "PgDn", "Print": "Print Screen", "Super_L": "Super", "Super_R": "Super", "Control_L": "Ctrl",
    "Control_R": "Ctrl", "Shift_L": "Shift", "Shift_R": "Shift", "button1": "Left click",
    "button2": "Middle click", "button3": "Right click", "button4": "Scroll up", "button5": "Scroll down",
    "button6": "Scroll left", "button7": "Scroll right", "button8": "Back button", "button9": "Forward button",
    "XF86AudioRaiseVolume": "Volume up", "XF86AudioLowerVolume": "Volume down", "XF86AudioMute": "Mute",
    "XF86AudioMicMute": "Mute microphone", "XF86AudioPlay": "Play/Pause", "XF86AudioPause": "Pause",
    "XF86AudioStop": "Stop", "XF86AudioNext": "Next track", "XF86AudioPrev": "Previous track",
    "XF86MonBrightnessUp": "Brightness up", "XF86MonBrightnessDown": "Brightness down",
}
MOD_WORDS = {"Super": "Super", "Ctrl": "Ctrl", "Shift": "Shift", "Caps": "Caps Lock"}
SYMBOLS = {
    "Escape": "Esc", "Tab": "Tab", "Left": "←", "Right": "→", "Up": "↑", "Down": "↓", "Alt_L": "Alt",
    "Alt_R": "Alt", "ISO_Level3_Shift": "AltGr", "bracketleft": "[", "bracketright": "]", "braceleft": "{",
    "braceright": "}", "parenleft": "(", "parenright": ")", "slash": "/", "backslash": "\\", "question": "?",
    "minus": "-", "plus": "+", "equal": "=", "comma": ",", "period": ".", "semicolon": ";", "colon": ":",
    "apostrophe": "'", "quotedbl": '"', "grave": "`", "asciitilde": "~", "less": "<", "greater": ">",
    "underscore": "_", "numbersign": "#", "asterisk": "*", "exclam": "!", "at": "@", "dollar": "$",
    "percent": "%", "ampersand": "&", "bar": "|",
}
GESTURE_WORDS = {"swipe": "Swipe", "pinch": "Pinch", "hold": "Hold", "inward": "Inward", "outward": "Outward",
                 "clockwise": "Clockwise", "counterclockwise": "Counterclockwise"}
ARROWS = {"left": "←", "right": "→", "up": "↑", "down": "↓"}


# --- O parser (parse.rs) ---

def tokens(line):
    out, i, n = [], 0, len(line)
    while i < n:
        while i < n and line[i].isspace():
            i += 1
        if i >= n:
            break
        start = i
        if line[i] in "\"'":
            quote = line[i]
            i += 1
            while i < n and line[i] != quote:
                i += 1
            inner = line[start + 1:i]
            i = min(i + 1, n)
            out.append((inner, i))
        else:
            while i < n and not line[i].isspace():
                i += 1
            out.append((line[start:i], i))
    return out


def unquote(text):
    t = text.strip()
    for q in "\"'":
        if len(t) >= 2 and t[0] == q and t[-1] == q:
            return t[1:-1]
    return t


def bind_kind(word):
    return {"bindsym": "sym", "bindcode": "code", "bindgesture": "gesture"}.get(word)


def identity(mode, kind, release, keys):
    if kind == "gesture":
        normal = keys.lower()
    else:
        mods, rest = [], []
        for part in keys.split("+"):
            m = MODS.get(part.lower())
            if m:
                mods.append(m)
            else:
                rest.append(part.lower())
        normal = "+".join(sorted(set(mods)) + rest)
    return (mode, kind, release, normal)


class Parser:
    def __init__(self):
        self.vars = {}
        self.entries = []

    def substitute(self, line):
        if not self.vars or "$" not in line:
            return line
        names = sorted(self.vars, key=len, reverse=True)
        out, rest = [], line
        while "$" in rest:
            pos = rest.index("$")
            out.append(rest[:pos])
            tail = rest[pos:]
            name = next((n for n in names if tail.startswith(n)), None)
            if name:
                out.append(self.vars[name])
                rest = tail[len(name):]
            else:
                out.append("$")
                rest = tail[1:]
        out.append(rest)
        return "".join(out)

    def text(self, text):
        st = {"section": None, "pending": None, "open": None, "blocks": []}
        lines, current = [], ""
        for raw in text.splitlines():
            if raw.endswith("\\"):
                current += raw[:-1]
            else:
                lines.append(current + raw)
                current = ""
        if current:
            lines.append(current)
        for line in lines:
            t = line.strip()
            if not t:
                st["pending"] = st["open"] = None
            elif t.startswith("###"):
                title = t[3:].lstrip("#").strip()
                st["section"] = title or None
                st["pending"] = st["open"] = None
            elif t.startswith("##"):
                st["pending"] = t[2:].strip() or None
                st["open"] = None
            elif t.startswith("#"):
                continue
            elif t == "}":
                if st["blocks"]:
                    st["blocks"].pop()
                st["pending"] = st["open"] = None
            else:
                self.directive(t, st)

    def mode(self, st):
        for kind, value in reversed(st["blocks"]):
            if kind == "mode":
                return value
        return None

    def directive(self, line, st):
        if st["blocks"] and st["blocks"][-1][0] == "bind":
            _, (kind, flags) = st["blocks"][-1]
            line = self.substitute(line)
            toks = tokens(line)
            if toks:
                keys, end = toks[0]
                self.add_bind(st, kind, flags, keys, line[end:].strip())
            return
        first = line.split()[0]
        if first == "set":
            toks = tokens(line)
            if len(toks) > 1 and toks[1][0].startswith("$") and len(toks[1][0]) > 1:
                self.vars[toks[1][0]] = unquote(self.substitute(line[toks[1][1]:].strip()))
            st["pending"] = st["open"] = None
            return
        line = self.substitute(line)
        toks = tokens(line)
        if not toks:
            return
        first, first_end = toks[0]
        if line.endswith("{"):
            head = []
            for t, _ in toks:
                if t == "{":
                    break
                head.append(t)
            kind = bind_kind(first)
            if kind:
                block = ("bind", (kind, [t for t in head[1:] if t.startswith("--")]))
            elif first == "mode":
                names = [t for t in head[1:] if not t.startswith("--")]
                block = ("mode", names[-1]) if names else ("other", None)
            else:
                block = ("other", None)
            if block[0] != "bind":
                st["pending"] = None
            st["open"] = None
            st["blocks"].append(block)
            return
        if first == "include":
            raise SystemExit(f"shortcuts.py: include in a keys file isn't supported: {line}")
        kind = bind_kind(first)
        if kind:
            flags = []
            for tok, end in toks[1:]:
                if tok.startswith("--"):
                    flags.append(tok)
                    continue
                self.add_bind(st, kind, flags, tok, line[end:].strip())
                return
            return
        if first.startswith("un") and bind_kind(first[2:]):
            kind = bind_kind(first[2:])
            keys = next((t for t, _ in toks[1:] if not t.startswith("--")), None)
            if keys:
                release = any(t == "--release" for t, _ in toks)
                wanted = identity(self.mode(st), kind, release, keys)
                for entry in self.entries:
                    entry["binds"] = [b for b in entry["binds"]
                                      if identity(entry["mode"], b["kind"], b["release"], b["keys"]) != wanted]
        st["pending"] = st["open"] = None

    def add_bind(self, st, kind, flags, keys, command):
        if not command:
            return
        bind = {"kind": kind, "keys": keys, "command": command, "locked": "--locked" in flags,
                "release": "--release" in flags}
        if st["open"] is not None:
            self.entries[st["open"]]["binds"].append(bind)
            return
        self.entries.append({"section": st["section"], "mode": self.mode(st), "description": st["pending"],
                             "binds": [bind]})
        if st["pending"] is not None:
            st["open"] = len(self.entries) - 1

    def finish(self):
        seen = set()
        for entry in reversed(self.entries):
            kept = []
            for bind in reversed(entry["binds"]):
                key = identity(entry["mode"], bind["kind"], bind["release"], bind["keys"])
                if key not in seen:
                    seen.add(key)
                    kept.append(bind)
            entry["binds"] = list(reversed(kept))
        return [e for e in self.entries if e["binds"]]


# --- As teclas (keys.rs) ---

def symbol(name):
    if name in SYMBOLS:
        return SYMBOLS[name]
    if len(name) == 1:
        return name.upper()
    return (name[4:] if name.startswith("XF86") else name).replace("_", " ")


def key_label(name):
    return ("word", WORDS[name]) if name in WORDS else ("text", symbol(name))


def chord(bind):
    if bind["kind"] == "gesture":
        out = []
        for part in bind["keys"].split(":"):
            if part in GESTURE_WORDS:
                out.append(("word", GESTURE_WORDS[part]))
            elif part in ARROWS:
                out.append(("text", ARROWS[part]))
            elif part.isdigit():
                out.append(("fingers", int(part)))
            else:
                out.append(("text", part))
        return out
    mods, keys = [], []
    for part in filter(None, bind["keys"].split("+")):
        m = MODS.get(part.lower())
        if m:
            mods.append(m)
        else:
            keys.append(part)
    mods = sorted(set(mods), key=MOD_ORDER.index)
    out = [("word", MOD_WORDS[m]) if m in MOD_WORDS else ("text", {"Mod5": "AltGr"}.get(m, m)) for m in mods]
    for key in keys:
        if bind["kind"] == "code" and key.isdigit():
            out.append(("code", int(key)))
        else:
            out.append(key_label(key))
    dedup = []
    for label in out:
        if not dedup or dedup[-1] != label:
            dedup.append(label)
    return dedup


def chords(entry):
    seen, out = set(), []
    for bind in entry["binds"]:
        c = tuple(chord(bind))
        if c not in seen:
            seen.add(c)
            out.append(list(c))
    if len(out) < 3:
        return out
    prefix = out[0][:-1]
    digits = []
    for c in out:
        last = c[-1]
        if c[:-1] != prefix or last[0] != "text" or len(last[1]) != 1 or not last[1].isdigit():
            return out
        digits.append(int(last[1]))
    if any(b != a + 1 for a, b in zip(digits, digits[1:])):
        return out
    return [prefix + [("text", f"{digits[0]}–{digits[-1]}")]]


def short_command(command):
    words = []
    for word in command.split():
        bare = word.strip("\"'")
        if bare[:1] in ("/", "~") and len(bare) > 1:
            word = bare.rsplit("/", 1)[-1] or bare
        words.append(word)
    return " ".join(words)


# --- A tradução (po/pt_BR.po) ---

def read_po(text):
    """msgid -> msgstr (ou [msgstr[0], msgstr[1]] nos plurais). Sem tradução ou fuzzy fica de fora: vale o
    inglês, como no gettext. Cada entrada do .po é um bloco separado por linha em branco."""
    out = {}
    for block in re.split(r"\n\s*\n", text):
        fields, field, fuzzy = {}, None, False
        for line in block.splitlines():
            line = line.strip()
            if line.startswith("#,") and "fuzzy" in line:
                fuzzy = True
            elif line.startswith("#") or not line:
                continue
            elif line.startswith('"') and field:
                fields[field] += json.loads(line)  # as aspas do .po são as do C, que o JSON lê
            else:
                field, _, rest = line.partition(" ")
                fields[field] = json.loads(rest)
        msgid = fields.get("msgid")
        if not msgid or fuzzy:
            continue
        if "msgid_plural" in fields:
            forms = [fields.get("msgstr[0]", ""), fields.get("msgstr[1]", "")]
            if all(forms):
                out[msgid] = forms
        elif fields.get("msgstr"):
            out[msgid] = fields["msgstr"]
    return out


def label_text(label, tr, lang):
    kind, value = label
    if kind == "text":
        return value
    if kind == "word":
        return tr(value)
    if kind == "fingers":
        forms = PO.get("%d finger") if lang == "pt" else None
        if forms:
            return (forms[0] if value == 1 else forms[1]).replace("%d", str(value))
        return f"{value} finger" + ("" if value == 1 else "s")
    # bindcode: a Ajuda pergunta ao layout em uso; o site mostra a tecla do layout US (o 49 é a à esquerda do 1)
    return {49: "`"}.get(value, f"#{value}")


def render(entries, lang):
    def tr(text):
        if lang == "en":
            return text
        value = PO.get(text)
        return value if isinstance(value, str) else text

    order, groups = [], {}
    for entry in entries:
        if entry["section"]:
            key = tr(entry["section"])
        elif entry["mode"]:
            key = tr("Mode “%s”").replace("%s", entry["mode"])
        else:
            key = None
        if key not in groups:
            order.append(key)
            groups[key] = []
        rows = groups[key]
        rows.append({
            "text": tr(entry["description"]) if entry["description"] else short_command(entry["binds"][0]["command"]),
            "raw": entry["description"] is None,
            "locked": any(b["locked"] for b in entry["binds"]),
            "chords": [[label_text(l, tr, lang) for l in c] for c in chords(entry)],
        })
    order.sort(key=lambda k: k is None)
    return [{"title": k if k is not None else tr("Other"), "rows": groups[k]} for k in order]


def main():
    global PO
    if len(sys.argv) not in (2, 3):
        raise SystemExit(__doc__)
    code = Path(sys.argv[1])
    ref = sys.argv[2] if len(sys.argv) == 3 else None

    def read(path):
        if ref:
            return subprocess.run(["git", "-C", str(code), "show", f"{ref}:{path}"], check=True,
                                  capture_output=True, text=True).stdout
        return (code / path).read_text(encoding="utf-8")

    PO = read_po(read("po/pt_BR.po"))
    base = read("home/.config/sway/keys/base.conf")
    data = {"source": ref or "", "profiles": PROFILES, "en": {}, "pt": {}}
    for profile in PROFILES:
        parser = Parser()
        parser.text(PRELUDE)
        parser.text(base)
        parser.text(read(f"home/.config/sway/keys/{profile}.conf"))
        entries = parser.finish()
        for lang in ("en", "pt"):
            data[lang][profile] = render(entries, lang)
    if ref:
        data["source"] = subprocess.run(["git", "-C", str(code), "rev-parse", "--short", ref], check=True,
                                        capture_output=True, text=True).stdout.strip()
    out = Path(__file__).resolve().parent.parent / "data" / "shortcuts.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{out}: {', '.join(f'{p} {sum(len(s['rows']) for s in data['en'][p])}' for p in PROFILES)}")


PO = {}
if __name__ == "__main__":
    main()
