#!/usr/bin/env python3
"""Tests of check-components.py. Run: python3 -I -m unittest discover -s scripts -p 'test_*.py'"""
import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent / "check-components.py"
REPO = SCRIPT.parent.parent

ICONS = '{{- $p := dict\n  "bar" `<rect/>`\n  "lock" `<rect/>`\n}}\n'


def lang(code, name="Name", text="Text."):
    return f'  [components.{code}]\n  name = "{name}"\n  text = "{text}"\n  keys = ""\n  guide = ""\n'


def component(cid="dock", group="session", icon="lock", shot="", page="true", extra="", langs=None):
    body = (f'[[components]]\nid = "{cid}"\ngroup = "{group}"\nicon = "{icon}"\nshot = "{shot}"\n'
            f'page = {page}\n{extra}')
    return body + "".join(langs if langs is not None else (lang("pt-br"), lang("en-us"), lang("es"))) + "\n"


class CheckComponentsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)
        (self.root / "data").mkdir()
        (self.root / "layouts/_partials").mkdir(parents=True)
        (self.root / "layouts/_partials/icon.html").write_text(ICONS, encoding="utf-8")
        (self.root / "assets/images/shots").mkdir(parents=True)
        (self.root / "assets/images/shots/dock.webp").write_bytes(b"RIFF")

    def tearDown(self):
        self.tmp.cleanup()

    def run_on(self, toml):
        (self.root / "data/components.toml").write_text(toml, encoding="utf-8")
        return subprocess.run([sys.executable, "-I", str(SCRIPT), str(self.root)], capture_output=True, text=True)

    def assert_fails_with(self, toml, message):
        result = self.run_on(toml)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(message, result.stdout)

    def test_the_real_data_passes(self):
        result = subprocess.run([sys.executable, "-I", str(SCRIPT), str(REPO)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_a_valid_file_passes(self):
        result = self.run_on(component(shot="dock"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_a_missing_file_fails(self):
        result = subprocess.run([sys.executable, "-I", str(SCRIPT), str(self.root / "nothing")],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)

    def test_a_missing_language_fails(self):
        self.assert_fails_with(component(langs=[lang("pt-br"), lang("en-us")]), "dock: no [components.es]")

    def test_an_empty_name_fails(self):
        self.assert_fails_with(component(langs=[lang("pt-br"), lang("en-us", name=""), lang("es")]),
                               "dock: en-us name is empty")

    def test_an_unknown_group_fails(self):
        self.assert_fails_with(component(group="tray"), "dock: unknown group tray")

    def test_an_unknown_icon_fails(self):
        self.assert_fails_with(component(icon="star"), "dock: unknown icon star")

    def test_a_missing_shot_fails(self):
        self.assert_fails_with(component(shot="nope"), "dock: assets/images/shots/nope.webp doesn't exist")

    def test_a_duplicate_id_fails(self):
        self.assert_fails_with(component() + component(), "dock: the id is used twice")

    def test_with_must_name_a_page(self):
        self.assert_fails_with(component(cid="rec", page="false", extra='with = "missing"\n'),
                               "rec: with = missing is not a component with a page")

    def test_waybar_outside_the_bar_fails(self):
        self.assert_fails_with(component(extra='waybar = "swaydesk-dock"\n'), "dock: waybar outside the bar group")

    def test_a_bad_waybar_name_fails(self):
        self.assert_fails_with(component(cid="audio", group="bar", extra='waybar = "custom/audio"\n'),
                               "audio: waybar custom/audio isn't swaydesk-<name>")

    def test_unit_without_an_include_fails(self):
        self.assert_fails_with(component(extra='start = "exec swaydesk-dock"\nunit = true\n'),
                               "dock: unit = true needs a start that includes /usr/share/swaydesk/sway/config.d/")

    def test_a_start_note_without_start_fails(self):
        langs = [lang("pt-br"), lang("en-us") + '  start_note = "A note."\n', lang("es")]
        self.assert_fails_with(component(langs=langs), "dock: en-us start_note without a start")

    def test_page_fields_on_a_card_without_a_page_fail(self):
        self.assert_fails_with(component(page="false", extra='package = "swaydesk-dock"\n'),
                               "dock: package on a card without a page")

    def test_a_group_without_a_language_text_fails(self):
        group = '[groups.session]\npackage = "swaydesk-session"\n  [groups.session.pt-br]\n  text = "T"\n'
        self.assert_fails_with(component() + group, "groups.session: no en-us text")

    def test_a_group_that_isnt_a_section_fails(self):
        group = ('[groups.tray]\npackage = "swaydesk-tray"\n' +
                 "".join(f'  [groups.tray.{c}]\n  text = "T"\n' for c in ("pt-br", "en-us", "es")))
        self.assert_fails_with(component() + group, "groups.tray: unknown group")


if __name__ == "__main__":
    unittest.main()
