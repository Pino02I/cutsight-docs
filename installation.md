# Installation

cutSIGHT is a Blender Extension and installs like any other.

## Install

1. Download `cutsight_v1_0_0.zip`. Do not unpack it.
2. In Blender, open **Edit ▸ Preferences ▸ Add-ons**.
3. Use the drop-down at the top right and choose **Install from Disk**.
4. Pick the zip file.

The add-on enables itself and registers `Ctrl+R` in Edit Mode straight away.
You can also drag the zip file onto the Blender window, which does the same
thing.

## Requirements

Blender **4.2** or newer. That is the first version with the Extensions system
the add-on is built on.

:::{note}
Version 1.0.0 was developed and tested on Blender 5.2. Earlier 4.x releases are
expected to work but have not been verified.
:::

## What it changes

The add-on claims `Ctrl+R` in the **Mesh** keymap. Its entry sits in the add-on
keyconfig, which Blender reads before its own, so `mesh.loopcut_slide` is
shadowed rather than removed. Rebind cutSIGHT to a different key and Loop Cut
comes back on its own — see [Preferences](preferences.md#keymap).

## Uninstall

Disable or remove the add-on from the same Add-ons list. The shortcut is
released and Loop Cut returns immediately.
