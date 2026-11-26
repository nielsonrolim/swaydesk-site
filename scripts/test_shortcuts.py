#!/usr/bin/env python3
"""Tests of shortcuts.py, the Atalhos page's generator. Run: python3 -I -m unittest discover -s scripts -p 'test_*.py'"""
import importlib.util
import pathlib
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent / "shortcuts.py"
spec = importlib.util.spec_from_file_location("shortcuts", SCRIPT)
shortcuts = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shortcuts)

BASE = """### Session and apps
## Show this help
bindsym $mod+F1 exec help
## Open the terminal
bindsym Ctrl+Alt+t exec $term
"""
PROFILE = """### Session and apps
## Show this help
bindsym $mod+slash exec help
## Lock the screen
bindsym $mod+l exec lock
### Mouse and touchpad
## Show this help
bindsym $mod+question exec help
"""


def rows(*texts):
    parser = shortcuts.Parser()
    parser.text(shortcuts.PRELUDE)
    for text in texts:
        parser.text(text)
    return {s["title"]: s["rows"] for s in shortcuts.render(parser.finish(), "en")}


class JoinTests(unittest.TestCase):
    def test_the_same_description_in_two_files_is_one_row_with_both_keys(self):
        # Like the Help (#440): keys/base.conf's Super+F1 and the profile's Super+/ under one "Show this help"
        session = rows(BASE, PROFILE)["Session and apps"]
        texts = [r["text"] for r in session]
        self.assertEqual(texts.count("Show this help"), 1, texts)
        row = next(r for r in session if r["text"] == "Show this help")
        self.assertEqual(len(row["chords"]), 2, row)

    def test_the_joined_row_keeps_the_first_ones_place(self):
        texts = [r["text"] for r in rows(BASE, PROFILE)["Session and apps"]]
        self.assertEqual(texts, ["Show this help", "Open the terminal", "Lock the screen"])

    def test_the_same_description_in_another_section_stays_its_own_row(self):
        mouse = rows(BASE, PROFILE)["Mouse and touchpad"]
        self.assertEqual([r["text"] for r in mouse], ["Show this help"])

    def test_binds_without_a_description_are_not_joined(self):
        text = "### Other things\nbindsym $mod+a exec foo\nbindsym $mod+b exec foo\n"
        other = rows(text)["Other things"]
        self.assertEqual(len(other), 2, other)


if __name__ == "__main__":
    unittest.main()
