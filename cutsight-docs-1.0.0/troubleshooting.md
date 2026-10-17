# Troubleshooting

## Loop Cut is gone

That is expected: cutSIGHT claims `Ctrl+R`. Rebind it in
[Preferences ▸ Keymap](preferences.md#keymap) and Loop Cut returns immediately,
with nothing to restore.

## `D` does nothing

`D` sets the direction the reach grows in, so it applies while you are aiming,
not while you are sliding a cut that already exists. The header lists only the
keys that are live at that moment.

`E` is different: it keeps working during the slide, because the distribution
still changes where the cut sits.

## I want a cut on one edge only, not the whole ring

Hold `Shift` and roll the wheel down. The reach shrinks until only the edge
under the cursor is left.

## The cut went to an edge I could not see

Report it. Picking discards edges hidden behind the surface by casting a
verification ray towards each candidate that does not belong to the face the
cursor actually hit, so this should not happen.

## The panel in the bottom left is empty or missing

It appears after the cut is committed, not during the modal. Press `F9` to
reopen it; if another operation ran in between, it belongs to that one instead.

## Nothing happens when I press the shortcut

Check that you are in Edit Mode on a mesh, with the cursor inside the 3D viewport.
If another add-on also claims `Ctrl+R`, the one loaded later wins; rebind one of
them.

## The preview shows but the mesh does not change

That is the first phase. Click once and the cut becomes real geometry you can
then slide. See [Quick start](quickstart.md).
