# Changelog

## 1.0.0

First release.

- Hover picking of edges, occlusion-aware, with no distance threshold, across
  every mesh in multi-object edit mode
- Live overlay preview, with one polyline per cut and a centre loop marking the
  middle
- Two-phase cutting: the first click applies, then it slides live on the real
  mesh until confirmed
- Reach adjustable one edge at a time, from the whole ring down to a single
  edge, with a choice of direction
- Proportional, Even and Even-flipped distribution
- Snapping with an increment ladder from 1% to 50%, adjustable while running
- Several cuts travelling together as a rigid group
- Selection mode for an existing edge selection
- Every setting editable afterwards in Adjust Last Operation (F9)
- Contextual header listing only the keys that are live
