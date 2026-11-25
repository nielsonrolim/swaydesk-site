#!/usr/bin/env python3
"""Checks the built site's layout in a headless Chrome. Usage: check-layout.py <public dir> [page ...]

The site's CSS can look right in one state and not another: the Install and component pages show their
per-distro sections as tabs (static/js/install.js), and every hidden panel is still in the DOM. This opens each
page at 1200 and 390 px and checks that:
- every tab panel's first block starts at the same distance from the tabs as the first panel's;
- every copy button is as tall as the code field next to it.
Without pages, it checks Install and three component pages (a plain install, start_text, a multi-line start) in
the three languages. The pages are served from a copy of <public dir> on 127.0.0.1; Chrome runs with a temporary
HOME and no display or session bus. A missing page, a missing Chrome or a page that doesn't report is an error.
"""
import functools
import http.server
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import threading

WIDTHS = (1200, 390)
PAGES = [f"{lang}/{page}" for lang in ("pt-br", "en-us", "es")
         for page in ("install", "components/dock", "components/greeter", "components/screenshot")]
TOLERANCE = 1  # px: rounding of fractional layout

MEASURE = r"""window.addEventListener("load", () => {
  const out = {tabs: [], cmds: []};
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
    });
  });
  document.querySelectorAll(".cmd").forEach((cmd) => {
    const pre = cmd.querySelector("pre"), btn = cmd.querySelector(".cmd__copy");
    if (!pre || !btn || !cmd.offsetParent) return;
    out.cmds.push({pre: Math.round(pre.getBoundingClientRect().height), btn: Math.round(btn.getBoundingClientRect().height)});
  });
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
    if tabs:
        first = tabs[0]["gap"]
        for tab in tabs[1:]:
            if abs(tab["gap"] - first) > TOLERANCE:
                errors.append(f"{page} @{width}: tab {tab['name']} opens {tab['gap']}px below the tabs, "
                              f"{tabs[0]['name']} {first}px")
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
                    data = json.loads(match.group(1).replace("&quot;", '"').replace("&amp;", "&"))
                    errors += problems(page, width, data)
        finally:
            server.shutdown()
    for line in errors:
        print(line)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
