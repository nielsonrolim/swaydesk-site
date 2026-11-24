---
title: Configuration
prompt: "cat ~/.config/swaydesk/config.toml"
crumb: guide/config
weight: 3
description: The files you edit to fit Swaydesk to your machine and your taste.
---
The Sway and bar configuration comes with the package and is updated with it. What's yours lives in a few files in your home folder, which the first login creates and updates never overwrite.

| File | What it holds |
| --- | --- |
| `~/.config/swaydesk/config.toml` | Language, theme, icons, accent color, weather city, holidays, file manager, shortcut profile and the components turned off |
| `~/.config/sway/config.d/50-local.conf` | Monitors, keyboard, mouse, startup apps and app workspaces |
| `~/.config/swaydesk/displays.json` | Your screens for each set of monitors, saved by the **Displays** app |
| `~/.config/sway-dock/config.toml` | The dock mode and size |

Before 0.1.4, the `swaydesk` folders were called `sway-desktop`: `~/.config/sway-desktop`, and the same in `~/.local/share` and `~/.local/state`. The first login on 0.1.4 moves them to `swaydesk` and leaves the old names as links to the new folders, so the old paths keep working. If a file is in both the old and the new folder, nothing moves, the old folder stays in use, and the session log says so (`grep kept: ~/.local/state/sway/sway.log`); merge the two folders by hand to switch.

## Desktop settings

`~/.config/swaydesk/config.toml` applies to every piece of Swaydesk. The easiest way to change the theme and the color is the **Desktop Theme** app, which writes this file for you. From a terminal, `swaydesk-theme` does the same:

```
swaydesk-theme families                  # the installed theme families
swaydesk-theme pick Adwaita dark teal    # family, light or dark, and color
swaydesk-theme current                   # the theme, icons and color in use
swaydesk-theme cursor 32                 # the cursor size; with no number, the sizes the cursor theme has
```

The colors are the Papirus folder colors; `swaydesk-theme colors` lists them all.

The cursor size is in the app too, in the **Cursor size** list below the icons, which shows only the sizes your cursor theme has. A choice applies at once, without **Apply**: GTK 4 and Qt 6 apps follow right away, and older ones (GTK 3, Qt 5, Electron and X11 apps) when you open them again.

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

# true: the accent color comes from the wallpaper and changes with it. Without this key, it's on while the
# accent is the default and there's a wallpaper, and off otherwise
accent_auto = true

# Papirus folder color, such as "teal". Empty: the closest to the accent
folder_color = ""

# File manager for Ctrl+Alt+E, the app grid and the dock. Empty: the first one installed
file_manager = "thunar"

# Power profiles in the System popup: "auto" (the default) only without a battery, "always" or "never"
power_profiles_in_system = "auto"

# Cursor size in pixels, from 16 to 96 (24 by default)
cursor_size = 24
```

Programs read the file when they start. After editing it by hand:

- for the accent color, first set `accent_auto = false`, or the next wallpaper brings its own color back; then run `swaydesk-desktop-config apply`, which writes the colors and reloads Sway; popups pick up the new color right away, and the rest changes at your next login;
- for the file manager, run `swaydesk-desktop-config generate`, so folders opened by other apps go to it too;
- for the language, the city and the holidays, log out and back in;
- for `power_profiles_in_system`, nothing: it applies the next time the System popup opens;
- for `cursor_size`, use `swaydesk-theme cursor <size>` instead, which also applies it at once.

A bad value doesn't break anything: that piece just uses the default for that key.

On a computer without a battery, the battery icon leaves the bar, and with it the profile buttons of its popup. So the System popup gets a **Power profile** row with the profiles `power-profiles-daemon` offers (Power saver, Balanced and, where the hardware supports it, Performance): a click changes the profile without closing the popup. Without the daemon, the row doesn't show. With `"always"` it shows on laptops too; the battery popup keeps its buttons either way.

## Turning components off

Every Swaydesk component starts on, except the input method ([below](#input-method)). To turn one off, set its key to `false` in the `[enabled]` section of `~/.config/swaydesk/config.toml`; the bar modules go in `[enabled.bar]`:

```
[enabled]
dock = false            # the dock
bing_wallpaper = false  # the wallpaper of the day

[enabled.bar]
weather = false         # the weather on the bar
```

| `[enabled]` key | What it turns off |
| --- | --- |
| `dock` | The dock |
| `app_grid` | The app grid (tapping `Super`) |
| `switcher` | The `Alt`+`Tab` card |
| `notifications` | The notification service |
| `osd` | The volume and brightness indicator |
| `clipboard_history` | The clipboard history |
| `nightlight` | The night light |
| `bing_wallpaper` | The wallpaper of the day |
| `polkit_agent` | The polkit agent (the administrator password) |
| `update_notifier` | The update notifier |
| `displays` | The automatic screen profiles; the **Displays** app stays |
| `autostart` | The apps in `~/.config/autostart` and `/etc/xdg/autostart` (see below) |
| `input_method` | Off unless set to `true`: then the session starts the fcitx5 input method (see below) |

The `[enabled.bar]` keys are the bar modules: `weather`, `clock`, `media`, `recording`, `notifications`, `clipboard`, `language`, `system`, `brightness`, `caffeine`, `bluetooth`, `network`, `volume`, `battery`, `power` and, on Arch, `updates`. The workspaces and the tray are always there.

A change applies at your next login. A missing key stays on (except `input_method`), and a mistake in the file never turns anything off. In the Help (`Super`+`F1`), the card of a component that's off says "Turned off" and how to turn it back on. The [Components](/en-us/components/) page shows each one's key.

### Apps that start at login

The session starts the apps of the XDG autostart folders, `~/.config/autostart` and `/etc/xdg/autostart`, as GNOME and KDE do, and closes them when you log out. The entries for what Swaydesk already covers (blueman, nm-applet, the mate and lxpolkit polkit agents, xapp-sn-watcher) are skipped, only in the Swaydesk session: GNOME or KDE on the same account still start them. PulseAudio's own entry is skipped there too, but only when PipeWire is the sound server, where it would just fail.

To keep one app from starting, put a copy of its `.desktop` file in `~/.config/autostart` with `Hidden=true`, or with `NotShowIn=sway;` to skip it only in Sway sessions, so GNOME or KDE still start it. To turn all of them off, set `autostart = false` in `[enabled]`. A `config.toml` from an earlier version doesn't have that key: add the line inside `[enabled]`, before the `[enabled.bar]` part, since a line below `[enabled.bar]` belongs to the bar.

### Input method (fcitx5) {#input-method}

On Wayland, Chromium, Chrome, Vivaldi, Brave and Electron apps (VS Code, Slack, Discord) ignore `~/.XCompose` and compose accents with a table of their own, the en_US one, where `'` + `c` gives `ć`. The fcitx5 input method gives them `ç`. With `input_method = true` in `[enabled]` and the `fcitx5` package installed, the login starts fcitx5 with its own shortcuts, tray icon and notices off, set to the session's keyboard (the first layout). It follows the keyboard when you change it in `50-local.conf`, until you change fcitx5's input methods yourself (in `fcitx5-configtool`, for example). Sway still switches the layout with `Super`+`Space`, and GTK apps keep composing on their own.

The key is off on a system that installed the packages, and on in the Debian 13 and Arch install images, through `/etc/swaydesk/config.toml`, which only holds the system's defaults for `[enabled]`. A line in your own `config.toml` wins.

The browsers also need two options, `--enable-wayland-ime --wayland-text-input-version=3`:

- **On Arch**, the login creates the files of options that the launchers read, in `~/.config`: `chromium-flags.conf`, `chrome-flags.conf`, `vivaldi-stable.conf`, `brave-flags.conf`, `electron-flags.conf` and `code-flags.conf`, only for what is installed and only when the file doesn't exist. Add the two options to a file of your own. A browser installed in the middle of a session gets its file at the next login: log out and in again (or create the file) before opening it.
- **On Debian**, Chromium doesn't read those files and reaches fcitx5 through the `GTK_IM_MODULE=fcitx` that im-config, which comes with fcitx5, exports. Chrome and Vivaldi from their makers' `.deb` files, and Electron apps, need the options in their shortcut: copy the `.desktop` file to `~/.local/share/applications` and add them to its `Exec` line.

Nothing starts if another input method is set up (`GTK_IM_MODULE`, `QT_IM_MODULE` or `XMODIFIERS` pointing to another one, such as the ibus that Linux Mint's im-config exports) or if `ibus-daemon` is already running. If you start ibus from `50-local.conf`, turn `input_method` off. On Linux Mint, to use fcitx5, pick it with `im-config -n fcitx5` (with the `fcitx5-frontend-gtk3` and `fcitx5-frontend-gtk4` packages) and turn the key on.

To turn it off, set `input_method = false`: it applies at the next login, and the files it created stay. On Arch, the fcitx5 package's own autostart entry still starts it, as in any session: remove the package, or put a copy of `/etc/xdg/autostart/org.fcitx.Fcitx5.desktop` in `~/.config/autostart` with `NotShowIn=sway;` (only in Swaydesk) or `Hidden=true` (in every desktop of the account). On Debian, im-config exports `GTK_IM_MODULE=fcitx` in every Wayland session while fcitx5 is installed, on any desktop; `im-config -n none` (or removing fcitx5) goes back to the default.

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

# Apps to start at login that have no autostart entry (the ones in ~/.config/autostart already start)
exec foot --server

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

### Keyboard and accents

- **The system keyboard.** The keyboard block that the first login writes at the end of `50-local.conf` follows the system keyboard at every login, as long as nobody edits it. A change with `localectl set-x11-keymap` or `sudo dpkg-reconfigure keyboard-configuration` reaches existing accounts at their next login, and the login screen and new accounts follow too. A block you edited stays as it is, and a block of your own further down in the file wins over ours.
- **Debian and Ubuntu.** There, `localectl` only changes `/etc/vconsole.conf`, which the boot rewrites from `/etc/default/keyboard`: the change that survives a reboot is `sudo dpkg-reconfigure keyboard-configuration`. On Arch, `localectl` lasts.
- **`ç` on US International.** With the session on US International (`intl` or `altgr-intl`), `'` + `c` gives `ç` (and `'` + `C` gives `Ç`) in GTK and Qt apps, in terminals and at the login screen. For that, the login creates this `~/.XCompose`, if nothing is at that path:

  ```
  include "%L"
  <dead_acute> <c> : "ç" ccedilla
  <dead_acute> <C> : "Ç" Ccedilla
  ```

  A file of your own is never touched. If the session stops using US International, the file goes away at the next login, as long as it's unedited. When you write one by hand, keep the `include` line first: without it, the file replaces the whole table and the other accents (`'` + `e`, `~` + `a`) stop working.
- **Accents and input methods.** With no input method (ibus, fcitx) set up, the session uses `GTK_IM_MODULE=simple`, so GTK composes the dead keys itself, in GTK 4 apps too. If you use an input method, set `GTK_IM_MODULE`, `QT_IM_MODULE` or `XMODIFIERS` in `~/.profile` (for example, `export GTK_IM_MODULE=wayland` for fcitx5), and the session leaves them alone. For `ç` in Chromium and Electron apps, see [Input method (fcitx5)](#input-method). The same goes for an on-screen keyboard that types through the input method, such as squeekboard: it needs `export GTK_IM_MODULE=wayland` in `~/.profile`.

## Launcher searches

The searches in the launcher's **Web** tab can be changed in `~/.config/swaydesk/launcher.conf`, one `key = value` per line (`#` starts a comment):

```
# a prefix and the search address; %s is the text you type
search = gh https://github.com/search?q=%s
# the search for text without a prefix (without this line, Google)
default = d
```

A `search` line with a new prefix adds a search, and one with an existing prefix (`g`, `d`, `w`, `yt`, `gt`, `cl`, `gpt`) replaces it. The address must start with `http://` or `https://`, contain `%s` and have no spaces, or the line is ignored; a `default` with an unknown prefix falls back to Google. The change takes effect the next time you open the launcher.

## Displays

The easiest way to set up your screens is the **Displays** app, in the app grid. Drag the screens on the map, pick each one's resolution, refresh rate, scale and rotation, and click **Apply**. Without a click on **Keep** within 15 seconds, everything goes back to how it was.

Each set of monitors (the laptop alone, the laptop with the office monitor…) keeps its own layout in `~/.config/swaydesk/displays.json`, applied by itself when you plug or unplug a screen. With the lid closed and an external monitor on, the laptop screen turns off. The last layout you kept also goes to `~/.config/sway/config.d/90-displays.conf`, read after `50-local.conf`, so it wins over an `output` line there. Don't edit that file by hand: the next **Keep** rewrites it.

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

## Updates on Arch

On Arch, the store's updates part (GNOME Software) is turned off, because the Swaydesk notice takes care of everything: the official repositories, the AUR (through paru or yay, if you already have one installed), Flatpak apps and firmware (fwupd). It checks in the background, shows an icon with the count in the bar and sends a notification when there is something new; nothing is updated on its own. A click (or the notification's **Update** button) opens a terminal with the update.

- **To turn the Swaydesk notice off** (if you'd rather update by hand or with another tool): set `update_notifier = false` in the `[enabled]` section of `~/.config/swaydesk/config.toml` and log in again. The check, the notification and the icon stop, and the store takes care of updates again on its own.
- **To turn the store's updates part back on by hand**, keeping the Swaydesk notice: `gsettings set org.gnome.software allow-updates true` (to undo: `gsettings reset org.gnome.software allow-updates`). With both on, Flatpak updates show up twice.
- **Just the icon:** `updates = false` in the `[enabled.bar]` section hides the icon and keeps the check and the notification.

## SwayFX on Arch (optional)

[SwayFX](https://github.com/WillPower3309/swayfx) is Sway with rounded corners, blur and shadows. On Arch it can take Sway's place, with the same configuration. It comes from the AUR, through an AUR helper:

```
yay -S swayfx           # or: paru -S swayfx; pacman swaps sway for it
sudo pacman -S sway     # to go back to Sway
```

`swaydesk-desktop` stays installed either way, because `swayfx` provides `sway`.

**Warning:** SwayFX comes from the AUR and is maintained by third parties, outside the project's support. It can lag behind Sway releases, and a `pacman -Syu` that brings a new wlroots can break it until the AUR catches up. If the session doesn't start after an update, go back to Sway with `sudo pacman -S sway` from a text console (Ctrl+Alt+F2).

Swaydesk turns the effects on by itself at the next login. It notices SwayFX and writes `~/.config/sway/config.d/10-effects.conf`; with plain Sway the file holds only a comment. The file is written again at every login, when the theme changes, and with `swaydesk-desktop-config generate` (then run `swaymsg reload`).

The effects live in the `[effects]` section of `~/.config/swaydesk/config.toml`. A missing key keeps its default:

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
