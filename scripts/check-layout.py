#!/usr/bin/env python3
"""Checks the built site's layout in a headless Chrome. Usage: check-layout.py <public dir> [page ...]

The site's CSS can look right in one state and not another: the Install and component pages show their
per-distro sections as tabs (static/js/install.js), and every hidden panel is still in the DOM. This opens each
page at 1200, 390, 1440 and 1920 px and checks that:
- every tab panel's first block starts at the same distance from the tabs as the first panel's;
- every copy button, in every tab panel, is as tall as the code field next to it;
- each page with distro tabs (Install, the component pages) reports at least two tabs and one copy block (none
  means the check measured nothing);
- a component page's row of images (component__shots) and the screenshots' gallery have thumbnails of one size,
  each at least 200px wide,
  and the Dock and login pages, which have more_shots, have one;
- no page scrolls sideways;
- at 1440 and 1920, the content box (main .content) is as wide as the header's container, its edges within 2% of
  the container's, and every card grid (.cgrid) and gallery (.gallery) has at least 3 columns.
Without pages, it checks Install, three component pages (a plain install, start_text, a multi-line start), the
screenshots, the components list, the shortcuts and a guide page in the three languages. The pages are served from a copy of <public dir> on 127.0.0.1; Chrome runs with a temporary
HOME and no display or session bus. A missing page, a missing Chrome or a page that doesn't report is an error.
"""
import functools
import html
import http.server
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import threading

WIDE = (1440, 1920)  # wide screens: the content as wide as the header's container, card grids of 3+ columns
WIDTHS = (1200, 390) + WIDE
PAGES = [f"{lang}/{page}" for lang in ("pt-br", "en-us", "es")
         for page in ("install", "components/dock", "components/greeter", "components/screenshot",
                      "screenshots", "components", "shortcuts", "guide/config")]
# The pages with distro tabs and copy blocks: Install and each component page
TABBED = re.compile(r"(^|/)(install|components/[^/]+)$")
EDGE = 0.02  # the content's edges within 2% of the header container's width from its edges
MIN_COLUMNS = 3
TOLERANCE = 1  # px: rounding of fractional layout
MIN_THUMB = 200  # px: narrower than this, a thumbnail's content can't be read
# Pages that have more_shots, so a row of images: none found means the template or a class changed
EXPECT_ROWS = ("components/dock", "components/greeter")

MEASURE = r"""window.addEventListener("load", () => {
  const out = {tabs: [], cmds: []};
  // Every copy block that is visible now; each panel is measured right after its tab is clicked, since a
  // hidden panel's blocks have no size, and the blocks outside any tab box once at the end
  const seen = new Set();
  const cmds = (root) => root.querySelectorAll(".cmd").forEach((cmd) => {
    const pre = cmd.querySelector("pre"), btn = cmd.querySelector(".cmd__copy");
    if (seen.has(cmd) || !pre || !btn || !cmd.offsetParent) return;
    seen.add(cmd);
    out.cmds.push({pre: Math.round(pre.getBoundingClientRect().height), btn: Math.round(btn.getBoundingClientRect().height)});
  });
  document.querySelectorAll("[data-tabs]").forEach((box) => {
    const list = box.querySelector(".tabs");
    if (!list) return;
    Array.from(list.querySelectorAll(".tabs__tab")).forEach((tab) => {
      tab.click();
      const panel = document.getElementById(tab.getAttribute("aria-controls"));
      const first = Array.from(panel.children).find((el) => !el.classList.contains("sr-only")
        && getComputedStyle(el).position !== "absolute");
      if (first) out.tabs.push({name: tab.textContent.trim(),
        gap: Math.round(first.getBoundingClientRect().top - list.getBoundingClientRect().bottom)});
      cmds(panel);
    });
  });
  cmds(document);
  // The component pages' rows of images: each thumbnail's box (its link), and whether the page scrolls sideways
  out.rows = Array.from(document.querySelectorAll(".component__shots, .gallery")).map((row) =>
    Array.from(row.querySelectorAll(":scope > figure > a")).map((a) => {
      const r = a.getBoundingClientRect();
      return {w: Math.round(r.width), h: Math.round(r.height)};
    }));
  out.overflow = document.documentElement.scrollWidth - document.documentElement.clientWidth;
  // The header's container (its content box) and the main content box; the columns of each card grid
  const head = document.querySelector(".topbar__in"), content = document.querySelector("main .content");
  if (head && content) {
    const h = head.getBoundingClientRect(), s = getComputedStyle(head), c = content.getBoundingClientRect();
    out.frame = {left: h.left + parseFloat(s.paddingLeft), right: h.right - parseFloat(s.paddingRight),
      cleft: c.left, cright: c.right};
  }
  out.grids = Array.from(document.querySelectorAll(".cgrid, .gallery")).map((grid) => ({
    kind: grid.classList.contains("cgrid") ? "cards" : "gallery",
    columns: new Set(Array.from(grid.children).filter((el) => el.getClientRects().length)
      .map((el) => Math.round(el.getBoundingClientRect().left))).size}));
  const el = document.createElement("pre");
  el.id = "__layout";
  el.textContent = JSON.stringify(out);
  document.body.appendChild(el);
});
"""


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def chrome():
    for name in ("google-chrome-stable", "google-chrome", "chromium", "chromium-browser"):
        if shutil.which(name):
            return name
    return None


def problems(page, width, data):
    errors, tabs = [], data["tabs"]
    if width in WIDE:
        frame = data.get("frame")
        if not frame:
            errors.append(f"{page} @{width}: no header container (.topbar__in) or content box (main .content)")
        else:
            span = frame["right"] - frame["left"]
            inner_left, inner_right = frame["cleft"] - frame["left"], frame["right"] - frame["cright"]
            if abs(inner_left) > EDGE * span or abs(inner_right) > EDGE * span:
                errors.append(f"{page} @{width}: the content isn't as wide as the header's container "
                              f"(its edges {round(inner_left)}px and {round(inner_right)}px inside it)")
        for grid in data.get("grids", []):
            if grid["columns"] < MIN_COLUMNS:
                errors.append(f"{page} @{width}: the {grid['kind']} grid has {grid['columns']} columns "
                              f"(at least {MIN_COLUMNS} at this width)")
    # Every page with distro tabs has tabs and copy blocks: finding none means a renamed class or a script
    # that didn't run, never a page without problems
    if not TABBED.search(page.strip("/")):
        tabs = []
    elif len(tabs) < 2 or not data["cmds"]:
        return errors + [f"{page} @{width}: measured {len(tabs)} tabs and {len(data['cmds'])} copy blocks "
                "(expected 2+ tabs and 1+ copy block)"]
    if tabs:
        first = tabs[0]["gap"]
        for tab in tabs[1:]:
            if abs(tab["gap"] - first) > TOLERANCE:
                errors.append(f"{page} @{width}: tab {tab['name']} opens {tab['gap']}px below the tabs, "
                              f"{tabs[0]['name']} {first}px")
    rows = data.get("rows", [])
    if page.endswith(EXPECT_ROWS) and not any(rows):
        errors.append(f"{page} @{width}: no row of images (component__shots)")
    for row in rows:
        sizes = sorted({(t["w"], t["h"]) for t in row}, reverse=True)
        if any(abs(a - c) > TOLERANCE or abs(b - d) > TOLERANCE for (a, b) in sizes for (c, d) in sizes):
            errors.append(f"{page} @{width}: the row's thumbnails differ in size "
                          f"({sizes[0][0]}x{sizes[0][1]} and {sizes[-1][0]}x{sizes[-1][1]})")
        for w in sorted({t["w"] for t in row if t["w"] < MIN_THUMB}):
            errors.append(f"{page} @{width}: a thumbnail is {w}px wide (at least {MIN_THUMB}px)")
    if data.get("overflow", 0) > TOLERANCE:
        errors.append(f"{page} @{width}: the page scrolls sideways ({data['overflow']}px wider than the window)")
    for cmd in data["cmds"]:
        if abs(cmd["btn"] - cmd["pre"]) > TOLERANCE:
            errors.append(f"{page} @{width}: a copy button is {cmd['btn']}px high, its field {cmd['pre']}px")
    return errors


def main(argv):
    if len(argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    public, pages = pathlib.Path(argv[1]), argv[2:] or PAGES
    browser = chrome()
    if not browser:
        print("error: no headless Chrome (google-chrome-stable or chromium)", file=sys.stderr)
        return 1
    missing = [p for p in pages if not (public / p / "index.html").is_file()]
    if missing:
        for page in missing:
            print(f"error: {page}: no {public / page / 'index.html'}", file=sys.stderr)
        return 1
    errors = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        site = tmp / "site"
        shutil.copytree(public, site)
        # The site's CSP accepts only its own scripts: the measuring script goes in as a file
        (site / "__layout.js").write_text(MEASURE, encoding="utf-8")
        for page in pages:
            f = site / page / "index.html"
            text = f.read_text(encoding="utf-8")
            f.write_text(text.replace("</body>", '<script src="/__layout.js"></script></body>', 1), encoding="utf-8")
        handler = functools.partial(QuietHandler, directory=str(site))
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        for name in ("home", "run"):
            (tmp / name).mkdir(mode=0o700)
        env = {"PATH": "/usr/bin:/bin", "HOME": str(tmp / "home"), "LANG": "C.UTF-8",
               "XDG_RUNTIME_DIR": str(tmp / "run"), "DBUS_SESSION_BUS_ADDRESS": "unix:path=/nonexistent"}
        try:
            for page in pages:
                for width in WIDTHS:
                    command = [browser, "--headless=new", "--no-first-run", "--disable-gpu", "--no-sandbox",
                               f"--user-data-dir={tmp / 'profile'}", f"--window-size={width},2000",
                               "--virtual-time-budget=10000", "--dump-dom",
                               f"http://127.0.0.1:{server.server_address[1]}/{page}/"]
                    dom = subprocess.run(command, capture_output=True, text=True, timeout=120, env=env).stdout
                    match = re.search(r'<pre id="__layout">(.*?)</pre>', dom, re.S)
                    if not match:
                        errors.append(f"{page} @{width}: the page didn't report (no layout data)")
                        continue
                    data = json.loads(html.unescape(match.group(1)))
                    errors += problems(page, width, data)
        finally:
            server.shutdown()
    for line in errors:
        print(line)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
