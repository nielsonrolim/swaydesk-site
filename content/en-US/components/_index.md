---
title: Components
prompt: "ls /usr/bin/swaydesk-*"
crumb: components
aliases: ["apps/"]
description: Swaydesk's pieces, one by one.
---
Swaydesk is made of components of its own, nearly all written in Rust with GTK 4. Each one has its shortcut and a part in the [guide](/en-us/guide/).

The shortcuts on this page are those of the **Swaydesk** profile, the default. The other profiles (i3, Hyprland, niri and dwm) change many of them: see them all in [Shortcuts](/en-us/shortcuts/).

Nearly every component can be turned off. The last line of each one shows the key, which goes in `~/.config/swaydesk/config.toml`; see [Turning components off](/en-us/guide/config/#turning-components-off).

{{< components >}}

## Apps that come along

| App | What for |
| --- | --- |
| kitty | Terminal (`Ctrl`+`Alt`+`T`) |
| Thunar | File manager (`Ctrl`+`Alt`+`E`) |
| rofi | The launcher (`Alt`+`Space`) |
| qalc | Math and unit conversions in the app grid search |
| Blueman | Bluetooth pairing (PIN and confirmation requests) |
| pavucontrol | Fine-grained audio settings, beyond the bar popup (middle-click the volume) |
| gammastep | The night light |
| mate-polkit | The administrator password window (on Debian and Ubuntu, lxpolkit works too) |
| gnome-text-editor | The Help's **Open** button, which edits `50-local.conf`; without it, the Help opens an editor in the terminal. Recommended on Debian and Ubuntu; optional on Arch |
| grim, slurp and wf-recorder | Screenshots and screen recording |
| gtklock | The last-resort lock screen, if Swaydesk's own can't start |

The install images also bring an app store, GNOME Software, with Flathub. On Debian it also installs and updates the distro's packages and the firmware; on Arch it handles Flatpak apps, and the Swaydesk notice handles the rest. With the packages, install `gnome-software` yourself if you want it.
