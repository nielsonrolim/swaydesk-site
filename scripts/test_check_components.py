#!/usr/bin/env python3
"""Tests of check-components.py. Run: python3 -I -m unittest discover -s scripts -p 'test_*.py'"""
import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent / "check-components.py"
REPO = SCRIPT.parent.parent

ICONS = '{{- $p := dict\n  "bar" `<rect/>`\n  "lock" `<rect/>`\n  "grid" `<rect/>`\n}}\n'


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
        (self.root / "assets/images/components").mkdir(parents=True)
        for name in ("dock", "dock-menu", "dock-drag"):
            (self.root / f"assets/images/components/{name}.webp").write_bytes(b"RIFF")

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

    def test_an_all_valid_file_passes(self):
        langs = [lang("pt-br"), lang("en-us") + '  start_note = "A note."\n', lang("es")]
        toml = (component(shot="dock", extra='start = "include /usr/share/swaydesk/sway/config.d/50-swaydesk-dock.conf"\n'
                          'unit = true\npackage = "swaydesk-dock"\narch_with = ["swayidle"]\n', langs=langs)
                + component(cid="audio", group="bar", icon="bar", extra='waybar = "swaydesk-audio"\n')
                + component(cid="rec", icon="grid", page="false", extra='with = "dock"\n')
                + '[groups.bar]\npackage = "swaydesk-bar"\n'
                + "".join(f'  [groups.bar.{c}]\n  text = "T"\n' for c in ("pt-br", "en-us", "es")))
        result = self.run_on(toml)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def assert_clean_error(self, result):
        self.assertEqual(result.returncode, 1)
        self.assertTrue(result.stderr.startswith("error: "), result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_a_missing_file_fails_with_a_message(self):
        self.assert_clean_error(subprocess.run([sys.executable, "-I", str(SCRIPT), str(self.root / "nothing")],
                                               capture_output=True, text=True))

    def test_a_file_that_isnt_utf8_fails_with_a_message(self):
        (self.root / "data/components.toml").write_bytes(b'[[components]]\nid = "\xff"\n')
        self.assert_clean_error(subprocess.run([sys.executable, "-I", str(SCRIPT), str(self.root)],
                                               capture_output=True, text=True))

    def test_no_components_fails(self):
        for toml in ("components = []\n", "", '[components]\nid = "dock"\n'):
            with self.subTest(toml=toml):
                self.assert_fails_with(toml, "no [[components]] tables")

    def test_a_component_that_isnt_a_table_fails(self):
        self.assert_fails_with("components = [1]\n", "component 1 is not a table")

    def test_an_id_must_be_a_non_empty_string(self):
        for extra in ('id = ""\n', 'id = ["a"]\n', ""):
            with self.subTest(extra=extra):
                toml = component().replace('id = "dock"\n', extra)
                self.assert_fails_with(toml, "component 1: id must be a non-empty string")

    def test_page_and_unit_must_be_booleans(self):
        self.assert_fails_with(component(page='"no"'), "dock: page must be true or false")
        self.assert_fails_with(component(extra='unit = "yes"\n'), "dock: unit must be true or false")

    def test_no_icons_in_the_partial_fails_once(self):
        (self.root / "layouts/_partials/icon.html").write_text("{{ nothing }}\n", encoding="utf-8")
        result = self.run_on(component())
        self.assertEqual(result.returncode, 1)
        self.assertIn("no icons found in layouts/_partials/icon.html", result.stdout)
        self.assertNotIn("unknown icon", result.stdout)

    def test_a_missing_language_fails(self):
        self.assert_fails_with(component(langs=[lang("pt-br"), lang("en-us")]), "dock: no [components.es]")

    def test_an_empty_name_fails(self):
        self.assert_fails_with(component(langs=[lang("pt-br"), lang("en-us", name=""), lang("es")]),
                               "dock: en-us name must be a non-empty string")

    def test_an_empty_text_fails(self):
        self.assert_fails_with(component(langs=[lang("pt-br"), lang("en-us"), lang("es", text=" ")]),
                               "dock: es text must be a non-empty string")

    def test_a_name_that_isnt_a_string_fails(self):
        langs = [lang("pt-br"), lang("en-us").replace('name = "Name"', "name = false"), lang("es")]
        self.assert_fails_with(component(langs=langs), "dock: en-us name must be a non-empty string")

    def test_an_unknown_group_fails(self):
        self.assert_fails_with(component(group="tray"), "dock: unknown group tray")

    def test_two_components_sharing_an_icon_fail(self):
        self.assert_fails_with(component() + component(cid="lock"), "lock: icon lock is already the icon of dock")

    def test_an_unknown_icon_fails(self):
        self.assert_fails_with(component(icon="star"), "dock: unknown icon star")

    def test_an_icon_that_isnt_a_string_fails(self):
        self.assert_fails_with(component().replace('icon = "lock"', 'icon = ["lock"]'), "dock: unknown icon ['lock']")

    def test_a_shot_that_isnt_a_string_fails(self):
        self.assert_fails_with(component(shot="x").replace('shot = "x"', "shot = true"), "dock: shot must be a string")

    def test_page_fields_of_the_wrong_type_fail(self):
        fields = {"package": "5", "start": "5", "start_file": "5", "arch_with": '"swayidle"', "optional": "[1]"}
        for field, value in fields.items():
            with self.subTest(field=field):
                self.assert_fails_with(component(extra=f"{field} = {value}\n"),
                                       f"dock: {field} must be {'a list of strings' if field in ('arch_with', 'optional') else 'a string'}")

    def test_page_notes_of_the_wrong_type_fail(self):
        for field in ("note", "start_note", "start_text", "arch_note", "waybar_note"):
            with self.subTest(field=field):
                langs = [lang("pt-br"), lang("en-us") + f"  {field} = 3\n", lang("es")]
                self.assert_fails_with(component(extra='start = "include x"\n', langs=langs),
                                       f"dock: en-us {field} must be a string")

    def test_a_missing_shot_fails(self):
        self.assert_fails_with(component(shot="nope"), "dock: assets/images/shots/nope.webp doesn't exist")

    def test_a_duplicate_id_fails(self):
        self.assert_fails_with(component() + component(), "dock: the id is used twice")

    def test_with_must_name_a_page(self):
        self.assert_fails_with(component(cid="rec", page="false", extra='with = "missing"\n'),
                               "rec: with = missing is not a component with a page")

    def test_with_cannot_name_a_card_without_a_page(self):
        toml = component(cid="cam", page="false") + component(cid="rec", page="false", extra='with = "cam"\n')
        self.assert_fails_with(toml, "rec: with = cam is not a component with a page")

    def test_with_must_be_a_string(self):
        self.assert_fails_with(component(cid="rec", page="false", extra='with = ["dock"]\n'),
                               "rec: with must be a string")

    def test_waybar_outside_the_bar_fails(self):
        self.assert_fails_with(component(extra='waybar = "swaydesk-dock"\n'), "dock: waybar outside the bar group")

    def test_a_bad_waybar_name_fails(self):
        for name in ("custom/audio", "swaydesk-", "swaydesk-Audio"):
            with self.subTest(name=name):
                self.assert_fails_with(component(cid="audio", group="bar", extra=f'waybar = "{name}"\n'),
                                       f"audio: waybar {name} isn't swaydesk-<name>")

    def test_a_waybar_that_isnt_a_string_fails(self):
        self.assert_fails_with(component(cid="audio", group="bar", extra="waybar = 1\n"),
                               "audio: waybar must be a string")

    def test_unit_without_an_include_fails(self):
        self.assert_fails_with(component(extra='start = "exec swaydesk-dock"\nunit = true\n'),
                               "dock: unit = true needs a start that includes /usr/share/swaydesk/sway/config.d/")

    def test_a_start_note_without_start_fails(self):
        langs = [lang("pt-br"), lang("en-us") + '  start_note = "A note."\n', lang("es")]
        self.assert_fails_with(component(langs=langs), "dock: en-us start_note without a start")

    def test_start_text_and_start_together_fail(self):
        langs = [lang(c) + '  start_text = "Nothing to start."\n' for c in ("pt-br", "en-us", "es")]
        self.assert_fails_with(component(extra='start = "exec x"\n', langs=langs),
                               "dock: en-us start_text next to a start")

    def test_start_text_in_one_language_only_fails(self):
        langs = [lang("pt-br"), lang("en-us") + '  start_text = "Nothing to start."\n', lang("es")]
        self.assert_fails_with(component(langs=langs), "dock: start_text missing in pt-br")

    def test_start_text_in_every_language_passes(self):
        langs = [lang(c) + '  start_text = "Nothing to start."\n' for c in ("pt-br", "en-us", "es")]
        result = self.run_on(component(langs=langs))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def more(self, shots='["dock-menu", "dock-drag"]', alts=None, page="true", crop=""):
        alts = alts if alts is not None else ['["Menu.", "Drag."]'] * 3
        langs = [lang(c) + (f"  more_alts = {a}\n" if a else "") for c, a in zip(("pt-br", "en-us", "es"), alts)]
        extra = (f"more_shots = {shots}\n" if shots else "") + crop
        return component(page=page, extra=extra, langs=langs)

    def test_a_crop_and_more_shots_pass(self):
        result = self.run_on(self.more(crop="crop = true\n"))
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_a_crop_needs_its_file(self):
        self.assert_fails_with(component(cid="audio", icon="bar", extra="crop = true\n"),
                               "audio: assets/images/components/audio.webp doesn't exist")

    def test_crop_must_be_a_boolean(self):
        self.assert_fails_with(component(extra='crop = "yes"\n'), "dock: crop must be true or false")

    def test_more_shots_need_their_files(self):
        self.assert_fails_with(self.more(shots='["dock-menu", "nope"]'),
                               "dock: assets/images/components/nope.webp doesn't exist")

    def test_more_shots_must_be_a_list_of_names(self):
        for shots in ('"dock-menu"', '["dock-menu", ""]', '["dock-menu", 2]', "[]"):
            with self.subTest(shots=shots):
                self.assert_fails_with(self.more(shots=shots), "dock: more_shots must be a non-empty list of names")

    def test_at_most_four_more_shots(self):
        names = ", ".join(['"dock-menu"'] * 5)
        alts = [f'[{", ".join(["{0}"] * 5)}]'.format('"A."')] * 3
        self.assert_fails_with(self.more(shots=f"[{names}]", alts=alts), "dock: more_shots has 5 items, at most 4")

    def test_more_alts_must_match_more_shots_in_every_language(self):
        self.assert_fails_with(self.more(alts=['["Menu.", "Drag."]', '["Menu."]', '["Menú.", "Arrastre."]']),
                               "dock: en-us more_alts has 1 items, more_shots has 2")
        self.assert_fails_with(self.more(alts=['["Menu.", "Drag."]', "", '["Menú.", "Arrastre."]']),
                               "dock: en-us more_alts has 0 items, more_shots has 2")
        self.assert_fails_with(self.more(alts=['["Menu.", ""]'] * 3), "dock: pt-br more_alts must be non-empty strings")

    def test_more_alts_without_more_shots_fail(self):
        self.assert_fails_with(self.more(shots=""), "dock: pt-br more_alts without more_shots")

    def test_more_shots_on_a_card_without_a_page_fail(self):
        self.assert_fails_with(self.more(page="false"), "dock: more_shots on a card without a page")

    def test_page_fields_on_a_card_without_a_page_fail(self):
        fields = {"package": '"swaydesk-dock"', "arch_with": '["swayidle"]', "optional": '["x"]',
                  "start": '"include x"', "start_file": '"~/x"', "unit": "true", "waybar": '"swaydesk-dock"'}
        for field, value in fields.items():
            with self.subTest(field=field):
                self.assert_fails_with(component(page="false", extra=f"{field} = {value}\n"),
                                       f"dock: {field} on a card without a page")

    def test_page_notes_on_a_card_without_a_page_fail(self):
        for field in ("note", "start_note", "start_text", "arch_note", "waybar_note"):
            with self.subTest(field=field):
                langs = [lang("pt-br"), lang("en-us") + f'  {field} = "A note."\n', lang("es")]
                self.assert_fails_with(component(page="false", langs=langs),
                                       f"dock: en-us {field} on a card without a page")

    def test_a_group_without_a_language_text_fails(self):
        group = '[groups.session]\npackage = "swaydesk-session"\n  [groups.session.pt-br]\n  text = "T"\n'
        self.assert_fails_with(component() + group, "groups.session: no en-us text")

    def test_a_group_or_its_language_that_isnt_a_table_fails(self):
        self.assert_fails_with(component() + "[groups]\nbar = 1\n", "groups.bar is not a table")
        self.assert_fails_with(component() + '[groups.bar]\nen-us = "T"\n', "groups.bar: no en-us text")

    def test_a_group_that_isnt_a_section_fails(self):
        group = ('[groups.tray]\npackage = "swaydesk-tray"\n' +
                 "".join(f'  [groups.tray.{c}]\n  text = "T"\n' for c in ("pt-br", "en-us", "es")))
        self.assert_fails_with(component() + group, "groups.tray: unknown group")


if __name__ == "__main__":
    unittest.main()
