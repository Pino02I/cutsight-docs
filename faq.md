# FAQ

## Does cutSIGHT replace Loop Cut?

It shadows it. cutSIGHT binds `Ctrl+R` in its own add-on keyconfig rather than
editing Blender's, so Loop Cut is still there, just no longer first in line.
Rebind cutSIGHT in [Preferences ▸ Keymap](preferences.md#keymap) and Loop Cut
answers `Ctrl+R` again immediately — there is nothing to restore and nothing to
reinstall.

## Which Blender versions does it run on?

The manifest declares **4.2** as the minimum, because that is the first release
with the Extensions system. 1.0.0 was developed and tested on **5.2**; the 4.x
line has not been verified. See [Limitations](limitations.md#version-coverage).

## Do I have to select anything first?

No. Point at a face and the nearest edge of that face is the one targeted —
that is the whole idea. But a selection is not ignored: if edges are already
selected when you press `Ctrl+R`, the cut runs on those instead of on the edge
under the cursor, and they all slide together. See [Modes](modes.md).

## Does it work on more than one object at a time?

Yes, across every mesh in multi-object edit mode.

## What units is the distance in?

Your scene's. A bare typed number is read in whatever the scene is set to, and
the distance is measured in **world space** — so an object with unapplied scale
still gets the offset you asked for rather than a scaled version of it. See
[Working along the edge](edges.md).

## Why can't the reach grow into a full ring on this mesh?

A ring is a chain of quads. The walk stops as soon as the next face is not one —
at an n-gon cap, at a triangle, or at a boundary. On a mesh like that the ring
is open, and the reach grows outwards from the edge you are pointing at until it
runs out of quads. That is also why `D` matters there and not on a closed ring:
with two ends, the direction the cut grows in is a real choice.

## Does it work under a Subdivision Surface?

It operates on the cage, like every mesh tool. The overlay and the distance in
the readout therefore describe the **cage**, not the smoothed surface you see:
with subdivision on, the green loop and the orange rails can sit visibly away
from the rendered shape. That is correct behaviour, but it makes the readout
harder to relate to what is on screen, so turn subdivision off while you are
placing a cut by the numbers — and leave it on when you are placing a loop by
eye to tighten an edge, which is what loops under subdivision are for.

## Why did cutting one edge leave a five-sided face?

Because that is what you asked for. A single cut with propagation off uses an
edge split, which puts a vertex on the edge and leaves the neighbouring quad
with five sides. With propagation on the ring is subdivided instead and the
topology stays clean. See [Limitations](limitations.md).

## Are crease, seam, sharp and bevel weight carried over?

No. New edges are created without them. On hard-surface work under a
Subdivision Surface this shows up straight away, so check those attributes after
cutting through creased geometry.

## Is it slow on a heavy mesh?

Sliding never rebuilds the topology — the cut becomes real geometry once, at the
first click, and from then on you are moving vertices that already exist. The
expensive part happens once, not on every mouse move.

## I changed my mind after confirming. Is the cut final?

No. Press `F9` and every decision is a field again: cut count, offset,
distribution, reach and direction. The mesh rebuilds live under the panel. See
[Adjusting after the cut](redo.md).

## And during the cut?

`Esc` cancels and puts the mesh back exactly as it was.

## Can I turn the readout off?

Yes — **Show Cursor Readout** and **Show Distance** in
[Preferences ▸ Behaviour](preferences.md#behaviour). The colours, line width and
point size of the overlay are editable there too.

## What licence is it under?

GPL-3.0-or-later, like any Blender add-on.
