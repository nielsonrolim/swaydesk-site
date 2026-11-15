---
title: Install
prompt: "sudo apt install swaydesk-desktop"
crumb: install
description: How to install Swaydesk from the packages, on Debian 13, Ubuntu 26.04, Linux Mint 27 and Arch Linux.
---
The packages come from a repository on the [Open Build Service](https://build.opensuse.org/), signed with the project's key. The desktop you already have stays on the login screen, and updates come with your usual `apt upgrade` or `pacman -Syu`.

You need Debian 13, Ubuntu 26.04, Linux Mint 27 or Arch Linux, 64-bit (x86_64), and an Intel, AMD or NVIDIA graphics card with a Wayland driver. Pick your distribution and run one step at a time:

{{< distros >}}
{{< distro id="debian" name="Debian 13" >}}
{{< steps >}}
{{< step text="Install `curl` and `gpg`, which download and check the key." >}}
sudo apt install curl gpg
{{< /step >}}
{{< step text="Download the repository key." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13/Release.key -o ~/swaydesk.key
{{< /step >}}
{{< step text="Show the downloaded key's fingerprint." fpr="plain" >}}
gpg --show-keys ~/swaydesk.key
{{< /step >}}
{{< step text="Install the key where apt looks for it. The command checks the fingerprint again and refuses any other key." >}}
[ "$(gpg --show-keys --with-colons ~/swaydesk.key | grep -c '^pub:')" = 1 ] &&
gpg --show-keys --with-colons ~/swaydesk.key | grep -q '^fpr:::::::::71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9:$' &&
sudo install -m644 ~/swaydesk.key /usr/share/keyrings/swaydesk-archive-keyring.asc &&
rm ~/swaydesk.key
{{< /step >}}
{{< step text="Add the repository." >}}
sudo tee /etc/apt/sources.list.d/swaydesk.sources <<'EOF'
Types: deb
URIs: https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13/
Suites: ./
Signed-By: /usr/share/keyrings/swaydesk-archive-keyring.asc
EOF
{{< /step >}}
{{< step text="Update the package list." >}}
sudo apt update
{{< /step >}}
{{< step text="Install Swaydesk. From then on, the `swaydesk-archive-keyring` package takes care of the key and the repository." >}}
sudo apt install swaydesk-archive-keyring swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="After step 1 (curl and gpg), the other steps chained: if the downloaded key doesn't have the right fingerprint, nothing gets installed." >}}
repo=https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13
key=$(mktemp) && curl -fsSL "$repo/Release.key" -o "$key" &&
[ "$(gpg --show-keys --with-colons "$key" | grep -c '^pub:')" = 1 ] &&
gpg --show-keys --with-colons "$key" | grep -q '^fpr:::::::::71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9:$' &&
sudo install -m644 "$key" /usr/share/keyrings/swaydesk-archive-keyring.asc &&
printf 'Types: deb\nURIs: %s/\nSuites: ./\nSigned-By: /usr/share/keyrings/swaydesk-archive-keyring.asc\n' "$repo" |
  sudo tee /etc/apt/sources.list.d/swaydesk.sources >/dev/null &&
sudo apt update && sudo apt install swaydesk-archive-keyring swaydesk-desktop
{{< /oneline >}}
{{< /distro >}}
{{< distro id="ubuntu" name="Ubuntu 26.04 / Mint 27" >}}
{{< steps >}}
{{< step text="Install `curl` and `gpg`, which download and check the key." >}}
sudo apt install curl gpg
{{< /step >}}
{{< step text="Download the repository key." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/xUbuntu_26.04/Release.key -o ~/swaydesk.key
{{< /step >}}
{{< step text="Show the downloaded key's fingerprint." fpr="plain" >}}
gpg --show-keys ~/swaydesk.key
{{< /step >}}
{{< step text="Install the key where apt looks for it. The command checks the fingerprint again and refuses any other key." >}}
[ "$(gpg --show-keys --with-colons ~/swaydesk.key | grep -c '^pub:')" = 1 ] &&
gpg --show-keys --with-colons ~/swaydesk.key | grep -q '^fpr:::::::::71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9:$' &&
sudo install -m644 ~/swaydesk.key /usr/share/keyrings/swaydesk-archive-keyring.asc &&
rm ~/swaydesk.key
{{< /step >}}
{{< step text="Add the repository." >}}
sudo tee /etc/apt/sources.list.d/swaydesk.sources <<'EOF'
Types: deb
URIs: https://download.opensuse.org/repositories/home:/nielsonrolim/xUbuntu_26.04/
Suites: ./
Signed-By: /usr/share/keyrings/swaydesk-archive-keyring.asc
EOF
{{< /step >}}
{{< step text="Update the package list." >}}
sudo apt update
{{< /step >}}
{{< step text="Install Swaydesk. From then on, the `swaydesk-archive-keyring` package takes care of the key and the repository." >}}
sudo apt install swaydesk-archive-keyring swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="After step 1 (curl and gpg), the other steps chained: if the downloaded key doesn't have the right fingerprint, nothing gets installed." >}}
repo=https://download.opensuse.org/repositories/home:/nielsonrolim/xUbuntu_26.04
key=$(mktemp) && curl -fsSL "$repo/Release.key" -o "$key" &&
[ "$(gpg --show-keys --with-colons "$key" | grep -c '^pub:')" = 1 ] &&
gpg --show-keys --with-colons "$key" | grep -q '^fpr:::::::::71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9:$' &&
sudo install -m644 "$key" /usr/share/keyrings/swaydesk-archive-keyring.asc &&
printf 'Types: deb\nURIs: %s/\nSuites: ./\nSigned-By: /usr/share/keyrings/swaydesk-archive-keyring.asc\n' "$repo" |
  sudo tee /etc/apt/sources.list.d/swaydesk.sources >/dev/null &&
sudo apt update && sudo apt install swaydesk-archive-keyring swaydesk-desktop
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
{{< step text="Import the repository key." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key | sudo pacman-key --add -
{{< /step >}}
{{< step text="Show the imported key's fingerprint." fpr="spaced" >}}
sudo pacman-key --finger 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9
{{< /step >}}
{{< step text="Sign the key locally, so pacman trusts it." >}}
sudo pacman-key --lsign-key 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9
{{< /step >}}
{{< step text="Install Swaydesk. The `noto-fonts` and `pipewire-jack` at the end answer, in advance, the two choices pacman would ask about (a font and the JACK provider): Swaydesk already uses Noto, and its audio is PipeWire. If you already have `jack2` and pacman asks whether to remove it, answer y." >}}
sudo pacman -Syu swaydesk-desktop noto-fonts pipewire-jack
{{< /step >}}
{{< /steps >}}
{{< oneline text="The same steps, chained: `--lsign-key` with the full fingerprint only accepts the right key." >}}
printf '\n[home_nielsonrolim_Arch]\nServer = https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/$arch\n' | sudo tee -a /etc/pacman.conf >/dev/null &&
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key | sudo pacman-key --add - &&
sudo pacman-key --lsign-key 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 &&
sudo pacman -Syu swaydesk-desktop noto-fonts pipewire-jack
{{< /oneline >}}
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

The packages are development snapshots (`0.1.0~git…` versions) until the 0.1.0 release.
