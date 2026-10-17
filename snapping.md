# Snapping

Hold `Ctrl` and the cut snaps to multiples of an increment along the edge. The
readout shows the active value, for example `snap 10%`.

## Changing the increment

While `Ctrl` is held, the wheel walks a ladder of increments:

`1% → 2% → 5% → 10% → 12.5% → 20% → 25% → 50%`

The wheel changes the increment rather than the cut count here on purpose: the
number you are looking at is the one that should respond.

The starting value is set in [Preferences](preferences.md#behaviour) and defaults
to 10%.

```{figure} _static/snap-increment.png
:alt: The snap increment changed with Ctrl and the wheel

`Ctrl` with the wheel walks the ladder of increments; the readout shows the
active one in brackets.
```

## The two ends

Snapping never reaches 0% or 100%. It always stays at least one increment away
from both endpoints, because a cut landing on an existing vertex would create
degenerate geometry.

## Pinning the midpoint

At the top of the ladder, 50%, the cut is pinned to the exact middle of the edge
whatever the mouse does. It is the most-used position, and this way you hit it
without aiming.

## Finding the centre

Snapping tells you the step, not where the middle is. While a cut position is
being read, the overlay draws a dimmed **centre loop** running through the
midpoint of every edge involved. It stays put while the cut moves, so the middle
becomes something to aim at rather than a number to watch.

When you are there, the readout says so: `50% proportional  (centred)`.

```{figure} _static/snap-centred.png
:alt: The cut sitting exactly on the midpoint

The dimmed centre loop marks the midpoint of every edge involved, and the
readout confirms it.
```

One loop is drawn whatever the cut count, since it marks the middle of the edges
themselves — the reference the whole group travels away from.

The colour is configurable as **Centre Marks** in the preferences.

## Reading the position

The readout under the cursor combines the reach, the cut count, the position and
the distribution. These are the real strings, as they appear in the viewport:

| Reading | Meaning |
|---|---|
| `1 edge  34% proportional` | a single edge, 34% along it |
| `full ring, 8 edges  25% proportional` | the whole ring, eight edges, 25% of the one you pointed at |
| `5 edges <-  49% proportional` | five edges, growing to one side only |
| `full ring, 8 edges  x4  70% proportional` | four parallel cuts |
| `full ring, 8 edges  50% proportional  (centred)` | sitting exactly on the midpoint |
| `full ring, 8 edges  60% proportional  [snap 10%]` | snapping active, 10% steps |
| `offset 125  full ring, 8 edges  12% proportional` | an offset typed in, with the distance below |
| `Slide  40% parallel` | sliding a cut that has already been applied |
| `Selection  39% proportional  3 edges` | running on an existing edge selection |

A second line underneath gives the distance in the scene's own units, and a
single letter in the viewport — **A**, **B** or **M** — marks what that distance
is measured from.
