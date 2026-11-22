#!/usr/bin/env python3
"""Checks the site's internal links in the built HTML. Usage: check-links.py public

- Every href and src starting with "/" must point to a file in the output folder (a folder counts if it has an
  index.html).
- An #anchor on a page link ("/es/guide/config/#pantallas", "#los-paquetes") must be an id on that page.
- A page under /<lang>/ links only to its own language: an <a> to another language's pages is an error, except
  the language switcher's links, which carry hreflang.
"""
import html.parser
import pathlib
import sys
import urllib.parse

LANGS = ("pt-br", "en-us", "es")


class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = []  # (tag, link, has hreflang)
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for name in ("href", "src"):
            value = attrs.get(name)
            if value and (value.startswith("/") and not value.startswith("//") or value.startswith("#")):
                self.found.append((tag, value, "hreflang" in attrs))


PAGES = {}


def parse(path):
    if path not in PAGES:
        parser = Links()
        parser.feed(path.read_text(encoding="utf-8"))
        PAGES[path] = parser
    return PAGES[path]


def target_of(root, page, link):
    path = urllib.parse.unquote(urllib.parse.urlsplit(link).path)
    if not path:
        return page
    target = (root / path.lstrip("/")).resolve()
    if root not in target.parents and target != root:
        return None
    if target.is_file():
        return target
    if (target / "index.html").is_file():
        return target / "index.html"
    return None


def problems(root, page):
    lang = page.relative_to(root).parts[0]
    for tag, link, has_hreflang in parse(page).found:
        target = target_of(root, page, link)
        if target is None:
            yield f"broken link: {link}"
            continue
        fragment = urllib.parse.unquote(urllib.parse.urlsplit(link).fragment)
        if fragment and target.suffix == ".html" and fragment not in parse(target).ids:
            yield f"missing anchor: {link}"
        other = link.split("/")[1] if link.startswith("/") else ""
        if lang in LANGS and tag == "a" and not has_hreflang and other in LANGS and other != lang:
            yield f"link to another language: {link}"


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "public").resolve()
    found = []
    for page in sorted(root.rglob("*.html")):
        found += [f"{page.relative_to(root)}: {p}" for p in problems(root, page)]
    for line in found:
        print(line)
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
