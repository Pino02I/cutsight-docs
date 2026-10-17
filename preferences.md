# Preferences

**Edit ▸ Preferences ▸ Add-ons ▸ cutSIGHT**

```{figure} _static/preferences.png
:alt: The cutSIGHT preferences panel in Blender

Everything the add-on exposes, on one panel: behaviour, overlay colours, the
shortcut, and the in-place list of controls.
```

## Behaviour

**Snap Increment** — the starting value for `Ctrl` snapping, from 1% to 50%.
Default 10%. Changeable while the tool runs with `Ctrl` + Wheel.

**Distribution** — whether a cut starts out Proportional, Parallel A or
Parallel B. Default Proportional. Cycled with `E`.

**Max Cuts** — upper limit for the wheel. Default 10.

**Propagation On by Default** — whether the cut starts covering the whole edge
ring or a single edge. Default on, since the tool takes the place of Loop Cut and
that is the behaviour muscle memory expects. `Shift` + Wheel changes it while the
tool runs.

**Select Result** — select the new vertices and make the last one active, so you
can move them straight away. Default on.

**Show Cursor Readout** — the text next to the cursor. Default on.

**Show Distance** — the measured distance under that text, in scene units.
Default on. Turning it off keeps the status line and drops the number.

## Appearance

| Setting | Default | What it colours |
|---|---|---|
| Target | amber | the edge or ring being aimed at |
| New Geometry | green | the cuts that will be created |
| New Vertices | green | the new vertex positions |
| Centre Marks | light grey | the midpoint guide, when the cut passes through it |
| Readout | white | the text beside the cursor |
| Distance | pale blue | the measured distance under it |
| Line Width | 2.5 | overlay lines |
| Point Size | 6.0 | overlay points |

## Keymap

The shortcut is editable in place, in the **Keymap** box. It defaults to `Ctrl+R`
in the Mesh keymap, which shadows Loop Cut.

Because cutSIGHT's entry lives in the add-on keyconfig rather than replacing
Blender's, rebinding it to something else brings Loop Cut straight back — there
is nothing to restore.
