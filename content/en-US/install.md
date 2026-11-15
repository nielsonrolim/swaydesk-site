---
title: Install
prompt: "sudo apt install swaydesk-desktop"
crumb: install
description: How to install Swaydesk from the packages, on Debian 13, Ubuntu 26.04, Linux Mint 27 and Arch Linux.
---
Swaydesk's packages come from a repository on the [Open Build Service](https://build.opensuse.org/), signed with the project's key. The desktop you already have stays on the login screen, and updates come with your usual `apt upgrade` or `pacman -Syu`.

## What you need

- Debian 13, Ubuntu 26.04, Linux Mint 27 or Arch Linux, 64-bit (x86_64), with or without another desktop.
- An Intel, AMD or NVIDIA graphics card with a Wayland driver.

## The repository key

Check that the key you download has this fingerprint before you trust it:

```
71A5 E6CB 39B9 844E 42CE  42D3 5815 F0B6 5BE1 CFB9
```

It's a 4096-bit RSA key, the project's key on OBS, valid until 2029-01-23.

## Debian 13, Ubuntu 26.04 and Linux Mint 27

On Ubuntu and Mint, replace `Debian_13` with `xUbuntu_26.04` in the first line.

```
repo=https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13
curl -fsSL "$repo/Release.key" | sudo tee /usr/share/keyrings/swaydesk-archive-keyring.asc >/dev/null
gpg --show-keys /usr/share/keyrings/swaydesk-archive-keyring.asc
printf 'Types: deb\nURIs: %s/\nSuites: ./\nSigned-By: /usr/share/keyrings/swaydesk-archive-keyring.asc\n' "$repo" \
  | sudo tee /etc/apt/sources.list.d/swaydesk.sources >/dev/null
sudo apt update
sudo apt install swaydesk-archive-keyring swaydesk-desktop
```

`gpg --show-keys` prints the fingerprint: it must be the one above. From then on, the `swaydesk-archive-keyring` package takes care of the key and the repository and keeps them up to date.

## Arch Linux

Add to `/etc/pacman.conf`:

```
[home_nielsonrolim_Arch]
Server = https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/$arch
```

Then import the key, check the fingerprint and install:

```
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key | sudo pacman-key --add -
sudo pacman-key --finger 5815F0B65BE1CFB9
sudo pacman-key --lsign-key 5815F0B65BE1CFB9
sudo pacman -Syu swaydesk-desktop
```

## After installing

Log out and pick the **Sway Desktop** session on the login screen you already use. The [first steps](/en-us/guide/first-steps/) cover the rest.

Want Swaydesk's own login screen too? It's optional: install the `swaydesk-greeter` package (on Arch, then enable greetd with `sudo systemctl enable greetd`). See [how it works and how to go back](/en-us/guide/first-steps/#optional-the-swaydesk-login-screen).

## The packages

| Package | What it brings |
| --- | --- |
| `swaydesk-desktop` | The full session, "Sway Desktop" on the login screen, with every component |
| `swaydesk-greeter` | Optional: Swaydesk's login screen, on top of greetd |
| `swaydesk-archive-keyring` | Debian, Ubuntu and Mint only: the key and the repository, kept up to date |

The packages are development snapshots (`0.1.0~git…` versions) until the 0.1.0 release.
