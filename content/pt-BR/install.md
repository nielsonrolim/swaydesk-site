---
title: Instalar
prompt: "sudo apt install swaydesk-desktop"
crumb: install
description: Como instalar o Swaydesk pelos pacotes, no Debian 13, no Ubuntu 26.04, no Linux Mint 27 e no Arch Linux.
---
Os pacotes do Swaydesk vêm de um repositório no [Open Build Service](https://build.opensuse.org/), assinado com a chave do projeto. O desktop que você já tem continua na tela de login, e as atualizações chegam com o `apt upgrade` ou o `pacman -Syu` de sempre.

## O que você vai precisar

- Debian 13, Ubuntu 26.04, Linux Mint 27 ou Arch Linux, de 64 bits (x86_64), com ou sem outro desktop instalado.
- Uma placa de vídeo Intel, AMD ou NVIDIA com driver para Wayland.

## A chave do repositório

Confira que a chave baixada tem esta impressão digital, antes de confiar nela:

```
71A5 E6CB 39B9 844E 42CE  42D3 5815 F0B6 5BE1 CFB9
```

É uma chave RSA de 4096 bits, a do projeto no OBS, válida até 23/01/2029.

## Debian 13, Ubuntu 26.04 e Linux Mint 27

No Ubuntu e no Mint, troque `Debian_13` por `xUbuntu_26.04` na primeira linha.

```
repo=https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13
key=$(mktemp) && curl -fsSL "$repo/Release.key" -o "$key" &&
gpg --show-keys --with-colons "$key" | grep -q '^fpr:::::::::71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9:$' &&
sudo install -m644 "$key" /usr/share/keyrings/swaydesk-archive-keyring.asc &&
printf 'Types: deb\nURIs: %s/\nSuites: ./\nSigned-By: /usr/share/keyrings/swaydesk-archive-keyring.asc\n' "$repo" |
  sudo tee /etc/apt/sources.list.d/swaydesk.sources >/dev/null &&
sudo apt update && sudo apt install swaydesk-archive-keyring swaydesk-desktop
```

Os comandos vão em cadeia: se a chave baixada não tiver a impressão digital de cima, nada é instalado. Daí em diante, o pacote `swaydesk-archive-keyring` cuida da chave e do repositório e os mantém atualizados.

## Arch Linux

Acrescente ao `/etc/pacman.conf`:

```
[home_nielsonrolim_Arch]
Server = https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/$arch
```

Depois importe a chave e instale. O `--lsign-key` com a impressão digital inteira só aceita a chave certa:

```
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key | sudo pacman-key --add -
sudo pacman-key --finger 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9
sudo pacman-key --lsign-key 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9
sudo pacman -Syu swaydesk-desktop
```

## Depois de instalar

Saia da sessão e, na tela de login que você já usa, escolha a sessão **Sway Desktop**. Os [primeiros passos](/pt-br/guide/first-steps/) mostram o resto.

Quer também a tela de login do Swaydesk? Ela é opcional: instale o pacote `swaydesk-greeter` (no Arch, ligue depois o greetd com `sudo systemctl enable greetd`). Veja [como ela funciona e como voltar à tela anterior](/pt-br/guide/first-steps/#opcional-a-tela-de-login-do-swaydesk).

## Os pacotes

| Pacote | O que traz |
| --- | --- |
| `swaydesk-desktop` | A sessão completa, "Sway Desktop" na tela de login, com todos os componentes |
| `swaydesk-greeter` | Opcional: a tela de login do Swaydesk, sobre o greetd |
| `swaydesk-archive-keyring` | Só no Debian, no Ubuntu e no Mint: a chave e o repositório, sempre em dia |

Os pacotes ainda são retratos do desenvolvimento (versões `0.1.0~git…`) até o lançamento da 0.1.0.
