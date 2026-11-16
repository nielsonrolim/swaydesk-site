---
title: Shortcuts
prompt: "grep '^## ' keys/*.conf"
crumb: shortcuts
description: Every keyboard shortcut of the Swaydesk session.
---
Swaydesk comes with five shortcut profiles: **Swaydesk** (the default, which follows KDE Plasma with Krohnkite), **i3**, **Hyprland**, **niri** and **dwm**. Each one brings the keys of that window manager to Swaydesk, and every profile has 9 workspaces. The shortcuts that don't use Super with a letter (the session menu, the terminal, screenshots, media keys) are the same in all of them. `Super` is the logo key.

**Choosing a profile:** in the **Help** (`Super`+`F1`), the drop-down at the top, next to the search field, shows the profile in use. Pick another and it applies at once, without logging out; the Help then shows the new shortcuts. Choosing dwm asks first, because its modifier is Alt. From a terminal, set `shortcuts = "i3"` (or `swaydesk`, `hyprland`, `niri`, `dwm`) in `~/.config/sway-desktop/config.toml` and reload Sway with `swaymsg reload`, or with the profile's reload key.

The tables below come from the same files and descriptions the **Help** app (`Super`+`F1`) shows.

{{< profiles >}}

**Inside the capture and recording panels**, the same in every profile: `R` region, `S` screen, `W` window, `Esc` closes. In the screenshot panel, `G` turns Gradia on or off and `D` changes the delay. In the recording panel, `Shift`+key records with the system sound, `Ctrl`+key with the microphone, and `A` changes the audio.

## Customize shortcuts

Your shortcuts live in `~/.config/sway/config.d/50-local.conf`. The file is created at your first login, with only comments and examples, and it's yours: neither updates nor a reinstall overwrite it. Sway reads it after Swaydesk's shortcuts and the shortcut profile you chose, so whatever it holds wins.

**Change what a shortcut does:** repeat the key with `--no-warn`. Without it, Sway warns that the key already had a shortcut.

```
## Open foot
bindsym --no-warn Ctrl+Alt+t exec foot
```

**Remove a shortcut:** use `unbindsym` with the key exactly as the active profile defines it, including flags such as `--locked`. Removing a key that has no shortcut is a config error.

```
unbindsym Print
```

**Add a shortcut:** pick a free key. `Super`+`F2` to `Super`+`F12` and `Super`+`Ctrl`+`Alt`+a letter are free in every profile.

```
## Open another terminal
bindsym Mod4+F12 exec kitty
```

The `##` comment right above a shortcut is the description the Help shows.

**Apply:** save the file and run `swaymsg reload` in a terminal, or log in again. If something is wrong, Sway shows a bar at the top of the screen with the offending line.

**Check:** the Swaydesk Help (`Super`+`F1`) shows the shortcuts in use, including your changes. At the bottom of its Shortcuts tab, the **Open** button opens the file in your editor.

The same file also holds this machine's settings: screen, keyboard, mouse, startup programs and apps on workspaces. The examples are in its comments, and the [configuration guide](/en-us/guide/config/#machine-settings) covers them.
