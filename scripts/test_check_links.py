#!/usr/bin/env python3
"""Tests of check-links.py. Run: python3 -I -m unittest discover -s scripts -p 'test_*.py'"""
import pathlib
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent / "check-links.py"


def run(root):
    return subprocess.run([sys.executable, "-I", str(SCRIPT), str(root)], capture_output=True, text=True)


def page(root, path, body):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f"<!doctype html><html><body>{body}</body></html>", encoding="utf-8")


class CheckLinksTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_a_missing_folder_fails(self):
        result = run(self.root / "public")
        self.assertEqual(result.returncode, 1)
        self.assertIn("no HTML pages", result.stdout)

    def test_an_empty_folder_fails(self):
        (self.root / "public").mkdir()
        self.assertEqual(run(self.root / "public").returncode, 1)

    def test_a_folder_without_html_fails(self):
        (self.root / "public").mkdir()
        (self.root / "public" / "CNAME").write_text("example.com")
        self.assertEqual(run(self.root / "public").returncode, 1)

    def test_good_links_pass(self):
        page(self.root, "pt-br/index.html", '<a href="/pt-br/guide/#x">guia</a>')
        page(self.root, "pt-br/guide/index.html", '<h2 id="x">x</h2>')
        result = run(self.root)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(result.stdout, "")

    def test_a_broken_link_fails(self):
        page(self.root, "pt-br/index.html", '<a href="/pt-br/nowhere/">x</a>')
        result = run(self.root)
        self.assertEqual(result.returncode, 1)
        self.assertIn("broken link: /pt-br/nowhere/", result.stdout)

    def test_a_missing_anchor_fails(self):
        page(self.root, "pt-br/index.html", '<a href="/pt-br/guide/#nope">x</a>')
        page(self.root, "pt-br/guide/index.html", '<h2 id="x">x</h2>')
        self.assertIn("missing anchor: /pt-br/guide/#nope", run(self.root).stdout)

    def test_a_link_to_another_language_fails_unless_it_has_hreflang(self):
        page(self.root, "es/index.html", '<a href="/pt-br/">pt</a>')
        page(self.root, "pt-br/index.html", "")
        self.assertIn("link to another language: /pt-br/", run(self.root).stdout)
        page(self.root, "es/index.html", '<a href="/pt-br/" hreflang="pt-BR">pt</a>')
        self.assertEqual(run(self.root).returncode, 0)


if __name__ == "__main__":
    unittest.main()
