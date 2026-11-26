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

    def run_on(self, sibling="0", align="stretch", extra="", first="A", html=None, path="en-us/install", body=""):
        page = self.root / path
        page.mkdir(parents=True, exist_ok=True)
        css = CSS % {"sibling": sibling, "align": align, "extra": extra}
        text = html or PAGE % {"css": css, "first": first}
        (page / "index.html").write_text(text.replace("</body>", body + "</body>", 1), encoding="utf-8")
        return subprocess.run([sys.executable, "-I", str(SCRIPT), str(self.root), path],
                              capture_output=True, text=True, timeout=300)

    def row(self, widths, path="en-us/components/dock"):
        # A row of images as the component pages draw it; each width is a thumbnail's CSS width
        figures = "".join(f'<figure class="component__thumb" style="flex:none;margin:0;width:{w}"><a href="#" style="display:block;'
                          f'height:150px"></a><figcaption>c</figcaption></figure>' for w in widths)
        return self.run_on(path=path, body=f'<div class="component__shots" style="display:flex;flex-wrap:wrap;gap:8px">{figures}</div>')

    def test_a_row_of_equal_thumbnails_passes(self):
        result = self.row(["300px", "300px"])
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_thumbnails_of_different_sizes_fail(self):
        result = self.row(["300px", "220px"])
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("en-us/components/dock @1200: the row's thumbnails differ in size (300x150 and 220x150)",
                      result.stdout)

    def test_a_thumbnail_too_small_to_read_fails(self):
        result = self.row(["120px", "120px"])
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("en-us/components/dock @390: a thumbnail is 120px wide (at least 200px)", result.stdout)

    def test_a_page_wider_than_the_window_fails(self):
        result = self.run_on(path="en-us/components/dock", body='<div class="component__shots">'
                        '<figure class="component__thumb" style="width:300px"><a href="#" style="display:block;'
                        'height:150px"></a></figure></div><div style="width:900px;height:4px"></div>')
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("en-us/components/dock @390: the page scrolls sideways", result.stdout)

    def test_a_component_page_expected_to_have_a_row_without_one_fails(self):
        result = self.run_on(path="en-us/components/greeter")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("en-us/components/greeter @1200: no row of images (component__shots)", result.stdout)

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
