---
title: The desktop
prompt: "man swaydesk-dock"
crumb: guide/desktop
weight: 2
description: A tour of the bar, the popups, the dock, the app grid and the rest of the session.
---
Each piece of Swaydesk is its own program, with the same look and the same accent color. Their keyboard shortcuts are all on the [shortcuts](/en-us/shortcuts/) page.

## The bar

The bar sits at the top of each monitor. Workspaces 1 to 9 are on the left, and the empty ones are dimmed. The weather and the clock are in the middle, and the system icons are on the right.

The icons open popups right under the bar. Opening one closes any other, and clicking the icon again, pressing `Esc`, clicking outside or switching workspaces closes it. Hover over an icon for a quick summary.

- **Network:** turns Wi-Fi on and off, lists Wi-Fi networks, wired connections and VPNs, connects, disconnects and shows the details of the active connection (IP, gateway, DNS, signal). Click a network to connect. It works with NetworkManager and, without it, with iwd for Wi-Fi and systemd-networkd for the cable; in that case there are no VPNs and no connection editor. Middle-click opens the NetworkManager connection editor.
- **Bluetooth:** turns Bluetooth and visibility on, lists paired devices, connects, disconnects, searches for and pairs new devices, forgets a device and sends files. The search only runs when you ask and stops by itself after 30 seconds. Pairing codes show up in a blueman dialog, and the popup stays open until pairing is done. Middle-click opens the blueman manager.
- **Audio:** volume and mute for the output and the microphone, and the choice of output and input device, with the current one in the accent color. Scroll over the icon to change the volume, right-click to mute, and middle-click to open `pavucontrol`.
- **Battery:** charge, time left, power draw, battery health, a chart of the last 12 hours, the power profiles, and the battery of other devices such as a headset or a mouse. Right-click switches the power profile, and middle-click shows the status in a notification.
- **Brightness and night light:** the brightness slider and the night light, which makes the screen warmer: off, on all the time, or only during the hours you choose. Scroll over the icon to change the brightness.
- **Caffeine:** while it's on, the screen won't lock or blank and the computer won't suspend when idle. Pick 1 hour, 2 hours or always. Right-click turns it on and off. Closing the lid still locks.
- **Media:** the icon only shows up when something is playing or paused. The popup has the cover, the track, the progress and the controls; with more than one player, a row of buttons switches between them. Middle-click plays or pauses, and right-click skips to the next track.
- **System:** CPU, memory, disk, temperature and the processes using the most. You can end one of your own processes: click **End** and click again to confirm. Right-click opens the system monitor.
- **Weather:** current conditions, the next hours and the next three days, from wttr.in. The city comes from your IP address, or from the configuration (see [Configuration](/en-us/guide/config/)).
- **Calendar:** click the clock to see the month, with today in the accent color and your country's holidays. The arrows and the scroll wheel change the month, and **Today** brings you back.
- **Notifications and clipboard:** the bell and the clipboard icon open the popups described below.
- **Keyboard:** shows the current layout; click it to switch to the next one.
- **Power:** the button at the far right opens the session menu.

When you change the volume or the brightness with the keys or the scroll wheel, an indicator shows up for a second near the bottom of the screen, above the dock.

## The dock

The dock sits at the bottom, with your pinned apps, then the open ones and, at the end, the app grid button. One dot under an icon means one open window, and two dots mean several. The dot takes the accent color when that window has the focus.

| Action | What happens |
| --- | --- |
| Click a closed app | Opens it |
| Click an app with one window | Focuses the window, switching workspaces if needed |
| Click an app with several windows | Lists their titles so you can pick one |
| Right-click | Pin or unpin, new window, close or close all |
| Drag a pinned app | Changes the order |

The dock has three modes:

- **Overlap** (`overlap`, the default): visible, and it only hides when a window needs its space. In practice, you'll see it on an empty workspace or with small floating windows.
- **Auto-hide** (`auto-hide`): hidden until you push the pointer against the middle of the bottom edge.
- **Always** (`always`): always visible, with windows on top of it.

The mode, the icon size and which monitors get a dock are set in `~/.config/sway-dock/config.toml` (see [Configuration](/en-us/guide/config/)). The dock doesn't show over a fullscreen window.

## The app grid

Press and release `Super` to open the grid, or click the dock button. It shows every installed app, Flatpak and Snap apps included.

- **Search:** just start typing. The search looks at app names, descriptions and keywords, and also finds files in your folders, listed under the grid. A calculation such as `2*21` shows the result, and `Enter` copies it. With `qalc` installed, it also converts units, as in `5 km to mi`.
- **Groups:** the bottom row has **Home**, with every app, and your groups. The first ones are Office, System and Utilities. Create one with **Add group**, and right-click an app to add it to a group or take it out. `Ctrl`+`Page Up` and `Ctrl`+`Page Down` move between groups.
- **Favorites:** right-click an app and choose **Add to favorites**. Favorites sit at the top of Home.
- **Dock:** right-click an app and choose **Pin to the dock**.

`Esc`, a click away from the icons, or launching an app closes the grid.

## The launcher

`Alt`+`Space` opens the launcher, a search box in the middle of the screen with four tabs: apps, open windows, the clipboard history and the web. `Tab` moves between tabs, and `Enter` opens the selected item. `Super`+`` ` `` (the key left of 1) goes straight to the window list. The same shortcut closes the launcher.

In the **Web** tab, what you type becomes a search. A prefix and a space pick the site: `g` Google, `d` DuckDuckGo, `w` Wikipedia, `yt` YouTube, `gt` Google Translate, `cl` Claude and `gpt` ChatGPT. Something that looks like an address, such as `kde.org`, opens directly, and plain text goes to Google. Your text only goes to an AI service (Claude or ChatGPT) when you type the `cl` or `gpt` prefix. You can add your own searches and change the default one in [the launcher settings](/en-us/guide/config/#launcher-searches).

## Switching windows

`Alt`+`Tab` switches windows in the order you used them, as in KDE and GNOME. While you hold `Alt`, a card in the middle of the screen shows the icon, title and workspace of each window. Each `Tab` moves one step, and letting go of `Alt` focuses the selected window, switching workspaces if needed. `Esc` cancels.

A quick tap goes straight back to the window you used before, without showing the card. `Alt`+`Shift`+`Tab` starts from the oldest one.

## Notifications

Notifications pop up in the top right corner and go away after 10 seconds (critical ones stay until you close them). Clicking a notification runs the app's default action.

The bell on the bar gets a dot when there are notifications. Click it, or press `Super`+`C`, to open the notification center: notifications grouped by app, with **Clear** for each group and **Clear all**.

**Do Not Disturb** lives in the notification center: off, for 1 hour, for 2 hours, or until you turn it off. While it's on, only critical notifications pop up; the rest go straight to the center. Right-click the bell to toggle it.

The list only lives in memory: nothing is written to disk, and it's gone when you log out.

## Clipboard history

Swaydesk keeps a history of what you copy: text, images and other content up to 5 MB. `Super`+`V`, or the icon on the bar, opens it.

- Type to search the full text of every item. The arrow keys pick an item, and `Enter` copies it, ready to paste.
- Images show a thumbnail.
- The buttons on each item pin it or delete it from the history. Pinned items stay at the top and survive clearing the history.
- **Clear history** asks you to click again to confirm.

## Session menu

`Ctrl`+`Alt`+`Delete`, or the power button on the bar, opens the session menu in the middle of the screen: **Lock**, **Log out**, **Suspend**, **Restart** and **Shut down**, also on the `L`, `E`, `S`, `R` and `P` keys. The arrow keys and `Tab` move between buttons, and `Esc` or a click outside closes the menu. There's no confirmation: clicking **Shut down** shuts down. When an app asks to restart or shut down, such as the store's **Restart & Update**, Swaydesk asks first, with a 60-second countdown and a button to cancel; cancelling installs nothing and the update stays downloaded.

## Lock screen and idle

`Ctrl`+`Alt`+`L` locks the screen. The lock screen shows the time and date over a blurred copy of your wallpaper, with a password field on every monitor. On the main monitor, it also shows the battery, the network, the keyboard layout (click to switch) and whatever media is playing.

This lock screen needs gtk4-layer-shell 1.2 or newer. On a system with an older version, such as Debian 13, its GTK 3 version runs instead, with the same look. If a lock screen stops without unlocking, another one takes over, with gtklock as the last resort, so the desktop never shows in between; if none can start, a critical notification says the screen isn't locked.

The password field never goes through an input method, so a password with accents typed with dead keys unlocks it. After three wrong passwords, the lock screen makes you wait a few seconds, with a countdown. On Arch, the system also locks the account for 10 minutes after three failed logins: see the [FAQ](/en-us/guide/faq/#account-locked).

When you're away, the computer:

- locks the screen after 10 minutes;
- turns the screen off after 15 minutes;
- suspends after 30 minutes, only on battery and only if no sound is playing.

It also locks before suspending. Caffeine, on the bar, holds all of this off while it's on. If the screen stays dark after turning off, `Super`+`Shift`+`O` turns it back on, even while locked.

## Screenshots and recording

`Print` captures a region, and there are shortcuts for the whole screen and for a window. Screenshots go to `~/Pictures/Screenshots`, to the clipboard, and show up in a notification. If Gradia is installed, you can open the screenshot in it to annotate.

`Super`+`Shift`+`E` opens the screenshot panel and `Super`+`Shift`+`R` the recording panel, with options for a delay and for sound. While recording, the bar shows the elapsed time in red; click it, or press the shortcut again, to stop. Videos go to `~/Videos/Screencasts`. The panel keys are on the [shortcuts](/en-us/shortcuts/) page.

## Screen sharing

Screen sharing works through the portal, like on other desktops. When an app, such as your browser during a call, asks to share the screen, the pointer turns into crosshairs: click the monitor you want to show.

Chromium-based browsers open a "… is sharing your screen" bar whose buttons don't respond under Sway. Swaydesk tucks it away; to stop sharing, use the button on the web page itself. `Super`+`Z` brings the bar back if you need it.

## Passwords and keyring

- **Keyring:** gnome-keyring stores the passwords of your browser, Git and other apps, and unlocks when you log in. If the first login created it without unlocking it, Swaydesk asks for your password once, and later logins unlock it on their own.
- **Administrator actions:** when an app needs permission, for example to mount a disk, a window asks for your password. It comes from the polkit agent; if none is installed, a notification tells you.
- **Wi-Fi passwords:** with NetworkManager, the password window is `nm-applet`'s. With iwd, you type the password of a new network right in the network popup.
