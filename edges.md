# Cutting edges

## Propagation

Propagation is a single state, not a switch plus a value:

- **full ring** — the cut runs all the way round
- **a number of edges** — it reaches that far on each side of the one you point at
- **1 edge** — only the edge under the cursor, cut at a single vertex

`Shift + Wheel` doses it. Rolling down shrinks the reach one edge at a time;
rolling up grows it, and as soon as it covers the ring it reads `full ring`
again. The readout always names the number of edges actually covered.

One gesture covers the whole range, so there is no separate on/off key: keep
rolling down and the cut ends up on the single edge under the cursor, where it
is just one vertex. It is drawn larger there than it would be as one bead on a
ring, so you can see exactly where it will land.

The ring walk keeps a consistent reference rail, so the cut points stay aligned
across the whole ring instead of zig-zagging. Closed rings are detected and the
preview loop closes on itself.

## Direction

```{figure} _static/figure-direction.png
:alt: The same cut growing both ways, then one way, then the other

`D` cycles the direction. The arrow in the readout says which way the reach is
running.
```

By default propagation grows on both sides. `D` cycles it:

| Reading | Meaning |
|---|---|
| `<->` | both sides |
| `->` | one side only |
| `<-` | the other side only |

With one side selected the span counts all the way to the end of that branch
rather than stopping at half the ring.

:::{note}
Which branch is which follows the internal ordering of the edge's faces, so the
side can appear to flip as you move from one edge to another. Press `D` until the
preview shows the side you want.
:::

## Number of cuts

The wheel, with no modifier, sets how many cuts. One cut lands wherever you
point. Two or more are spread evenly and move together as a rigid group: the
cursor drags the whole group along the edge and the spacing between the cuts
never changes. The travel is limited to one spacing either way, which is exactly
what keeps the outer cuts on the edge; at the middle of that range the cuts sit
evenly along the edge.

Like a single cut, a group is applied on the first click and can then be slid on
the real mesh before committing.

Each cut draws its own polyline in the preview, so three cuts read as three
distinct loops.

## Exact offsets

Start typing a number at any point during the tool and the cut leaves the
cursor: it goes to that distance from the side loop and stays there while you
carry on adjusting everything else. The text is read with the scene's own
units, so `3mm`, `0.25`, `2 cm` and `1'` all work, and with units switched off
it is a plain number.

```{figure} _static/offset-typed.png
:alt: An offset typed while the tool is running

Start typing and the cut leaves the cursor for the distance you asked for.
```

Where the distance starts from is the distribution's own zero:

| Distribution | Zero | A typed `0` means |
|---|---|---|
| Proportional | the middle of the edge, signed | dead centre |
| Parallel A | the first side loop | on that loop |
| Parallel B | the opposite side loop | on that loop |

Proportional has no side of its own, so measuring it from one would be an
arbitrary choice of which end counts as the start. It is measured from the
middle instead, and the value carries a sign: `-12 mm` is twelve millimetres
one way, `+12 mm` the other.

The same number is shown live under the cursor as you move, so the readout
doubles as a measurement of a cut you are placing by hand — whatever it says is
what you would type to put the cut back there.

The distance is measured in **world space**, which means an object with
unapplied scale still gets the offset you asked for rather than one divided by
its scale factor. When an edge is shorter than the distance the cut is clamped
near its end instead of running past it.

Backspace edits what you typed, Esc clears it and hands the cut back to the
mouse, and the readout shows the number as you type with a `?` while it cannot
be parsed. Snapping steps aside while an offset is active: a typed distance is
an exact request and nothing should move it.

## Distribution: proportional and parallel

`E` cycles how a cut spreads over edges of different length. It is the same
distinction Loop Cut draws between its proportional slide and **Even** with
**Flipped**, named here for what it actually produces.

| Mode | Reading | Behaviour |
|---|---|---|
| Proportional | `25% proportional` | the same fraction on every edge |
| Parallel A | `25% parallel` | constant real distance from one side loop |
| Parallel B | `25% parallel` | constant real distance from the other side loop |

The two parallel modes read the same in the viewport; the letter marker tells
them apart — **A** or **B** shows which side loop the distance is taken from.

```{figure} _static/figure-distribution.png
:alt: The same ring cut proportionally and in parallel

The same object, the same cut, a few percent apart. Proportional holds the
share of each edge; Parallel holds a real distance from a side loop — and the
measured length changes from 575.6 mm to 863.6 mm.
```

On a ring whose edges measure 1, 2, 4 and 8 units, a cut at 25% of the edge under
the cursor gives:

| Mode | distance from side A | distance from side B |
|---|---|---|
| Proportional | 0.25 / 0.5 / 1 / 2 | 0.75 / 1.5 / 3 / 6 |
| Parallel A | **0.25 on all** | 0.75 / 1.75 / 3.75 / 7.75 |
| Parallel B | 0.25 / 1.25 / 3.25 / 7.25 | **0.75 on all** |

Proportional makes the new loop follow uneven topology; Parallel holds it
parallel to the side loop you chose. The distance is always taken from the edge
under the cursor, so you aim where the spacing matters and the rest of the ring
follows.

Where an edge is too short to hold the distance, the cut is clamped near its end
instead of running past it.

## Sliding

Cuts on edges are applied for real on the first click, then slide live until you
commit. Each new vertex remembers the two endpoints of the edge it was
born on, so sliding is an interpolation between two points: the cost is
proportional to the number of cuts, not to the size of the mesh. A 500-edge ring
on a million-polygon mesh slides exactly as smoothly as on a cube.

During the slide the topology is already decided, so `D` and the plain wheel
are inert. `Ctrl` and `Ctrl + Wheel` still work, and `E` still switches the
distribution. `Esc` restores the mesh from a copy taken the moment the cut was
applied, so backing out is exact rather than approximate.
