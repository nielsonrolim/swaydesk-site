---
title: Configuration
prompt: "cat ~/.config/sway-desktop/config.toml"
crumb: guide/config
weight: 3
description: The files you edit to fit Swaydesk to your machine and your taste.
---
The Sway and bar configuration comes with the package and is updated with it. What's yours lives in a few files in your home folder, which the first login creates and updates never overwrite.

| File | What it holds |
| --- | --- |
| `~/.config/sway-desktop/config.toml` | Language, theme, icons, accent color, weather city, holidays and file manager |
| `~/.config/sway/config.d/50-local.conf` | Monitors, keyboard, mouse, startup apps and app workspaces |
| `~/.config/sway/outputs` | Your displays, saved by `nwg-displays` |
| `~/.config/sway-dock/config.toml` | The dock mode and size |

## Desktop settings

`~/.config/sway-desktop/config.toml` applies to every piece of Swaydesk. The easiest way to change the theme and the color is the **Desktop Theme** app, which writes this file for you. From a terminal, `swaydesk-theme` does the same:

```
swaydesk-theme families                  # the installed theme families
swaydesk-theme pick Adwaita dark teal    # family, light or dark, and color
swaydesk-theme current                   # the theme, icons and color in use
```

The colors are the Papirus folder colors; `swaydesk-theme colors` lists them all.

Here's a sample file with the keys you can change by hand:

```
# Language for text, dates and the weather. Empty: the system language
locale = "en_US"

# City for the weather forecast. Empty: based on your IP address
weather_location = "Denver"

# Country for calendar holidays. Empty: from the language. "none": no holidays
holidays = "US"

# GTK theme, icons and accent color
gtk_theme = "Adwaita-dark"
icon_theme = "Papirus-Dark"
accent = "#199ca8"

# Papirus folder color, such as "teal". Empty: the closest to the accent
folder_color = ""

# File manager for Ctrl+Alt+E, the app grid and the dock. Empty: the first one installed
file_manager = "thunar"
```

Programs read the file when they start. After editing it by hand:

- for the accent color, run `swaydesk-desktop-config apply`, which writes the colors and reloads Sway; popups pick up the new color right away, and the rest changes at your next login;
- for the file manager, run `swaydesk-desktop-config generate`, so folders opened by other apps go to it too;
- for the language, the city and the holidays, log out and back in.

A bad value doesn't break anything: that piece just uses the default for that key.

## Machine settings

Sway reads the files in `~/.config/sway/config.d/` last, so whatever is there wins over the package configuration. The first login creates `50-local.conf` with commented examples and the system keyboard layout. Edit it and apply with `Super`+`R` (or `swaymsg reload`).

A filled-in example:

```
# Display: get the output name from `swaymsg -t get_outputs`
output eDP-1 mode 1920x1080@60Hz scale 1

# Keyboard: Brazilian ABNT2 and US International, switched with Super+Space
input type:keyboard {
    xkb_layout  br,us
    xkb_variant abnt2,intl
}

# Mouse: left-handed with natural scrolling
input type:pointer {
    left_handed    enabled
    natural_scroll enabled
}

# Apps to start at login (Sway doesn't read ~/.config/autostart)
exec nextcloud --background

# App workspaces: the app opens there, and you stay where you are
assign [app_id="^org.mozilla.firefox$"] workspace number 2
assign [app_id="^thunderbird$"]         workspace number 9

# To change a shortcut that already exists, use --no-warn
bindsym --no-warn Ctrl+Alt+t exec foot
```

A few tips:

- With two layouts in `xkb_layout`, the session always starts with the first one.
- To find the `app_id` of an open window, run `swaymsg -t get_tree | grep app_id`. Apps running through XWayland use `class=` instead of `app_id=`.
- Swaydesk generates `00-accent.conf` and `00-font.conf` in the same folder: don't edit them, since they get rewritten.
- The full reference for these commands is in `man 5 sway` and `man 5 sway-input`.

## Launcher searches

The searches in the launcher's **Web** tab can be changed in `~/.config/sway-desktop/launcher.conf`, one `key = value` per line (`#` starts a comment):

```
# a prefix and the search address; %s is the text you type
search = gh https://github.com/search?q=%s
# the search for text without a prefix (without this line, Google)
default = d
```

A `search` line with a new prefix adds a search, and one with an existing prefix (`g`, `d`, `w`, `yt`, `gt`, `cl`, `gpt`) replaces it. The address must start with `http://` or `https://`, contain `%s` and have no spaces, or the line is ignored; a `default` with an unknown prefix falls back to Google. The change takes effect the next time you open the launcher.

## Displays

The easiest way to set the resolution, position and scale of your screens is `nwg-displays`, in the app grid. It saves your setup to `~/.config/sway/outputs` and each screen's workspaces to `~/.config/sway/workspaces`. Sway reads these two files after everything else, so they win over an `output` line in `50-local.conf`.

## The dock

The dock reads `~/.config/sway-dock/config.toml`, which doesn't exist at first: create it with only what you want to change. After editing, run `swaydesk-dock reload`.

```
# overlap: hides when a window needs its space
# auto-hide: hidden until you push the pointer against the edge
# always: always visible
mode = "auto-hide"

icon_size = 40          # from 16 to 128
hide_delay_ms = 400     # delay before hiding, in milliseconds
animation_ms = 200      # slide duration; 0 turns it off

ignore = []             # app_ids that never show on the dock
outputs = ["eDP-1"]     # monitors with a dock; empty: all of them
```

Pinned apps are listed in `~/.local/share/sway-dock/pinned`, but it's simpler to pin them with a right-click on the dock or in the app grid. The app grid keeps its groups and favorites in `~/.local/share/sway-drawer/`.

## SwayFX on Arch (optional)

[SwayFX](https://github.com/WillPower3309/swayfx) is Sway with rounded corners, blur and shadows. On Arch it can take Sway's place, with the same configuration. It comes from the AUR, through an AUR helper:

```
yay -S swayfx           # or: paru -S swayfx; pacman swaps sway for it
sudo pacman -S sway     # to go back to Sway
```

`swaydesk-desktop` stays installed either way, because `swayfx` provides `sway`.

**Warning:** SwayFX comes from the AUR and is maintained by third parties, outside the project's support. It can lag behind Sway releases, and a `pacman -Syu` that brings a new wlroots can break it until the AUR catches up. If the session doesn't start after an update, go back to Sway with `sudo pacman -S sway` from a text console (Ctrl+Alt+F2).

Swaydesk turns the effects on by itself at the next login. It notices SwayFX and writes `~/.config/sway/config.d/10-effects.conf`; with plain Sway the file holds only a comment. The file is written again at every login, when the theme changes, and with `sway-desktop-config generate` (then run `swaymsg reload`).

The effects live in the `[effects]` section of `~/.config/sway-desktop/config.toml`. A missing key keeps its default:

```
[effects]
corner_radius = 10      # window and layer corners, in pixels, from 0 (square) to 30
blur = true             # blur behind transparent windows
shadows = true          # a light shadow on windows
layer_blur = false      # blur behind the bar, the dock, popups, notifications and menus
dim_inactive = 0.0      # darken unfocused windows, from 0.0 (not at all) to 1.0
```

The blur behind the bar, the dock and the popups is off by default, because it showed visual garbage in a virtual machine (virgl). Turn it on with `layer_blur = true`. Two things never get blur: the invisible layer that closes popups when you click outside them, and the screenshot picker, which has to show the screen sharp.

## The login screen

With `swaydesk-greeter`, the login screen has its own settings, for the whole machine:

- `/etc/swaydesk-greeter/config.toml` takes the accent color and the language, in the same format as the desktop settings (`accent = "#8e44ad"`, `locale = "en_US"`);
- files in `/etc/swaydesk-greeter/sway.d/*.conf` take Sway commands for the login screen's displays, such as `output eDP-1 scale 1.25`.
