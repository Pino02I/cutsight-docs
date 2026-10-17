# Controls

The header of the 3D viewport lists only the keys that do something at that
moment. The table below is the full set.

## Aiming and cutting

| Input | Action |
|---|---|
| Move mouse | Aim at an edge, or position the cut |
| Wheel | Number of cuts |
| Type a number | Exact offset in scene units |
| `Shift` + Wheel | Reach: from the whole ring down to a single edge |
| `D` | Propagation direction: both sides / one side / the other |
| `E` | Distribution: proportional / parallel A / parallel B |
| `Ctrl` (hold) | Snap the cut along the edge |
| `Ctrl` + Wheel | Change the snap increment |
| `LMB`, `RMB`, `Enter` | Confirm |
| `Esc` | Cancel, restoring the mesh |
| `MMB` | Passes through, so you can orbit while the tool is open |

## After cutting

`F9`, or the Adjust Last Operation panel in the bottom left, reopens the
settings. See [Adjusting after the cut](redo.md).

## Not bound

Every other key does nothing. The tool will not commit because you pressed
something unmapped; only `LMB`, `RMB` and `Enter` confirm, and only `Esc`
cancels.
