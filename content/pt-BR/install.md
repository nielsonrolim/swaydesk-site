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
{{< step text="Instale o `curl`, que baixa o pacote do repositório." >}}
sudo apt install curl
{{< /step >}}
{{< step text="Baixe o pacote `swaydesk-archive-keyring`: ele adiciona o repositório e a chave do projeto." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13/all/swaydesk-archive-keyring_2026.11.20_all.deb -o ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Confira o arquivo baixado. O comando tem de mostrar `OK`; se não mostrar, pare aqui, apague o arquivo e não continue." >}}
echo "2527bebb378c926e631fb367f2ccb18120cea26617c3a90b859c633cb2845700  $HOME/swaydesk-archive-keyring_2026.11.20_all.deb" | sha256sum -c
{{< /step >}}
{{< step text="Instale-o. Ele põe a chave em `/usr/share/keyrings/` e o repositório em `/etc/apt/sources.list.d/swaydesk.sources`, e daí em diante mantém os dois atualizados." >}}
sudo dpkg -i ~/swaydesk-archive-keyring_2026.11.20_all.deb && rm ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Opcional, antes do passo 6: veja a impressão digital da chave instalada (precisa do `gpg`: `sudo apt install gpg`)." fpr="installed" >}}
gpg --show-keys /usr/share/keyrings/swaydesk-archive-keyring.asc
{{< /step >}}
{{< step text="Atualize a lista de pacotes e instale o Swaydesk." >}}
sudo apt update && sudo apt install swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="Depois do passo 1 (curl), os outros passos encadeados: se o arquivo baixado não for o esperado, nada é instalado." >}}
deb=swaydesk-archive-keyring_2026.11.20_all.deb
dir=$(mktemp -d) && curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13/all/$deb -o "$dir/$deb" &&
echo "2527bebb378c926e631fb367f2ccb18120cea26617c3a90b859c633cb2845700  $dir/$deb" | sha256sum -c && sudo dpkg -i "$dir/$deb" && rm -r "$dir" &&
sudo apt update && sudo apt install swaydesk-desktop
{{< /oneline >}}
{{< /distro >}}
{{< distro id="ubuntu" name="Ubuntu 26.04 / Mint 27" >}}
{{< steps >}}
{{< step text="Instale o `curl`, que baixa o pacote do repositório." >}}
sudo apt install curl
{{< /step >}}
{{< step text="Baixe o pacote `swaydesk-archive-keyring`: ele adiciona o repositório e a chave do projeto." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/xUbuntu_26.04/all/swaydesk-archive-keyring_2026.11.20_all.deb -o ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Confira o arquivo baixado. O comando tem de mostrar `OK`; se não mostrar, pare aqui, apague o arquivo e não continue." >}}
echo "a34f455e495c69a2c5dd94ff8ce6dd0618ec569d6b010010c2360432f6029020  $HOME/swaydesk-archive-keyring_2026.11.20_all.deb" | sha256sum -c
{{< /step >}}
{{< step text="Instale-o. Ele põe a chave em `/usr/share/keyrings/` e o repositório em `/etc/apt/sources.list.d/swaydesk.sources`, e daí em diante mantém os dois atualizados." >}}
sudo dpkg -i ~/swaydesk-archive-keyring_2026.11.20_all.deb && rm ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Opcional, antes do passo 6: veja a impressão digital da chave instalada (precisa do `gpg`: `sudo apt install gpg`)." fpr="installed" >}}
gpg --show-keys /usr/share/keyrings/swaydesk-archive-keyring.asc
{{< /step >}}
{{< step text="Atualize a lista de pacotes e instale o Swaydesk." >}}
sudo apt update && sudo apt install swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="Depois do passo 1 (curl), os outros passos encadeados: se o arquivo baixado não for o esperado, nada é instalado." >}}
deb=swaydesk-archive-keyring_2026.11.20_all.deb
dir=$(mktemp -d) && curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/xUbuntu_26.04/all/$deb -o "$dir/$deb" &&
echo "a34f455e495c69a2c5dd94ff8ce6dd0618ec569d6b010010c2360432f6029020  $dir/$deb" | sha256sum -c && sudo dpkg -i "$dir/$deb" && rm -r "$dir" &&
sudo apt update && sudo apt install swaydesk-desktop
{{< /oneline >}}
{{< /distro >}}
{{< distro id="arch" name="Arch Linux" >}}
{{< steps >}}
{{< step text="Adicione o repositório ao fim do `/etc/pacman.conf` (uma vez só)." >}}
sudo tee -a /etc/pacman.conf <<'EOF'

[home_nielsonrolim_Arch]
Server = https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/$arch
EOF
{{< /step >}}
{{< step text="Baixe a chave do repositório." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key -o ~/swaydesk.key
{{< /step >}}
{{< step text="Mostre a impressão digital da chave baixada." fpr="plain" >}}
gpg --show-keys ~/swaydesk.key
{{< /step >}}
{{< step text="Adicione a chave ao chaveiro do pacman e assine-a localmente, para o pacman confiar nela. Antes, o comando confere a chave de novo e recusa qualquer outra, como no passo 3." >}}
[ "$(gpg --show-keys --with-colons ~/swaydesk.key | grep -E '^(pub|sub|fpr):' | cut -d: -f1,10 | tr '\n' ' ')" = 'pub: fpr:71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 ' ] &&
sudo pacman-key --add ~/swaydesk.key &&
sudo pacman-key --lsign-key 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 &&
rm ~/swaydesk.key
{{< /step >}}
{{< step text="Instale o Swaydesk. Se você já tem o `jack2`, o pacman pergunta se pode trocá-lo pelo `pipewire-jack`, o JACK do PipeWire, que o Swaydesk usa: responda s." >}}
sudo pacman -Syu swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="Os mesmos passos, encadeados: se a chave baixada não tiver a impressão digital certa, nada é adicionado nem instalado." >}}
key=$(mktemp) && curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key -o "$key" &&
[ "$(gpg --show-keys --with-colons "$key" | grep -E '^(pub|sub|fpr):' | cut -d: -f1,10 | tr '\n' ' ')" = 'pub: fpr:71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 ' ] &&
sudo pacman-key --add "$key" && rm -f "$key" &&
sudo pacman-key --lsign-key 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 &&
printf '\n[home_nielsonrolim_Arch]\nServer = https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/$arch\n' | sudo tee -a /etc/pacman.conf >/dev/null &&
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

Os pacotes estão na versão 0.1.2, estável: veja as [notas do lançamento](https://github.com/nielsonrolim/swaydesk/releases/tag/v0.1.2) e o [histórico de mudanças](https://github.com/nielsonrolim/swaydesk/blob/main/CHANGELOG.md). As versões novas chegam como atualizações.
