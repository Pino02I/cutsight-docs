# cutSIGHT documentation

Sphinx sources for the cutSIGHT 1.0.0 documentation, ready for Read the Docs.

The sources sit in the repository **root**: `conf.py`, the `.md` pages and
`_static/` are all here, and `.readthedocs.yaml` points `sphinx.configuration`
at `conf.py`. Keep that layout, or change the `configuration` line if you move
the sources into a subfolder — the two have to agree, or the build fails
immediately after "Running Sphinx".

## Publish on Read the Docs

1. Push this folder to a Git repository (GitHub, GitLab or Bitbucket).
2. Sign in at readthedocs.org and choose **Import a Project**.
3. Pick the repository. `.readthedocs.yaml` is detected automatically, so there
   is nothing to configure in the web interface.
4. Every push rebuilds the site. HTML, PDF and a downloadable zip are produced.

## Build locally

```bash
pip install -r requirements.txt
sphinx-build -b html . _build/html
```

Open `_build/html/index.html`.

## A note on MyST extensions

`myst_enable_extensions` must only list extensions whose packages are installed.
`linkify` is the usual trap: it needs `linkify-it-py`, which is not a dependency
of `myst-parser`. None of these pages rely on it — there are no bare URLs in the
text — so it is left out rather than adding the package.

---

cutSIGHT 1.0.0 · by Pino Iulio · GPL-3.0-or-later
