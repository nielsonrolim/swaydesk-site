---
title: Download
prompt: "sha256sum -c --ignore-missing SHA256SUMS"
crumb: download
description: Swaydesk's live ISOs, stable version 0.1.2, with an installer.
---
Each ISO boots a live Swaydesk session: try it without touching the disk and, if you like it, install it with the **Install Swaydesk** icon in the dock. These are stable ISOs, version 0.1.2, the same as the packages. Already have Debian 13 or testing, Ubuntu 26.04, Linux Mint 27 or Arch? Then you don't need an ISO: [install the packages](/en-us/install/) on the system you have. Linux Mint 27 has no Swaydesk ISO; there, Swaydesk comes only through the packages.

## Requirements

- A 64-bit PC (x86_64), with UEFI or BIOS
- 2 GB of RAM
- 22 GB of disk
- An Intel, AMD or NVIDIA graphics card with a Wayland driver

## The ISOs

{{< isos >}}
{{< iso id="debian" >}}
Debian 13 with Swaydesk. With Secure Boot on, the installer doesn't install the NVIDIA driver (its module isn't signed): turn Secure Boot off and run `sudo swaydesk-extras`.
{{< /iso >}}
{{< iso id="ubuntu" >}}
Ubuntu 26.04 with Swaydesk, without telemetry. It keeps the Ubuntu Pro client without its ads: Ubuntu Pro (extended security updates for universe, free for personal use on up to 5 machines) is off until you run `sudo pro attach`. The NVIDIA driver comes signed and works with Secure Boot on.
{{< /iso >}}
{{< iso id="arch" >}}
Arch Linux with Swaydesk. Turn Secure Boot off in the firmware settings before booting it. The NVIDIA driver (nvidia-open) is installed only for Turing (GTX 16xx, RTX 20xx) and newer cards; older ones stay on nouveau.
{{< /iso >}}
{{< /isos >}}

## Checking the download

Also download `SHA256SUMS` (the link is next to each ISO) into the same folder as the ISO and, in that folder, run:

```
sha256sum -c --ignore-missing SHA256SUMS
```

It must print the ISO's name followed by `OK`. If it prints `FAILED`, or nothing, delete the ISO and download it again. Each ISO's SHA-256 is also on its card above: it must match the ISO's line in `SHA256SUMS`. This catches a corrupted or incomplete download; it is not a signature (both are published from the same GitHub account).

## Writing it to a USB stick

The ISO is written as it is, byte for byte, to the whole stick, and **everything on the stick is erased**. Copying the file onto the stick doesn't work.

On Linux, find the stick's name with `lsblk` (such as `/dev/sdb`; never a partition such as `/dev/sdb1`, and check the size so you don't pick your disk), then run the command below, with `swaydesk.iso` replaced by the name of the ISO you downloaded and `/dev/sdX` by the stick:

```
sudo dd if=swaydesk.iso of=/dev/sdX bs=4M status=progress oflag=sync
```

On Windows or macOS, [balenaEtcher](https://etcher.balena.io/) does the same with a window: choose the ISO, the stick, and write. [Rufus](https://rufus.ie/), on Windows, works too: when it asks, pick **DD image** mode.

## Booting and installing

1. Plug the stick in and turn the computer on with the boot menu key (usually F12, F11, F8 or Esc, depending on the maker) and pick the stick.
2. The live session starts on its own, with no password and no automatic lock.
3. The **Install Swaydesk** icon in the dock opens the installer. It picks the time zone from your IP address (when there is no network, America/Sao_Paulo; you can change it), and it has a box for proprietary codecs and drivers, off by default. That box needs a network during the installation; without one, the installed system reminds you at login and you can run `sudo swaydesk-extras` later.

Printing and scanning come ready (CUPS, network printers through avahi, and Document Scanner), and so do the manual pages (`man`).

### Next to another system (dual boot)

The installed system's GRUB lists the other systems on the disks. The installer's **Install alongside** option shows only when the disk has room for Swaydesk (22 GB plus a margin), and it shrinks the other system's partition. On a tight disk the installer can misjudge that partition's minimum: the resize fails before anything changes, the data stays as it was, and the installation stops. To avoid that, shrink the other system first, with its own tools, and install into the free space.

After installing, the [first steps](/en-us/guide/first-steps/) cover the rest.
