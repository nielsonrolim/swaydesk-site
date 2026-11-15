#!/usr/bin/env python3
"""Checks the site's internal links: every href and src starting with "/" in the built HTML must point
to a file in the output folder (a folder counts if it has an index.html). Usage: check-links.py public"""
import html.parser
import pathlib
import sys
import urllib.parse


class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ("href", "src") and value and value.startswith("/") and not value.startswith("//"):
                self.found.append(value)


def exists(root, link):
    path = urllib.parse.unquote(urllib.parse.urlsplit(link).path)
    target = (root / path.lstrip("/")).resolve()
    if root not in target.parents and target != root:
        return False
    return target.is_file() or (target / "index.html").is_file()


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()
    broken = []
    for page in sorted(root.rglob("*.html")):
        parser = Links()
        parser.feed(page.read_text(encoding="utf-8"))
        broken += [f"{page.relative_to(root)}: {link}" for link in parser.found if not exists(root, link)]
    for line in broken:
        print(f"broken link: {line}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
