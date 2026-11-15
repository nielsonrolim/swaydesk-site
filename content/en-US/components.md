---
title: Components
prompt: "ls /usr/bin/swaydesk-*"
crumb: components
aliases: ["/en-us/apps/"]
description: Swaydesk's pieces, one by one.
---
Swaydesk is made of components of its own, nearly all written in Rust with GTK 4. Each one has its shortcut and a part in the [guide](/en-us/guide/). Soon, each component can be turned off in the configuration.


## Bar and popups

{{< component title="Network" keys="Click the network icon" guide="guide/desktop/#the-bar" bin="swaydesk-network-popup" tech="rust" >}}Wi-Fi, wired and VPN: turn them on and off, connect, enter the password and see the details. Works with NetworkManager, and also with iwd and systemd-networkd (VPN only with NetworkManager).{{< /component >}}

{{< component title="Bluetooth" keys="Click the Bluetooth icon" guide="guide/desktop/#the-bar" bin="swaydesk-bluetooth-popup" tech="rust" >}}Turns Bluetooth on, finds devices, pairs, connects, forgets them and sends files.{{< /component >}}

{{< component title="Audio" shot="audio" keys="Click the volume (middle click: pavucontrol)" guide="guide/desktop/#the-bar" bin="swaydesk-audio-popup" tech="rust" >}}Volume and mute for the output and the microphone, and which device each one uses.{{< /component >}}

{{< component title="Battery" keys="Click the battery" guide="guide/desktop/#the-bar" bin="swaydesk-battery-popup" tech="rust" >}}Charge, time left, power draw, health, a 12-hour graph and the power profile.{{< /component >}}

{{< component title="Brightness and night light" shot="brightness" keys="Click the brightness icon; brightness keys" guide="guide/desktop/#the-bar" bin="swaydesk-brightness-popup" tech="rust" >}}Screen brightness and the night light: off, on, or on the schedule you pick.{{< /component >}}

{{< component title="Media" shot="media" keys="Click the media icon (only there while something plays)" guide="guide/desktop/#the-bar" bin="swaydesk-media-popup" tech="rust" >}}Cover, title, progress and the controls of whatever player is playing.{{< /component >}}

{{< component title="Weather" shot="weather" keys="Click the temperature" guide="guide/desktop/#the-bar" bin="swaydesk-weather-popup" tech="rust" >}}The forecast for today and the next days, for the city you set or the one your IP points to.{{< /component >}}

{{< component title="Calendar" shot="calendar" keys="Click the date" guide="guide/desktop/#the-bar" bin="swaydesk-calendar" tech="rust" >}}The month, with your country's holidays.{{< /component >}}

{{< component title="System" shot="system" keys="Click the system icon" guide="guide/desktop/#the-bar" bin="swaydesk-system-popup" tech="rust" >}}CPU, memory, disk, temperature and the busiest processes, with "End". The icon turns orange when something is tight.{{< /component >}}

{{< component title="Caffeine" shot="caffeine" keys="Click the cup" guide="guide/desktop/#the-bar" bin="swaydesk-caffeine-popup" tech="rust" >}}Keeps the screen from locking and the computer from sleeping for 1 hour, 2 hours or always.{{< /component >}}

{{< component title="Notification center" shot="notifications" keys="`Super`+`C`; click the bell" guide="guide/desktop/#notifications" bin="swaydesk-notifications-popup" tech="rust" >}}Notifications grouped by app, with their actions, and Do Not Disturb.{{< /component >}}

{{< component title="Clipboard" shot="clipboard" keys="`Super`+`V`" guide="guide/desktop/#clipboard-history" bin="swaydesk-clipboard-popup" tech="rust" >}}The history of what you copied, with search, thumbnails and pinned items.{{< /component >}}


## Windows and apps

{{< component title="Dock" shot="desktop" keys="Push the pointer against the bottom edge" guide="guide/desktop/#the-dock" bin="swaydesk-dock" tech="rust" >}}Pinned and open apps, with a right-click menu. It hides when a window needs the room, or stays visible.{{< /component >}}

{{< component title="App grid" shot="drawer" keys="`Super`" guide="guide/desktop/#the-app-grid" bin="swaydesk-drawer" tech="rust" >}}Every installed app, with search, groups and favorites. The search also does math, and converts units with `qalc`.{{< /component >}}

{{< component title="Launcher" shot="launcher-apps" keys="`Alt`+`Space`" guide="guide/desktop/#the-launcher" bin="sway-launcher (rofi)" tech="script" >}}rofi with four tabs: apps, open windows, clipboard and web search (with prefixes such as `w` for Wikipedia).{{< /component >}}

{{< component title="Window switcher" shot="switcher" keys="`Alt`+`Tab`" guide="guide/desktop/#switching-windows" bin="swaydesk-switcher" tech="rust" >}}Windows in the order you used them, from every workspace, on a card in the middle of the screen.{{< /component >}}


## Session

{{< component title="Notifications" guide="guide/desktop/#notifications" bin="swaydesk-notifd" tech="rust" >}}The service that receives the apps' notifications and shows the pop-ups in the corner.{{< /component >}}

{{< component title="Volume and brightness indicator" shot="osd" keys="Volume and brightness keys" bin="swaydesk-osd-bar" tech="rust" >}}Icon, bar and percentage on screen for a second.{{< /component >}}

{{< component title="Session menu" shot="session" keys="`Ctrl`+`Alt`+`Delete`; the bar's power button" guide="guide/desktop/#session-menu" bin="swaydesk-session-menu" tech="rust" >}}Lock, log out, suspend, restart and shut down.{{< /component >}}

{{< component title="Lock screen" keys="`Ctrl`+`Alt`+`L`; on its own after 10 minutes" guide="guide/desktop/#lock-screen-and-idle" bin="swaydesk-lock" tech="rust" >}}Time, date and the password field on every monitor, over the blurred wallpaper. It needs gtk4-layer-shell 1.2; before that, as on Debian 13, swaylock locks the screen.{{< /component >}}

{{< component title="Login screen (optional)" shot="greeter" guide="guide/first-steps/#optional-the-swaydesk-login-screen" bin="swaydesk-greeter" tech="rust" >}}A login screen on top of greetd, with the same look as the lock screen. The one you already use works too.{{< /component >}}

{{< component title="Night light" keys="In the brightness popup" guide="guide/desktop/#the-bar" bin="sway-nightlight (gammastep)" tech="script" >}}Warms up the colors at night through gammastep, and comes back in its last mode when you log in.{{< /component >}}

{{< component title="Wallpaper of the day" keys="At login" bin="bing-wallpaper" tech="script" >}}Downloads Bing's image of the day and sets it as the wallpaper.{{< /component >}}


## Apps of its own

{{< component title="Desktop Theme" shot="theme" keys="In the app grid" guide="guide/config/" bin="swaydesk-theme-app" tech="rust" >}}Picks the GTK theme, the icons and the accent color, and applies them all at once, GTK and libadwaita apps included.{{< /component >}}

{{< component title="Screenshot" shot="capture" keys="`Super`+`Shift`+`E`; `Print`" guide="guide/desktop/#screenshots-and-recording" bin="swaydesk-capture" tech="rust" >}}A region, the whole screen or a window, with a delay. It goes to the clipboard and to `~/Pictures/Screenshots`; with Gradia, it opens for editing.{{< /component >}}

{{< component title="Screen recording" shot="recording" keys="`Super`+`Shift`+`R`" guide="guide/desktop/#screenshots-and-recording" bin="swaydesk-capture" tech="rust" >}}A region, the whole screen or a window, with the system sound, the microphone or no audio. The video goes to `~/Videos/Screencasts`.{{< /component >}}

{{< component title="Displays" keys="In the app grid" tech="rust" soon="true" >}}The position, resolution, scale and rotation of each monitor. Until it arrives, nwg-displays does the same.{{< /component >}}

{{< component title="Help" keys="In the app grid" tech="rust" soon="true" >}}The session's keyboard shortcuts, with search, taken from the Sway configuration itself.{{< /component >}}


## Apps that come along

| App | What for |
| --- | --- |
| kitty | Terminal (`Ctrl`+`Alt`+`T`) |
| Thunar | File manager (`Ctrl`+`Alt`+`E`) |
| rofi | The launcher (`Alt`+`Space`) |
| Blueman | Bluetooth pairing (PIN and confirmation requests) |
| pavucontrol | Fine-grained audio settings, beyond the bar popup (middle-click the volume) |
