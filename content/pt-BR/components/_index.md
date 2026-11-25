---
title: Componentes
prompt: "ls /usr/bin/swaydesk-*"
crumb: components
aliases: ["apps/"]
description: As peças do Swaydesk, uma por uma.
---
O Swaydesk é feito de componentes próprios, quase todos escritos em Rust com GTK 4. Cada um tem o seu atalho e uma parte no [guia](/pt-br/guide/).

Os atalhos desta página são os do perfil **Swaydesk**, o padrão. Os outros perfis (i3, Hyprland, niri e dwm) mudam boa parte deles: veja todos em [Atalhos](/pt-br/shortcuts/).

Quase todo componente pode ser desligado. A última linha de cada um mostra a chave, que vai no `~/.config/swaydesk/config.toml`; veja [Ligar e desligar componentes](/pt-br/guide/config/#ligar-e-desligar-componentes).

{{< components >}}

## Apps que acompanham

| App | Para quê |
| --- | --- |
| kitty | Terminal (`Ctrl`+`Alt`+`T`) |
| Thunar | Gerenciador de arquivos (`Ctrl`+`Alt`+`E`) |
| rofi | O lançador (`Alt`+`Espaço`) |
| qalc | As contas e as conversões de unidades na busca da grade de apps |
| Blueman | Pareamento do Bluetooth (os pedidos de PIN e confirmação) |
| pavucontrol | Ajustes finos de áudio, além do popup da barra (clique do meio no volume) |
| gammastep | A luz noturna |
| mate-polkit | A janela da senha de administrador (no Debian e no Ubuntu, o lxpolkit também serve) |
| gnome-text-editor | O botão **Abrir** da Ajuda, que edita o `50-local.conf`; sem ele, a Ajuda abre um editor no terminal. Recomendado no Debian e no Ubuntu; opcional no Arch |
| grim, slurp e wf-recorder | A captura e a gravação de tela |
| gtklock | O último recurso do bloqueio, se o do Swaydesk não abrir |

As imagens de instalação trazem também uma loja de apps, o GNOME Software, com o Flathub. No Debian, ela também instala e atualiza os pacotes da distro e o firmware; no Arch, cuida dos apps Flatpak, e o aviso do Swaydesk cuida do resto. Pelos pacotes, instale o `gnome-software` você mesmo, se quiser.
