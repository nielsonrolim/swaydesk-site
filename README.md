# swaydesk-site

The website of Swaydesk, a complete desktop on top of Sway: <https://swaydesk.org>.

The site is in Brazilian Portuguese (`/pt-br/`) and American English (`/en-us/`). It is built with [Hugo](https://gohugo.io/), with its own templates and no theme, and published on GitHub Pages. It makes no requests to other sites: no web fonts from a CDN, no analytics, no cookies.

## Building

With Hugo 0.147 or later:

```sh
hugo server          # preview at http://localhost:1313
hugo build           # the site in public/
```

Or without installing Hugo:

```sh
docker run --rm -u "$(id -u):$(id -g)" -v "$PWD:/src" -w /src ghcr.io/gohugoio/hugo:v0.147.0 build
```

## Layout

- `content/pt-BR/`, `content/en-US/`: the pages, one Markdown file per page in each language, with the same file names.
- `layouts/`: the templates. `assets/css/site.css`: the styles. `i18n/`: the interface strings.
- `static/`: fonts, scripts, images and the `CNAME` file.

## License

The text and the images are under the [Creative Commons Attribution 4.0](LICENSE) license (CC BY 4.0). The screenshots show third-party icons and app logos, which keep their own licenses. The Fira Code font in `static/fonts/` is under the [SIL Open Font License 1.1](static/fonts/OFL.txt).
