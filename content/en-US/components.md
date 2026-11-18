---
title: Components
prompt: "ls /usr/bin/swaydesk-*"
crumb: components
aliases: ["/en-us/apps/"]
description: Swaydesk's pieces, one by one.
---
Swaydesk is made of components of its own, nearly all written in Rust with GTK 4. Each one has its shortcut and a part in the [guide](/en-us/guide/).

The shortcuts on this page are those of the **Swaydesk** profile, the default. The other profiles (i3, Hyprland, niri and dwm) change many of them: see them all in [Shortcuts](/en-us/shortcuts/).

Nearly every component can be turned off. The last line of each one shows the key, which goes in `~/.config/sway-desktop/config.toml`; see [Turning components off](/en-us/guide/config/#turning-components-off).


## Bar and popups

{{< component title="Network" shot="network" keys="Click the network icon" guide="guide/desktop/#the-bar" bin="swaydesk-network-popup" src="rust/network-popup" tech="rust" off="bar.network" >}}Wi-Fi, wired and VPN: turn them on and off, connect, enter the password and see the details. Works with NetworkManager, and also with iwd and systemd-networkd (VPN only with NetworkManager).{{< /component >}}

{{< component title="Bluetooth" shot="bluetooth" keys="Click the Bluetooth icon" guide="guide/desktop/#the-bar" bin="swaydesk-bluetooth-popup" src="rust/bluetooth-popup" tech="rust" off="bar.bluetooth" >}}Turns Bluetooth on, finds devices, pairs, connects, forgets them and sends files.{{< /component >}}

{{< component title="Audio" shot="audio" keys="Click the volume (middle click: pavucontrol)" guide="guide/desktop/#the-bar" bin="swaydesk-audio-popup" src="rust/audio-popup" tech="rust" off="bar.volume" >}}Volume and mute for the output and the microphone, and which device each one uses.{{< /component >}}

{{< component title="Battery" shot="battery" keys="Click the battery" guide="guide/desktop/#the-bar" bin="swaydesk-battery-popup" src="rust/battery-popup" tech="rust" off="bar.battery" >}}Charge, time left, power draw, health, a 12-hour graph and the power profile.{{< /component >}}

{{< component title="Brightness and night light" shot="brightness" keys="Click the brightness icon; brightness keys" guide="guide/desktop/#the-bar" bin="swaydesk-brightness-popup" src="rust/brightness-popup" tech="rust" off="bar.brightness" >}}Screen brightness and the night light: off, on, or on the schedule you pick.{{< /component >}}

{{< component title="Media" shot="media" keys="Click the media icon (only there while something plays)" guide="guide/desktop/#the-bar" bin="swaydesk-media-popup" src="rust/media-popup" tech="rust" off="bar.media" >}}Cover, title, progress and the controls of whatever player is playing.{{< /component >}}

{{< component title="Weather" shot="weather" keys="Click the temperature" guide="guide/desktop/#the-bar" bin="swaydesk-weather-popup" src="rust/weather-popup" tech="rust" off="bar.weather" >}}The forecast for today and the next days, for the city you set or the one your IP points to.{{< /component >}}

{{< component title="Calendar" shot="calendar" keys="Click the date" guide="guide/desktop/#the-bar" bin="swaydesk-calendar" src="rust/calendar" tech="rust" off="bar.clock" >}}The month, with your country's holidays.{{< /component >}}

{{< component title="System" shot="system" keys="Click the system icon" guide="guide/desktop/#the-bar" bin="swaydesk-system-popup" src="rust/system-popup" tech="rust" off="bar.system" >}}CPU, memory, disk, temperature and the busiest processes, with "End". The icon turns orange when something is tight.{{< /component >}}

{{< component title="Caffeine" shot="caffeine" keys="Click the cup" guide="guide/desktop/#the-bar" bin="swaydesk-caffeine-popup" src="rust/caffeine-popup" tech="rust" off="bar.caffeine" >}}Keeps the screen from locking and the computer from sleeping for 1 hour, 2 hours or always.{{< /component >}}

{{< component title="Notification center" shot="notifications" keys="`Super`+`C`; click the bell" guide="guide/desktop/#notifications" bin="swaydesk-notifications-popup" src="rust/notifications-popup" tech="rust" off="bar.notifications" >}}Notifications grouped by app, with their actions, and Do Not Disturb.{{< /component >}}

{{< component title="Clipboard" shot="clipboard" keys="`Super`+`V`" guide="guide/desktop/#clipboard-history" bin="swaydesk-clipboard-popup" src="rust/clipboard-popup" tech="rust" off="clipboard_history" >}}The history of what you copied, with search, thumbnails and pinned items. Turned off, nothing more is saved to the history.{{< /component >}}

The bar also shows the keyboard layout when there are two or more; a click switches the layout. To take it off the bar: `[enabled.bar] language = false`.


## Windows and apps

{{< component title="Dock" shot="desktop" keys="Push the pointer against the bottom edge" guide="guide/desktop/#the-dock" bin="swaydesk-dock" src="rust/dock" tech="rust" off="dock" >}}Pinned and open apps, with a right-click menu. It hides when a window needs the room, or stays visible.{{< /component >}}

{{< component title="App grid" shot="drawer" keys="`Super`" guide="guide/desktop/#the-app-grid" bin="swaydesk-drawer" src="rust/drawer" tech="rust" off="app_grid" >}}Every installed app, with search, groups and favorites. The search also finds files, does math and converts units.{{< /component >}}

{{< component title="Launcher" shot="launcher-apps" keys="`Alt`+`Space`" guide="guide/desktop/#the-launcher" bin="sway-launcher (rofi)" src="home/.local/bin/sway-launcher" tech="script" >}}rofi with four tabs: apps, open windows, clipboard and web search (with prefixes such as `w` for Wikipedia). One click opens an entry, and a click outside closes it.{{< /component >}}

{{< component title="Window switcher" shot="switcher" keys="`Alt`+`Tab`" guide="guide/desktop/#switching-windows" bin="swaydesk-switcher" src="rust/switcher" tech="rust" off="switcher" >}}Windows in the order you used them, from every workspace, on a card in the middle of the screen.{{< /component >}}


## Session

{{< component title="Notifications" guide="guide/desktop/#notifications" bin="swaydesk-notifd" src="rust/notifd" tech="rust" off="notifications" >}}The service that receives the apps' notifications and shows the pop-ups in the corner.{{< /component >}}

{{< component title="Volume and brightness indicator" shot="osd" keys="Volume and brightness keys" bin="swaydesk-osd-bar" src="rust/osd-bar" tech="rust" off="osd" >}}Icon, bar and percentage on screen for a second.{{< /component >}}

{{< component title="Session menu" shot="session" keys="`Ctrl`+`Alt`+`Delete`; the bar's power button" guide="guide/desktop/#session-menu" bin="swaydesk-session-menu" src="rust/session-menu" tech="rust" >}}Lock, log out, suspend, restart and shut down.{{< /component >}}

{{< component title="Lock screen" shot="lock" keys="`Ctrl`+`Alt`+`L`; on its own after 10 minutes" guide="guide/desktop/#lock-screen-and-idle" bin="swaydesk-lock" src="rust/lock" tech="rust" >}}Time, date and the password field on every monitor, over the blurred wallpaper. It needs gtk4-layer-shell 1.2; before that, as on Debian 13, swaylock locks the screen.{{< /component >}}

{{< component title="Login screen (optional)" shot="greeter" guide="guide/first-steps/#optional-the-swaydesk-login-screen" bin="swaydesk-greeter" src="rust/greeter" tech="rust" >}}A login screen on top of greetd, with the same look as the lock screen, on every supported distro, Arch included. It unlocks the keyring with your login password. The login screen you already use works too.{{< /component >}}

{{< component title="Keyring" guide="guide/desktop/#passwords-and-keyring" bin="swaydesk-keyring" src="rust/keyring" tech="rust" >}}gnome-keyring keeps the apps' passwords and unlocks when you log in. On Debian 13, each user's first login shows a notice and asks for the password once; from then on, the keyring unlocks by itself. On Ubuntu and Arch, it asks for nothing.{{< /component >}}

{{< component title="Administrator password" keys="When an app asks for permission" guide="guide/desktop/#passwords-and-keyring" bin="sway-polkit-agent (mate-polkit)" src="home/.local/bin/sway-polkit-agent" tech="script" off="polkit_agent" >}}Starts the polkit agent: the window that asks for your password for administrator actions, such as mounting a disk. With no agent installed, a notification says so.{{< /component >}}

{{< component title="Update notifier" keys="At login" bin="sway-update-notifier" src="home/.local/bin/sway-update-notifier" tech="script" off="update_notifier" >}}Starts the distro's update notifier, which Sway doesn't start by itself: GNOME Software's, Ubuntu's Software Updater or Discover's. With none of them, it does nothing.{{< /component >}}

{{< component title="Night light" keys="In the brightness popup" guide="guide/desktop/#the-bar" bin="sway-nightlight (gammastep)" src="home/.local/bin/sway-nightlight" tech="script" off="nightlight" >}}Warms up the colors at night through gammastep, and comes back in its last mode when you log in.{{< /component >}}

{{< component title="Wallpaper of the day" keys="At login" bin="bing-wallpaper" src="home/.local/bin/bing-wallpaper" tech="script" off="bing_wallpaper" >}}Downloads Bing's image of the day and sets it as the wallpaper.{{< /component >}}


## Apps of its own

{{< component title="Desktop Theme" shot="theme" keys="In the app grid" guide="guide/config/" bin="swaydesk-theme-app" src="rust/theme-app" tech="rust" >}}Picks the GTK theme, the icons and the accent color, and applies them all at once, GTK and libadwaita apps included.{{< /component >}}

{{< component title="Displays" shot="displays" keys="In the app grid" guide="guide/config/#displays" bin="swaydesk-displays" src="rust/displays" tech="rust" off="displays" >}}Your screens on a map, to drag around, with each one's resolution, refresh rate, scale and rotation, and whether it's on. A change undoes itself after 15 seconds unless you keep it. Each set of monitors keeps its own layout, applied when you plug or unplug a screen, and the laptop screen turns off with the lid closed and an external monitor on. The key turns off only these automatic profiles; the app stays.{{< /component >}}

{{< component title="Help" shot="help" keys="`Super`+`F1`; `Super`+`/`" guide="shortcuts/" bin="swaydesk-help" src="rust/help" tech="rust" >}}The shortcuts of the profile in use, with search, read from the Sway configuration itself, and a card for each part of the desktop, with its shortcut and a button that opens it. It's also where you switch the shortcut profile and open your `50-local.conf` to edit it.{{< /component >}}

{{< component title="Shortcut profiles" keys="In the Help; or `shortcuts` in `config.toml`" guide="shortcuts/" src="home/.config/sway/keys/" tech="Sway" >}}The shortcuts of Swaydesk, i3, Hyprland, niri or dwm (which uses `Alt` as the modifier), all with 9 workspaces. A switch applies at once, without logging out, and your `50-local.conf` wins over any profile.{{< /component >}}

{{< component title="Screenshot" shot="capture" keys="`Super`+`Shift`+`E`; `Print`" guide="guide/desktop/#screenshots-and-recording" bin="swaydesk-capture" src="rust/capture" tech="rust" >}}A region, the whole screen or a window, with a delay. It goes to the clipboard and to `~/Pictures/Screenshots`; with Gradia, it opens for editing.{{< /component >}}

{{< component title="Screen recording" shot="recording" keys="`Super`+`Shift`+`R`" guide="guide/desktop/#screenshots-and-recording" bin="swaydesk-capture" src="rust/capture" tech="rust" >}}A region, the whole screen or a window, with the system sound, the microphone or no audio. The video goes to `~/Videos/Screencasts`.{{< /component >}}

{{< component title="Desktop configuration" keys="In the terminal" guide="guide/config/" bin="swaydesk-desktop-config" src="rust/desktop-config" tech="rust" >}}Reads `~/.config/sway-desktop/config.toml` and writes the files that Sway, the bar and the apps use. After editing the file by hand, `swaydesk-desktop-config apply` applies the accent color, and `swaydesk-desktop-config generate` writes the rest.{{< /component >}}


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
| mate-polkit | The administrator password window (on Debian, lxpolkit works too) |
| gnome-text-editor | The Help's **Open** button, which edits `50-local.conf`; without it, the Help opens an editor in the terminal. Optional on Arch |
| grim, slurp and wf-recorder | Screenshots and screen recording |
| swaylock | The fallback lock screen; on Debian 13, the one in use |
