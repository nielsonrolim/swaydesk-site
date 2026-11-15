---
title: Apps
prompt: "ls /usr/bin/swaydesk-*"
crumb: apps
description: The Swaydesk apps, and the ones it relies on.
---
Besides the bar, the dock and the popups, Swaydesk comes with a few apps of its own. They all show up in the app grid (`Super`).

## Desktop Theme

Picks the GTK theme, the icons and the accent color, and applies them all at once: to the bar, the dock, the popups, the window borders, and GTK 3, GTK 4 and libadwaita apps. The choice is saved in `~/.config/sway-desktop/config.toml`. From a terminal, `swaydesk-theme` does the same. See [configuration](/en-us/guide/config/).

## Screenshot

Opens the screenshot panel (`Super`+`Shift`+`E`): a region, the whole screen or a window, with an optional delay. The image goes to the clipboard and to `~/Pictures/Screenshots`. With [Gradia](https://flathub.org/apps/be.alexandervanhee.gradia) installed, the capture can open in it to crop, annotate and highlight. To capture without the panel, use `Print` and its variations in the [shortcuts](/en-us/shortcuts/).

## Screen Recording

Opens the recording panel (`Super`+`Shift`+`R`): a region, the whole screen or a window, with the system sound, the microphone or no audio. While recording, a ● on the bar shows it is running; click it, or press the same shortcut, to stop. The video goes to `~/Videos/Screencasts`.

## Displays {{< soon >}}

Arranges your monitors: position, resolution, scale and rotation, and which monitor each workspace lives on. Until it arrives, [nwg-displays](https://github.com/nwg-piotr/nwg-displays) does the same, and the session already reads what it saves.

## Help {{< soon >}}

Shows the session's keyboard shortcuts, with search. The descriptions come from the Sway configuration itself, so a shortcut you add shows up there too.

## Wallpaper of the day

When you log in, Swaydesk downloads Bing's image of the day and sets it as the wallpaper. Without a network, the last downloaded image stays.

## Apps that come along

| App | What for |
| --- | --- |
| kitty | Terminal (`Ctrl`+`Alt`+`T`) |
| Thunar | File manager (`Ctrl`+`Alt`+`E`) |
| rofi | Launcher (`Alt`+`Space`) |
| Blueman | Bluetooth pairing (PIN and confirmation requests) |
| pavucontrol | Fine-grained audio settings, beyond the bar popup (middle-click the volume) |
