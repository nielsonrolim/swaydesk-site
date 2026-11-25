#!/usr/bin/env python3
"""Tests of check-layout.py. Run: python3 -I -m unittest discover -s scripts -p 'test_*.py'

They drive a headless Chrome. Without one they're skipped locally, but on CI (CI set) a missing Chrome fails.
"""
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parent / "check-layout.py"
REPO = SCRIPT.parent.parent
CHROME = shutil.which("google-chrome-stable") or shutil.which("google-chrome") or shutil.which("chromium")

CSS = """
body { margin: 0; font: 16px/1.5 monospace; }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
.tabs { display: flex; }
.distro { padding-top: 4px; }
.distro + .distro { margin-top: %(sibling)s; }
.cmd { display: flex; align-items: %(align)s; gap: 6px; }
.cmd pre { flex: 1; margin: 0; padding: 12px; }
.cmd__copy { padding: 4px; }
%(extra)s
"""

PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>%(css)s</style></head><body>
<div class="distros" data-tabs data-label="Distro">
<section class="distro" id="a"><h3 class="distro__title">%(first)s</h3>
<div class="cmd" data-copy="Copy"><pre><code>sudo apt install x</code></pre></div></section>
<section class="distro" id="b"><h3 class="distro__title">B</h3>
<div class="cmd" data-copy="Copy"><pre><code>sudo apt install x</code></pre></div></section>
</div>
<script src="/js/install.js"></script>
</body></html>"""


@unittest.skipUnless(CHROME or os.environ.get("CI"), "no headless Chrome here")
class CheckLayoutTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tmp.name)
        (self.root / "js").mkdir()
        shutil.copy(REPO / "static/js/install.js", self.root / "js/install.js")

    def tearDown(self):
        self.tmp.cleanup()

    def run_on(self, sibling="0", align="stretch", extra="", first="A", html=None):
        page = self.root / "en-us/install"
        page.mkdir(parents=True, exist_ok=True)
        css = CSS % {"sibling": sibling, "align": align, "extra": extra}
        (page / "index.html").write_text(html or PAGE % {"css": css, "first": first}, encoding="utf-8")
        return subprocess.run([sys.executable, "-I", str(SCRIPT), str(self.root), "en-us/install"],
                              capture_output=True, text=True, timeout=300)

    def test_equal_gaps_and_full_height_buttons_pass(self):
        result = self.run_on()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_a_tab_that_opens_lower_fails(self):
        result = self.run_on(sibling="40px")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("en-us/install @1200: tab B opens", result.stdout)

    def test_a_copy_button_shorter_than_its_field_fails(self):
        result = self.run_on(align="flex-start")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("en-us/install @390: a copy button is", result.stdout)

    def test_a_short_button_in_a_hidden_panel_fails(self):
        # Only the first panel's button is short; after the last click that panel is hidden
        result = self.run_on(extra="#a .cmd { align-items: flex-start; }")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("en-us/install @1200: a copy button is", result.stdout)

    def test_a_page_where_nothing_is_measured_fails(self):
        # Renamed classes: no tabs and no copy blocks found, which must not pass as "no problems"
        html = "<!doctype html><html><body><div class='box'><pre>sudo apt install x</pre></div></body></html>"
        result = self.run_on(html=html)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("en-us/install @1200: measured 0 tabs and 0 copy blocks", result.stdout)

    def test_a_tab_name_with_angle_brackets_is_reported(self):
        result = self.run_on(sibling="40px", first="A &lt;x&gt; &amp; y")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("A <x> & y", result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_a_missing_page_fails_with_a_message(self):
        result = subprocess.run([sys.executable, "-I", str(SCRIPT), str(self.root), "nothing/here"],
                                capture_output=True, text=True, timeout=120)
        self.assertEqual(result.returncode, 1)
        self.assertIn("nothing/here", result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
