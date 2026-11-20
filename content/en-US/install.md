---
title: Install
prompt: "sudo apt install swaydesk-desktop"
crumb: install
description: How to install Swaydesk from the packages, on Debian 13 and testing, Ubuntu 26.04, Linux Mint 27 and Arch Linux.
---
The packages come from a repository on the [Open Build Service](https://build.opensuse.org/), signed with the project's key. The desktop you already have stays on the login screen, and updates come with your usual `apt upgrade` or `pacman -Syu`.

You need Debian 13 or testing, Ubuntu 26.04, Linux Mint 27 or Arch Linux, 64-bit (x86_64), and an Intel, AMD or NVIDIA graphics card with a Wayland driver. Pick your distribution and run one step at a time:

{{< distros >}}
{{< distro id="debian" name="Debian 13" >}}
{{< steps >}}
{{< step text="Install `curl`, which downloads the repository package." >}}
sudo apt install curl
{{< /step >}}
{{< step text="Download the `swaydesk-archive-keyring` package: it adds the repository and the project's key." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13/all/swaydesk-archive-keyring_2026.11.20_all.deb -o ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Check the downloaded file. The command must print `OK`; if it doesn't, stop here, delete the file and don't go on." >}}
echo "2527bebb378c926e631fb367f2ccb18120cea26617c3a90b859c633cb2845700  $HOME/swaydesk-archive-keyring_2026.11.20_all.deb" | sha256sum -c
{{< /step >}}
{{< step text="Install it. It puts the key in `/usr/share/keyrings/` and the repository in `/etc/apt/sources.list.d/swaydesk.sources`, and from then on keeps both up to date." >}}
sudo dpkg -i ~/swaydesk-archive-keyring_2026.11.20_all.deb && rm ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Optional, before step 6: see the installed key's fingerprint (needs `gpg`: `sudo apt install gpg`)." fpr="installed" >}}
gpg --show-keys /usr/share/keyrings/swaydesk-archive-keyring.asc
{{< /step >}}
{{< step text="Update the package list and install Swaydesk." >}}
sudo apt update && sudo apt install swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="After step 1 (curl), the other steps chained: if the downloaded file isn't the expected one, nothing gets installed." >}}
deb=swaydesk-archive-keyring_2026.11.20_all.deb
dir=$(mktemp -d) && curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13/all/$deb -o "$dir/$deb" &&
echo "2527bebb378c926e631fb367f2ccb18120cea26617c3a90b859c633cb2845700  $dir/$deb" | sha256sum -c && sudo dpkg -i "$dir/$deb" && rm -r "$dir" &&
sudo apt update && sudo apt install swaydesk-desktop
{{< /oneline >}}
{{< /distro >}}
{{< distro id="debian-testing" name="Debian testing" >}}
<p class="distro__note">Debian testing is best effort: during a library transition in testing the packages can break for a few days, until a new revision.</p>
{{< steps >}}
{{< step text="Install `curl`, which downloads the repository package." >}}
sudo apt install curl
{{< /step >}}
{{< step text="Download the `swaydesk-archive-keyring` package: it adds the repository and the project's key." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_Testing/all/swaydesk-archive-keyring_2026.11.20_all.deb -o ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Check the downloaded file. The command must print `OK`; if it doesn't, stop here, delete the file and don't go on." >}}
echo "0fa0971606384baf62a634376006c5b01e52a095795f88c730dc8e07104cb664  $HOME/swaydesk-archive-keyring_2026.11.20_all.deb" | sha256sum -c
{{< /step >}}
{{< step text="Install it. It puts the key in `/usr/share/keyrings/` and the repository in `/etc/apt/sources.list.d/swaydesk.sources`, and from then on keeps both up to date." >}}
sudo dpkg -i ~/swaydesk-archive-keyring_2026.11.20_all.deb && rm ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Optional, before step 6: see the installed key's fingerprint (needs `gpg`: `sudo apt install gpg`)." fpr="installed" >}}
gpg --show-keys /usr/share/keyrings/swaydesk-archive-keyring.asc
{{< /step >}}
{{< step text="Update the package list and install Swaydesk." >}}
sudo apt update && sudo apt install swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="After step 1 (curl), the other steps chained: if the downloaded file isn't the expected one, nothing gets installed." >}}
deb=swaydesk-archive-keyring_2026.11.20_all.deb
dir=$(mktemp -d) && curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_Testing/all/$deb -o "$dir/$deb" &&
echo "0fa0971606384baf62a634376006c5b01e52a095795f88c730dc8e07104cb664  $dir/$deb" | sha256sum -c && sudo dpkg -i "$dir/$deb" && rm -r "$dir" &&
sudo apt update && sudo apt install swaydesk-desktop
{{< /oneline >}}
{{< /distro >}}
{{< distro id="ubuntu" name="Ubuntu 26.04 / Mint 27" >}}
{{< steps >}}
{{< step text="Install `curl`, which downloads the repository package." >}}
sudo apt install curl
{{< /step >}}
{{< step text="Download the `swaydesk-archive-keyring` package: it adds the repository and the project's key." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/xUbuntu_26.04/all/swaydesk-archive-keyring_2026.11.20_all.deb -o ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Check the downloaded file. The command must print `OK`; if it doesn't, stop here, delete the file and don't go on." >}}
echo "a34f455e495c69a2c5dd94ff8ce6dd0618ec569d6b010010c2360432f6029020  $HOME/swaydesk-archive-keyring_2026.11.20_all.deb" | sha256sum -c
{{< /step >}}
{{< step text="Install it. It puts the key in `/usr/share/keyrings/` and the repository in `/etc/apt/sources.list.d/swaydesk.sources`, and from then on keeps both up to date." >}}
sudo dpkg -i ~/swaydesk-archive-keyring_2026.11.20_all.deb && rm ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Optional, before step 6: see the installed key's fingerprint (needs `gpg`: `sudo apt install gpg`)." fpr="installed" >}}
gpg --show-keys /usr/share/keyrings/swaydesk-archive-keyring.asc
{{< /step >}}
{{< step text="Update the package list and install Swaydesk." >}}
sudo apt update && sudo apt install swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="After step 1 (curl), the other steps chained: if the downloaded file isn't the expected one, nothing gets installed." >}}
deb=swaydesk-archive-keyring_2026.11.20_all.deb
dir=$(mktemp -d) && curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/xUbuntu_26.04/all/$deb -o "$dir/$deb" &&
echo "a34f455e495c69a2c5dd94ff8ce6dd0618ec569d6b010010c2360432f6029020  $dir/$deb" | sha256sum -c && sudo dpkg -i "$dir/$deb" && rm -r "$dir" &&
sudo apt update && sudo apt install swaydesk-desktop
{{< /oneline >}}
{{< /distro >}}
{{< distro id="arch" name="Arch Linux" >}}
{{< steps >}}
{{< step text="Add the repository to the end of `/etc/pacman.conf` (only once)." >}}
sudo tee -a /etc/pacman.conf <<'EOF'

[home_nielsonrolim_Arch]
Server = https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/$arch
EOF
{{< /step >}}
{{< step text="Download the repository key." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key -o ~/swaydesk.key
{{< /step >}}
{{< step text="Show the downloaded key's fingerprint." fpr="plain" >}}
gpg --show-keys ~/swaydesk.key
{{< /step >}}
{{< step text="Add the key to pacman's keyring and sign it locally, so pacman trusts it. The command checks the key again first and refuses any other, as in step 3." >}}
[ "$(gpg --show-keys --with-colons ~/swaydesk.key | grep -E '^(pub|sub|fpr):' | cut -d: -f1,10 | tr '\n' ' ')" = 'pub: fpr:71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 ' ] &&
sudo pacman-key --add ~/swaydesk.key &&
sudo pacman-key --lsign-key 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 &&
rm ~/swaydesk.key
{{< /step >}}
{{< step text="Install Swaydesk. If you already have `jack2`, pacman asks whether to replace it with `pipewire-jack`, the JACK of PipeWire, which Swaydesk uses: answer y." >}}
sudo pacman -Syu swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="The same steps, chained: if the downloaded key doesn't have the right fingerprint, nothing gets added or installed." >}}
key=$(mktemp) && curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key -o "$key" &&
[ "$(gpg --show-keys --with-colons "$key" | grep -E '^(pub|sub|fpr):' | cut -d: -f1,10 | tr '\n' ' ')" = 'pub: fpr:71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 ' ] &&
sudo pacman-key --add "$key" && rm -f "$key" &&
sudo pacman-key --lsign-key 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 &&
printf '\n[home_nielsonrolim_Arch]\nServer = https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/$arch\n' | sudo tee -a /etc/pacman.conf >/dev/null &&
sudo pacman -Syu swaydesk-desktop
{{< /oneline >}}
<p class="distro__note">On Arch, the Swaydesk update notice covers the repositories, the AUR, Flatpak apps and firmware, so the store’s updates part comes turned off. <a href="/en-us/guide/config/#updates-on-arch">How to change that</a>.</p>
{{< /distro >}}
{{< /distros >}}

## After installing

Log out and pick **Sway Desktop** on the login screen you already use. The [first steps](/en-us/guide/first-steps/) cover the rest.

Swaydesk's own login screen is optional: see [how to install it and how to go back](/en-us/guide/first-steps/#optional-the-swaydesk-login-screen).

## The packages

| Package | What it brings |
| --- | --- |
| `swaydesk-desktop` | The full session, "Sway Desktop" on the login screen, with every component |
| `swaydesk-greeter` | Optional: Swaydesk's login screen, on top of greetd |
| `swaydesk-archive-keyring` | Debian, Ubuntu and Mint only: the key and the repository, kept up to date |

The packages are version 0.1.2, stable: see the [release notes](https://github.com/nielsonrolim/swaydesk/releases/tag/v0.1.2) and the [changelog](https://github.com/nielsonrolim/swaydesk/blob/main/CHANGELOG.md). New versions come as updates.
