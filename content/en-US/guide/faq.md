---
title: FAQ
prompt: "less ~/.local/state/sway/sway.log"
crumb: guide/faq
weight: 4
description: Known problems and what to do about each one.
---
## Session and login

### Logging in takes me back to the login screen, or the screen goes black

Log in to your other session (GNOME, KDE or whatever you have) and look for the error in `~/.local/state/sway/sway.log`. The log from the previous attempt is next to it, in `sway.log.old`.

### The login screen shows both "Sway" and "Sway Desktop". Which one do I pick?

**Sway Desktop**. The **Sway** session comes from the Sway package and starts plain Sway, without the environment Swaydesk sets up.

### How do I go back to the login screen I used before?

Without removing the `swaydesk-greeter` package:

```
sudo mkdir -p /etc/systemd/system/greetd.service.d
sudo ln -s /dev/null /etc/systemd/system/greetd.service.d/swaydesk-greeter.conf
sudo systemctl daemon-reload
```

greetd goes back to `/etc/greetd/config.toml` on the next boot. If you used GDM or SDDM, disable greetd and enable the other one again with `systemctl`.

### The session asked for my keyring password on the first login. Is that normal?

Yes, once, on Debian 13. Its gnome-keyring 48 creates the keyring on the first login but doesn't make it available to apps; Swaydesk reopens it, and to do that it shows a notice and asks for your login password once. After that, the keyring unlocks on its own. Ubuntu 26.04 and Arch don't ask. See [the first steps](/en-us/guide/first-steps/#what-the-first-login-sets-up).

## Screen and power

### The screen stays black after turning off when idle

Press `Super`+`Shift`+`O`: it turns the screens back on, even while locked.

### The brightness keys do nothing

Add your user to the `video` group and log in again:

```
sudo usermod -aG video $USER
```

### The lock screen is very plain, just the wallpaper

That's swaylock. Swaydesk's lock screen needs gtk4-layer-shell 1.2 or newer; with an older version, such as Debian 13's, swaylock locks the screen instead. It also takes over if Swaydesk's lock screen fails, so the screen never ends up unlocked.

### The dock doesn't show up

In the default mode, it hides when a window needs its space. Push the pointer against the middle of the bottom edge to bring it up. It doesn't show over a fullscreen window. To keep it visible all the time, set `mode = "always"` in the [dock settings](/en-us/guide/config/).

## Network, Bluetooth and passwords

### A network with a password won't connect, and nothing asks for the password

With NetworkManager, `nm-applet` asks for the password. Install the `network-manager-applet` package and log in again.

With iwd, you type the password of a new network in the network popup, which has to stay open until it connects.

### Pairing a Bluetooth device fails, or no window shows up

blueman shows the pairing code. Install the `blueman` package and log in again.

### An app asked for an administrator password and nothing showed up

A polkit agent is missing, and the session tells you so with a notification. Install `mate-polkit` and log in again.

### VS Code says "An OS keyring couldn't be identified"

VS Code doesn't recognize Sway and can't find the keyring on its own. Don't accept the weaker encryption it offers. Instead, add this line to `~/.vscode/argv.json` and restart VS Code:

```
"password-store": "gnome-libsecret"
```

## Apps and appearance

### Screen sharing has nothing to choose from

Restart the portal, or log out and back in:

```
systemctl --user restart xdg-desktop-portal
```

When an app asks for the screen, the pointer turns into crosshairs: click the monitor you want to share.

### The browser's "… is sharing your screen" bar ignores clicks

The buttons on that bar in Chromium-based browsers don't work under Sway, so Swaydesk tucks it away. Stop sharing with the button on the web page itself. `Super`+`Z` brings the bar back.

### A Flatpak app looks blurry

It's running through XWayland. Use Flatseal to give it the Wayland permission (`--socket=wayland`).

### Qt apps don't follow the theme

Install `qt5ct` and `qt6ct`. Swaydesk sets both up with the GTK theme colors and your accent color.

### The Desktop Theme app says the configured theme isn't installed

In the meantime, the session uses `Adwaita-dark`. Pick a theme in the app and apply it, and the warning goes away.

### I changed the file manager, but the dock still has the old one

The dock doesn't swap pinned apps on its own. Unpin the old one with a right-click on the dock, and pin the new one with a right-click in the app grid.

### The calendar shows no holidays

Holidays come from the `python3-holidays` package, for the country in the `holidays` key or, without it, the country of your language. Check that the package is installed and that the country is right in the [configuration](/en-us/guide/config/).

### Text or the clock is in the wrong language

Set `locale` in the [desktop settings](/en-us/guide/config/) and log in again. The language has to be generated on the system: `locale -a` lists the ones that are.

### The weather is for a different city

By default, the city comes from your IP address. Set `weather_location` in the [desktop settings](/en-us/guide/config/) and log in again. The old forecast may stick around for up to 15 minutes.

### The notification bell turned red

The notification service isn't responding, and notifications are getting lost. It usually comes back by itself within a second. If it doesn't, check whether another notification service, such as mako or dunst, is running in the session: only one can work at a time.
