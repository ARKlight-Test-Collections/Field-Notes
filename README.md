# field-notes

An ARKlight site, scaffolded with `arklight new field-notes --template production`.

## Layout

```
site.py               routes -- @site.page(...) decorators live here
components/
  nav.py                 a registered @component (checked "active" prop)
  footer.py              a plain function -- both work, mix freely
pages/                 one module per route, returns Page(...)
content/               copy/text constants, kept out of the markup
assets/                icon, images, fonts -- copied into the build
tests/                 build smoke tests (pytest)
arklight.config.py     optional project settings, all commented out
```

Run `arklight new --explain-architecture` for the reasoning behind
this shape and how to extend it.

## Build it

```
arklight build site.py -o ARK
```

This writes `ARK/index.html`, `ARK/about.html`, `ARK/styles.css`, and
`ARK/arklight.js`, then opens `ARK/index.html` in your default browser
(pass `--no-open` to skip that). Anything in `assets/` is copied into
`ARK/assets/` automatically -- no manual copy step.

While editing, `arklight live-streaming --subscribe site.py` rebuilds
and reloads on every save.

## Test it

```
pip install pytest
pytest
```

`tests/test_site.py` builds the real site, so a broken import, a
misspelled component, or a missing required prop fails there.

## Adding a page

1. Add `pages/<name>.py` with a function that returns `Page(...)`
   (copy `pages/about.py` as a starting point).
2. In `site.py`, import it and add a decorated wrapper:

   ```python
   from pages.<name> import <name>

   @site.page("/<route>")
   def <name>_page():
       return <name>()
   ```
3. Add the route to `ROUTES` in `tests/test_site.py`.

The decorator has to live in `site.py` itself -- ARKlight discovers
routes by statically scanning the entry file's own source, not any
file it imports.

## Make it installable (PWA)

```
arklight build site.py -o ARK
arklight pwa ARK --name "field-notes" --icon assets/icon.svg:any
```

Re-run `arklight pwa` after every `arklight build`.
