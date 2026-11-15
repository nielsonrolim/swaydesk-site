---
title: Instalar
prompt: "sudo apt install swaydesk-desktop"
crumb: install
description: Como instalar o Swaydesk pelos pacotes, no Debian 13, no Ubuntu 26.04, no Linux Mint 27 e no Arch Linux.
---
Os pacotes vêm de um repositório no [Open Build Service](https://build.opensuse.org/), assinado com a chave do projeto. O desktop que você já tem continua na tela de login, e as atualizações chegam com o `apt upgrade` ou o `pacman -Syu` de sempre.

Precisa de Debian 13, Ubuntu 26.04, Linux Mint 27 ou Arch Linux, de 64 bits (x86_64), e de uma placa de vídeo Intel, AMD ou NVIDIA com driver para Wayland. Escolha a sua distro e rode um passo por vez:

{{< distros >}}
{{< distro id="debian" name="Debian 13" >}}
{{< steps >}}
{{< step text="Instale o `curl` e o `gpg`, que baixam e conferem a chave." >}}
sudo apt install curl gpg
{{< /step >}}
{{< step text="Baixe a chave do repositório." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13/Release.key -o ~/swaydesk.key
{{< /step >}}
{{< step text="Mostre a impressão digital da chave baixada." fpr="plain" >}}
gpg --show-keys ~/swaydesk.key
{{< /step >}}
{{< step text="Instale a chave no lugar que o apt usa." >}}
sudo install -m644 ~/swaydesk.key /usr/share/keyrings/swaydesk-archive-keyring.asc
{{< /step >}}
{{< step text="Adicione o repositório." >}}
sudo tee /etc/apt/sources.list.d/swaydesk.sources <<'EOF'
Types: deb
URIs: https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13/
Suites: ./
Signed-By: /usr/share/keyrings/swaydesk-archive-keyring.asc
EOF
{{< /step >}}
{{< step text="Atualize a lista de pacotes." >}}
sudo apt update
{{< /step >}}
{{< step text="Instale o Swaydesk. Daqui em diante, o pacote `swaydesk-archive-keyring` cuida da chave e do repositório." >}}
sudo apt install swaydesk-archive-keyring swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="Depois do passo 1 (curl e gpg), os outros passos encadeados: se a chave baixada não tiver a impressão digital certa, nada é instalado." >}}
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
{{< step text="Instale o `curl` e o `gpg`, que baixam e conferem a chave." >}}
sudo apt install curl gpg
{{< /step >}}
{{< step text="Baixe a chave do repositório." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/xUbuntu_26.04/Release.key -o ~/swaydesk.key
{{< /step >}}
{{< step text="Mostre a impressão digital da chave baixada." fpr="plain" >}}
gpg --show-keys ~/swaydesk.key
{{< /step >}}
{{< step text="Instale a chave no lugar que o apt usa." >}}
sudo install -m644 ~/swaydesk.key /usr/share/keyrings/swaydesk-archive-keyring.asc
{{< /step >}}
{{< step text="Adicione o repositório." >}}
sudo tee /etc/apt/sources.list.d/swaydesk.sources <<'EOF'
Types: deb
URIs: https://download.opensuse.org/repositories/home:/nielsonrolim/xUbuntu_26.04/
Suites: ./
Signed-By: /usr/share/keyrings/swaydesk-archive-keyring.asc
EOF
{{< /step >}}
{{< step text="Atualize a lista de pacotes." >}}
sudo apt update
{{< /step >}}
{{< step text="Instale o Swaydesk. Daqui em diante, o pacote `swaydesk-archive-keyring` cuida da chave e do repositório." >}}
sudo apt install swaydesk-archive-keyring swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="Depois do passo 1 (curl e gpg), os outros passos encadeados: se a chave baixada não tiver a impressão digital certa, nada é instalado." >}}
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
{{< step text="Adicione o repositório ao fim do `/etc/pacman.conf`." >}}
sudo tee -a /etc/pacman.conf <<'EOF'

[home_nielsonrolim_Arch]
Server = https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/$arch
EOF
{{< /step >}}
{{< step text="Importe a chave do repositório." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key | sudo pacman-key --add -
{{< /step >}}
{{< step text="Mostre a impressão digital da chave importada." fpr="spaced" >}}
sudo pacman-key --finger 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9
{{< /step >}}
{{< step text="Assine a chave localmente, para o pacman confiar nela." >}}
sudo pacman-key --lsign-key 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9
{{< /step >}}
{{< step text="Instale o Swaydesk." >}}
sudo pacman -Syu swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="Os mesmos passos, encadeados: `--lsign-key` com a impressão digital completa só aceita a chave certa." >}}
printf '\n[home_nielsonrolim_Arch]\nServer = https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/$arch\n' | sudo tee -a /etc/pacman.conf >/dev/null &&
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key | sudo pacman-key --add - &&
sudo pacman-key --lsign-key 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 &&
sudo pacman -Syu swaydesk-desktop
{{< /oneline >}}
{{< /distro >}}
{{< /distros >}}

## Depois de instalar

Saia da sessão e, na tela de login de sempre, escolha **Sway Desktop**. Os [primeiros passos](/pt-br/guide/first-steps/) explicam o resto.

A tela de login do Swaydesk é opcional: veja [como instalar e como voltar](/pt-br/guide/first-steps/#opcional-a-tela-de-login-do-swaydesk).

## Os pacotes

| Pacote | O que traz |
| --- | --- |
| `swaydesk-desktop` | A sessão completa, "Sway Desktop" na tela de login, com todos os componentes |
| `swaydesk-greeter` | Opcional: a tela de login do Swaydesk, sobre o greetd |
| `swaydesk-archive-keyring` | Só Debian, Ubuntu e Mint: a chave e o repositório, sempre em dia |

Os pacotes são versões de desenvolvimento (`0.1.0~git…`) até o lançamento da 0.1.0.
