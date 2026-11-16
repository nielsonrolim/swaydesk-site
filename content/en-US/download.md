---
title: Download
prompt: "sha256sum -c swaydesk.iso.sha256"
crumb: download
description: Swaydesk's live ISOs for Debian 13, Ubuntu 26.04 and Arch Linux, with an installer.
---
Each ISO boots a live Swaydesk session: try it without touching the disk and, if you like it, install it with the **Install Swaydesk** icon in the dock. Already have Debian 13, Ubuntu 26.04, Linux Mint 27 or Arch? Then you don't need an ISO: [install the packages](/en-us/install/) on the system you have.

## Requirements

- A 64-bit PC (x86_64), with UEFI or BIOS
- 2 GB of RAM
- 20 GB of disk
- An Intel, AMD or NVIDIA graphics card with a Wayland driver

## The ISOs

{{< isos >}}
{{< iso id="debian" >}}
Debian 13 with Swaydesk.
{{< /iso >}}
{{< iso id="ubuntu" >}}
Ubuntu 26.04 with Swaydesk, without telemetry. It keeps the Ubuntu Pro client without its ads: Ubuntu Pro (extended security updates for universe, free for personal use on up to 5 machines) is off until you run `sudo pro attach`.
{{< /iso >}}
{{< iso id="arch" >}}
Arch Linux with Swaydesk. Turn Secure Boot off in the firmware settings before booting it.
{{< /iso >}}
{{< /isos >}}

## Writing it to a USB stick

The ISO is written as it is, byte for byte, to the whole stick, and **everything on the stick is erased**. Copying the file onto the stick doesn't work.

On Linux, find the stick's name with `lsblk` (such as `/dev/sdb`; never a partition such as `/dev/sdb1`, and check the size so you don't pick your disk), then:

```
sudo dd if=swaydesk-debian13-amd64.hybrid.iso of=/dev/sdX bs=4M status=progress oflag=sync
```

On Windows or macOS, [balenaEtcher](https://etcher.balena.io/) does the same with a window: choose the ISO, the stick, and write. [Rufus](https://rufus.ie/), on Windows, works too: when it asks, pick **DD image** mode.

## Booting and installing

1. Plug the stick in and turn the computer on with the boot menu key (usually F12, F11, F8 or Esc, depending on the maker) and pick the stick.
2. The live session starts on its own, with no password and no automatic lock.
3. The **Install Swaydesk** icon in the dock opens the installer. It picks the time zone from your IP address (when there is no network, America/Sao_Paulo; you can change it), and it has a box for proprietary codecs and drivers, off by default. That box needs a network during the installation; without one, the installed system reminds you at login and you can run `sudo swaydesk-extras` later.

**Secure Boot:** the Debian and Ubuntu ISOs boot with it on. With Secure Boot on, the Debian installer doesn't install the NVIDIA driver (its module isn't signed): turn Secure Boot off, or enroll a MOK key, and run `sudo swaydesk-extras`. The Arch ISO needs Secure Boot off.

After installing, the [first steps](/en-us/guide/first-steps/) cover the rest. The ISOs and the packages are version 0.1.0.
