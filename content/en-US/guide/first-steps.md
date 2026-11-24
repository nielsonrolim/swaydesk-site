---
title: First steps
prompt: "swaydesk-desktop-config setup"
crumb: guide/first-steps
weight: 1
description: How to log in to the Swaydesk session and what to do the first time.
---
Once the packages are installed, Swaydesk shows up as one more session on the login screen. The desktop you already had stays there, and the two keep their settings apart.

## Logging in

If you already use a login screen, such as GNOME's (GDM), KDE's (SDDM) or Mint's and Xfce's (LightDM), **there's nothing to do but pick the session**. Swaydesk shows up there as one more option, and the desktop you already had stays:

- **GDM:** click your name and, before typing the password, the gear icon in the bottom right corner;
- **SDDM:** use the session menu in the bottom left corner;
- **LightDM:** use the session icon or menu (on Mint, next to your name; in other themes, on the top panel).

Pick **Sway Desktop** and enter your password. The login screen remembers the choice for next time. If you also see a session called just **Sway**, that one comes from the Sway package and has none of Swaydesk: use **Sway Desktop**.

### The Swaydesk login screen

Swaydesk also has a login screen of its own, the `swaydesk-greeter` package, with the same look as the lock screen. With GDM, SDDM or LightDM it's optional. Without a display manager, as on a minimal or server install, the system starts in a text console, and this is what gives you a graphical login. What it does:

- it lists the accounts on the machine with their pictures, plus **Other user…** to type a name;
- it remembers the last account and each person's session, with **Sway Desktop** at the top of the list;
- after the password, it asks whatever else the system needs, such as a code or a new password when the old one has expired;
- it uses the system keyboard layout and language, and has suspend, restart and shut down buttons.

It runs on top of greetd. On Debian and Ubuntu, greetd only turns itself on when the machine has no other login screen; with GDM, SDDM or LightDM, nothing changes until you switch:

```
sudo apt install swaydesk-greeter
sudo systemctl disable gdm      # or sddm, or lightdm
sudo systemctl enable greetd
```

On Arch, pacman doesn't enable services: after installing, run `sudo systemctl enable greetd`. On every distro, the sessions you open from this login screen use the package's own PAM service, `/etc/pam.d/swaydesk-greeter`, which also unlocks your keyring when you log in. If you customized `/etc/pam.d/greetd` (a fingerprint reader, a security key), make that change in `/etc/pam.d/swaydesk-greeter`.

To go back to the login screen you had, disable greetd and enable the other one (`sudo systemctl disable greetd` and `sudo systemctl enable gdm`, for example). See also the [FAQ](/en-us/guide/faq/#how-do-i-go-back-to-the-login-screen-i-used-before).

## What you'll see

- **The bar at the top:** workspaces 1 to 9 on the left, the weather and the clock in the middle, and on the right the tray, clipboard, keyboard layout, system, brightness, caffeine, Bluetooth, network, volume and battery icons, plus the power button. Click any icon to open its popup.
- **The dock at the bottom:** your pinned apps, the open ones, and the app grid button. It slides away when a window needs its space and comes back when you push the pointer against the middle of the bottom edge.
- **The app grid:** press and release `Super` (the logo key) to show or hide every installed app, with search.

The shortcuts follow the Swaydesk scheme, inspired by KDE Plasma with Krohnkite, and you can switch them to the i3, Hyprland, niri or dwm keys. The full list, profile by profile, is on the [shortcuts](/en-us/shortcuts/) page, and there's a tour of each piece in [The desktop](/en-us/guide/desktop/).

## What the first login sets up

The first time you log in, the session copies into your home folder whatever files you don't have yet. It never overwrites anything, and what it copies is yours to edit:

- `~/.config/swaydesk/config.toml`, the desktop settings: language, theme, icons and accent color. If the default theme isn't installed, it starts with `Adwaita-dark`;
- `~/.config/sway/config.d/50-local.conf`, the settings for this machine, with commented examples and the system keyboard layout;
- the first set of apps pinned to the dock: the file manager and the terminal.

It also applies the theme and the accent color to GTK apps, the bar, the dock and the popups. See [Configuration](/en-us/guide/config/) for the details.

**The keyring on Debian 13:** on each user's first login, a notice ("First login: type your password once to turn on the keyring. From the next login on, it opens by itself.") is followed by the keyring password prompt (**Unlock Login Keyring**). Type your login password. It happens only once: from the next login on, the keyring opens by itself. This is a limitation of gnome-keyring 48 in Debian; Ubuntu 26.04 and Arch are not affected.

## First things to do

- **Theme and accent color:** open the **Desktop Theme** app from the app grid. Pick a theme family, light or dark, and a color; **Apply** changes everything at once, and the window stays open so you can try another combination.
- **Displays:** open the **Displays** app from the app grid to set the position, resolution and scale of your screens. Each set of monitors keeps your choice, which comes back by itself when you plug in the same screens.
- **Keyboard:** Swaydesk starts with the system layout. To use two layouts, say US and US International, edit `50-local.conf` (see [Configuration](/en-us/guide/config/)). `Super`+`Space` switches between them, and the keyboard icon on the bar shows the current one.
- **Wi-Fi:** click the network icon on the bar, pick the network and type the password.
- **Bluetooth:** click the Bluetooth icon, turn it on and search to pair a new device.
- **Sound:** click the volume icon to choose the output and the microphone.
