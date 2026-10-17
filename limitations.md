# Limitations

Known behaviour worth understanding before it surprises you.

## Edge attributes are not carried over

Crease, seam, sharp and bevel weight are **not** propagated to the edges created
by a cut. On hard-surface work with Subdivision Surface this is visible
immediately, so check those attributes after cutting through creased geometry.

## A single cut on an edge produces an n-gon

Cutting one edge without propagation uses an edge split, which leaves the
adjacent quad as a five-sided face. That is the intended behaviour — you asked for
a vertex on an edge, not for the neighbours to be retopologised.

With propagation on, the ring is subdivided instead and the topology stays clean.

## Propagation sides are not screen-relative

Which branch `D` calls the first side follows the internal ordering of the edge's
linked faces, so it can appear to swap as you move between edges. The preview
always shows the truth; press `D` until it matches what you want.

## Position 0 or 1 in the redo panel

Those values ask for a cut exactly on an existing vertex, which would make a
zero-length edge. Every factor is clamped just inside the edge instead, so the
mesh stays valid, but the cut lands a hair's breadth from the end rather than
where the number says. The modal never produces those values; only typing them
into the panel does.

## The redo panel depends on the edge index

Adjust Last Operation replays the cut by looking the aimed edge up by its index
in the rolled-back mesh. That holds for an ordinary redo, but editing the mesh in
other ways and then reaching back for the panel can land on a different edge.

## Version coverage

1.0.0 was developed and tested on Blender 5.2. The manifest declares 4.2 as the
minimum because that is the first release with the Extensions system, but 4.x has
not been verified.
