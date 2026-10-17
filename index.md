# cutSIGHT

**Take aim with the cursor and cut exactly where you point.**

cutSIGHT cuts the edge ring running under your mouse. There is nothing to select
first and no dialog to fill in: press the shortcut, the preview follows the
cursor, confirm when it looks right.

```{figure} _static/hero-overview.png
:alt: cutSIGHT running in the Blender viewport

The ring under the cursor, the cut as real geometry, and a live readout of where
it actually sits.
```

It replaces Blender's Loop Cut on `Ctrl+R` and does the same job with more
control — a reach you can dose one edge at a time down to a single vertex, a
direction you can choose, snapping you can tune while the tool is running, and
a live slide on the real mesh before you commit.

```{figure} _static/figure-subdivision.png
:alt: The same mesh before and after placing loops near its edges

Under a Subdivision Surface a loop is not a cut but a control. The same cage,
before and after a few loops land close to the edges.
```

```{toctree}
:maxdepth: 2
:caption: Getting started

installation
quickstart
```

```{toctree}
:maxdepth: 2
:caption: Using cutSIGHT

modes
edges
snapping
redo
```

```{toctree}
:maxdepth: 2
:caption: Reference

controls
preferences
limitations
faq
troubleshooting
changelog
```

## At a glance

| | |
|---|---|
| Blender | 4.2 or newer |
| Default shortcut | `Ctrl+R` in Edit Mode (shadows Loop Cut) |
| Works on | Edges, edge rings, and existing edge selections |
| Multi-object edit | Yes |
| Author | Pino Iulio |
| License | GPL-3.0-or-later |
