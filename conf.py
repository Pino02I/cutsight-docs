# Configuration file for the Sphinx documentation builder.
# cutSIGHT 1.0.0 — Pino Iulio

project = "cutSIGHT"
author = "Pino Iulio"
copyright = "2026, Pino Iulio"
release = "1.0.0"
version = "1.0.0"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

# Only extensions that ship with myst-parser itself: adding one that needs a
# separate package (linkify needs linkify-it-py) breaks the Read the Docs
# build at configuration load unless that package is in requirements.txt.
myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

templates_path = ["_templates"]
exclude_patterns = ["_build", "build", "README.md", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = "cutSIGHT 1.0.0"
html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
}
