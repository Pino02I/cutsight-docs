# Modes

cutSIGHT starts in one of two modes, decided by what is selected at the moment
you press the shortcut. The mode never changes while the tool is running: the
header always tells you which one you are in, and if it is the wrong one, press
`Esc`, fix the selection and run it again.

| Selection when you start | Mode | Header reads |
|---|---|---|
| Nothing | Hover | `cutSIGHT:` |
| Edges | Selected edges | `cutSIGHT [selected edges]:` |

```{figure} _static/header-selection.png
:alt: The header in selected-edges mode

In selected-edges mode the header drops reach and direction: the selection
decides the extent.
```

## Hover

The default. Nothing is selected, so the tool follows the cursor and cuts the
edge ring running through whatever is under it.

There is no distance threshold on picking: the nearest edge of the surface under
the cursor always wins, so hovering the middle of a face still targets a ring,
the way Loop Cut does. Candidate edges come from the face the ray actually hits
plus its neighbours, and edges that turn out to be hidden behind the surface are
discarded. It also works across every mesh in multi-object edit mode; the
nearest hit wins.

## Selected edges

Every selected edge gets a cut and the mouse slides them all together, from one
end of the ring to the other.

```{figure} _static/selection.png
:alt: A cut running on three selected edges

With edges already selected the cut runs on those, and the readout says
`Selection`.
```

The selection is first grouped into ordered chains by walking the ring *inside*
the selection, which keeps a consistent reference rail. Separate chains — two
parallel loops, or lone edges — are then compared against the first one and
flipped if they point the other way. Without that step the cuts would zig-zag,
because a factor measured from each edge's own first vertex means nothing when
the edges are not oriented the same way.

Faces are never read: selecting faces and running the tool simply treats their
edges as unselected, so it falls back to hovering.
