# Quick start

## Cut one loop

1. Enter Edit Mode on a mesh.
2. Press `Ctrl+R`.
3. Move the mouse over an edge. The whole edge ring lights up with a green
   preview showing where the cut will land.
4. Click. **The cut is now real geometry on the mesh.**
5. Move the mouse. The loop slides live, with shading, so you can see the result
   before committing.
6. Click again to finish, or press `Esc` to put the mesh back as it was.

```{figure} _static/header-hover.png
:alt: The cutSIGHT header in the viewport

While the tool runs, the viewport header lists everything it accepts.
```

That two-step rhythm is deliberate and matches Loop Cut: the first click decides
*where*, the second decides *exactly how far*. Sliding never rebuilds topology,
so it stays smooth on any mesh size.

## Cut part of a ring, or just one edge

Hold `Shift` and roll the wheel. The reach shrinks one edge at a time on each
side, so you can stop it three edges out instead of running around the whole
model — and keep going to land on the single edge under the cursor, where the
cut is one vertex. Press `D` to grow the reach on one side only.

```{figure} _static/reach-short.png
:alt: The reach shortened to seven edges

`Shift` and the wheel walk the reach down one edge at a time. The readout counts
them, so the reach is a number rather than a feeling.
```

## Add several cuts at once

Roll the wheel without any modifier. Two or more cuts are spread evenly along
the edge and slide as a rigid group: the mouse moves them together and the
spacing between them never changes.

## Change your mind afterwards

Press `F9`, or open the panel in the bottom left. Cuts, position, reach,
direction and distribution are all still editable. See
[Adjusting after the cut](redo.md).

## Work on a selection

Select some edges *before* pressing `Ctrl+R` and the tool cuts all of them and
slides them together. See [Modes](modes.md).
