---
title: Apps
prompt: "ls /usr/bin/swaydesk-*"
crumb: apps
description: Os apps do Swaydesk e os que ele usa.
---
Além da barra, da dock e dos popups, o Swaydesk traz alguns apps próprios. Todos aparecem na grade de apps (`Super`).

## Tema do Desktop

Escolhe o tema GTK, os ícones e a cor de destaque, e aplica tudo de uma vez: na barra, na dock, nos popups, nas bordas das janelas e nos apps GTK 3, GTK 4 e libadwaita. A escolha fica em `~/.config/sway-desktop/config.toml`. Pelo terminal, o mesmo é feito com o `swaydesk-theme`. Veja a [configuração](/pt-br/guide/config/).

## Captura de Tela

Abre o painel de captura (`Super`+`Shift`+`E`): região, tela inteira ou janela, com atraso opcional. A imagem vai para a área de transferência e para `~/Imagens/Screenshots`. Com o [Gradia](https://flathub.org/apps/be.alexandervanhee.gradia) instalado, a captura pode abrir nele para recortar, anotar e destacar. Para capturar sem o painel, use `Print` e as variações nos [atalhos](/pt-br/shortcuts/).

## Gravação de Tela

Abre o painel de gravação (`Super`+`Shift`+`R`): região, tela inteira ou janela, com o som do sistema, com o microfone ou sem áudio. Durante a gravação, um ● na barra mostra que ela está rodando; um clique nele, ou o mesmo atalho, para. O vídeo vai para `~/Vídeos/Screencasts`.

## Telas {{< soon >}}

Organiza os monitores: posição, resolução, escala e rotação, e em que monitor fica cada workspace. Até ele chegar, o [nwg-displays](https://github.com/nwg-piotr/nwg-displays) faz o mesmo, e a sessão já lê o que ele grava.

## Ajuda {{< soon >}}

Mostra os atalhos de teclado da sessão, com busca. As descrições vêm da própria configuração do Sway, então um atalho que você acrescentar aparece ali também.

## Papel de parede do dia

Ao entrar na sessão, o Swaydesk baixa a imagem do dia do Bing e a usa como papel de parede. Sem rede, fica a última imagem baixada.

## Apps que acompanham

| App | Para quê |
| --- | --- |
| kitty | Terminal (`Ctrl`+`Alt`+`T`) |
| Thunar | Gerenciador de arquivos (`Ctrl`+`Alt`+`E`) |
| rofi | Lançador (`Alt`+`Espaço`) |
| Blueman | Pareamento do Bluetooth (os pedidos de PIN e confirmação) |
| pavucontrol | Ajustes finos de áudio, além do popup da barra (clique do meio no volume) |
