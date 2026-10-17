# Adjusting after the cut

Every setting the modal chose is stored on the operator, so Blender's **Adjust
Last Operation** panel — bottom left of the viewport, or `F9` — reopens them
after the cut is committed.

```{figure} _static/f9-panel.png
:alt: The Adjust Last Operation panel for cutSIGHT

Every decision the modal made is a field again.
```

| Field | What it changes |
|---|---|
| Cuts | How many parallel cuts |
| Fixed Offset | Measure the cut as a distance instead of a share |
| Position | Where they sit along the edge, 0 to 1 |
| Offset | The distance itself, shown in the scene's units |
| Distribution | Proportional, Parallel A, or Parallel B |
| Full Ring | Whether the cut follows the whole ring |
| Reach | Edges per side, when the ring is not followed all the way round |
| Direction | Both sides, or one side only |

Position and Offset swap places depending on Fixed Offset, since only one of
the two decides where the cut goes. Reach and Direction are greyed out while Full Ring is on, since they have
nothing to act on, and the whole group is hidden when the tool ran on a
selection — there the selection decides the extent, not a reach.

Changing a value re-runs the cut from scratch on the rolled-back mesh, so the
result is exactly what you would have got by aiming that way in the first place.
The edge you aimed at is remembered by index, which is why the panel keeps
working as long as you do not undo past the cut itself.

:::{note}
The panel appears after a cut, not during the modal. While the tool is running
the viewport header is the live readout.
:::
