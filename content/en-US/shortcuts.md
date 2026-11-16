---
title: Shortcuts
prompt: "grep bindsym ~/.config/sway/config"
crumb: shortcuts
description: Every keyboard shortcut of the Swaydesk session.
---
The shortcuts follow KDE Plasma with Krohnkite. `Super` is the logo key.

> This table was written from the Sway configuration. Soon it will be generated from the same descriptions the **Help** app shows.

## Session and apps

| Shortcut | What it does |
| --- | --- |
| `Super` (alone) | Shows or hides the app grid |
| `Alt`+`Space` | Launcher: apps, open windows, clipboard and web search |
| `Super`+`` ` `` (left of 1) | List of open windows, to search |
| `Ctrl`+`Alt`+`T` | Terminal |
| `Ctrl`+`Alt`+`E` | File manager |
| `Super`+`C` | Notification center |
| `Super`+`V` | Clipboard history |
| `Super`+`Space` | Switches the keyboard layout |
| `Ctrl`+`Alt`+`L` | Locks the screen |
| `Ctrl`+`Alt`+`Delete` | Session menu: lock, log out, suspend, restart, shut down |
| `Super`+`R` | Reloads the Sway configuration |
| `Super`+`Shift`+`O` | Turns the screen back on if it stays off (works while locked) |

## Windows

| Shortcut | What it does |
| --- | --- |
| `Alt`+`Tab` / `Alt`+`Shift`+`Tab` | Switches windows in the order of use, with the switcher on screen |
| `Super`+`Tab` / `Super`+`Shift`+`Tab` | Next or previous window in screen order |
| `Super`+`H` `J` `K` `L` or `Super`+`Alt`+arrows | Focuses the window to the left, below, above or to the right |
| `Super`+`Shift`+`H` `J` `K` `L` | Moves the window |
| `Super`+`Ctrl`+`H` `J` `K` `L` | Resizes the window |
| `Super`+`Enter` | Swaps the window with the first one in the workspace (the "master") |
| `Super`+`Q` or `Super`+`Ctrl`+`Esc` | Closes the window |
| `Super`+`F` | Floats or tiles the window |
| `Super`+`Shift`+`F` | Floats or tiles every window in the workspace |
| `Super`+`M`, `Super`+`Page Up` or `Super`+`Ctrl`+`F` | Fullscreen |
| `Super`+`Page Down` | Puts the window aside (Sway's "minimize") |
| `Super`+`Backspace` or `Super`+`Z` | Brings the window back |
| `Super`+`Shift`+`G` | Keeps a floating window on every workspace |

## Layout

| Shortcut | What it does |
| --- | --- |
| `Super`+`]` | Cycles side by side, one above the other, stacked and tabbed |
| `Super`+`Ctrl`+`T` | Back to side by side |
| `Super`+`Ctrl`+`Enter` | Toggles the next split between horizontal and vertical |
| `Super`+`Ctrl`+`X` / `Z` | More or less space between windows |
| `Super`+`Ctrl`+`R` | Turns the space between windows on or off |

## Workspaces and monitors

| Shortcut | What it does |
| --- | --- |
| `Super`+`1`…`9` | Goes to the workspace |
| `Super`+`Ctrl`+`1`…`9` | Takes the window to the workspace, and follows it |
| `Super`+`←` / `→` | Previous or next workspace, even if empty |
| `Super`+`Ctrl`+`←` / `→` | Takes the window to the previous or next workspace |
| `Super`+mouse wheel | Previous or next workspace |
| `Super`+`W` / `E` | Focuses the monitor on the left or on the right |
| `Super`+`Ctrl`+`W` / `E` or `Super`+`Shift`+`←` / `→` | Takes the window to the other monitor |

## Screenshots and recording

| Shortcut | What it does |
| --- | --- |
| `Print` | Captures a region |
| `Shift`+`Print` | Captures the whole screen |
| `Super`+`Print` | Captures the window |
| `Ctrl` + any of the three | The same, and opens the capture in Gradia to edit |
| `Super`+`Shift`+`E` | Screenshot panel |
| `Super`+`Shift`+`R` | Recording panel; while recording, stops it |

In the panels: `R` region, `S` screen, `W` window, `Esc` closes. In the screenshot panel, `G` turns Gradia on or off and `D` changes the delay. In the recording panel, `Shift`+key records with the system sound, `Ctrl`+key with the microphone, and `A` changes the audio.

## Media and brightness

They also work while the screen is locked.

| Key | What it does |
| --- | --- |
| Volume +, −, mute | Volume, with the on-screen indicator |
| Microphone mute | Turns the microphone on or off |
| Play, next, previous | Controls the player that is playing |
| Brightness +, − | Brightness, with the on-screen indicator |

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

**Check:** the Swaydesk Help (`Super`+`F1`) shows the shortcuts in use, including your changes.

The same file also holds this machine's settings: screen, keyboard, mouse, startup programs and apps on workspaces. The examples are in its comments, and the [configuration guide](/en-us/guide/config/#machine-settings) covers them.
