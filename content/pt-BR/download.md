---
title: Baixar
prompt: "sha256sum -c swaydesk.iso.sha256"
crumb: download
description: As ISOs live do Swaydesk para Debian 13, Ubuntu 26.04 e Arch Linux, com instalador.
---
Cada ISO abre uma sessão live do Swaydesk: experimente sem mexer no disco e, se gostar, instale pelo ícone **Instalar o Swaydesk** na dock. Já tem Debian 13, Ubuntu 26.04, Linux Mint 27 ou Arch? Então não precisa de ISO: [instale os pacotes](/pt-br/install/) no sistema que você já usa.

## Requisitos

- Um PC de 64 bits (x86_64), com UEFI ou BIOS
- 2 GB de RAM
- 20 GB de disco
- Placa de vídeo Intel, AMD ou NVIDIA com driver para Wayland

## As ISOs

{{< isos >}}
{{< iso id="debian" >}}
Debian 13 com o Swaydesk.
{{< /iso >}}
{{< iso id="ubuntu" >}}
Ubuntu 26.04 com o Swaydesk, sem telemetria. Mantém o cliente do Ubuntu Pro, sem os anúncios: o Ubuntu Pro (atualizações de segurança estendidas para o universe, grátis para uso pessoal em até 5 máquinas) fica desligado até você rodar `sudo pro attach`.
{{< /iso >}}
{{< iso id="arch" >}}
Arch Linux com o Swaydesk. Desligue o Secure Boot nas configurações do firmware antes de dar o boot.
{{< /iso >}}
{{< /isos >}}

## Gravar num pendrive

A ISO é gravada como está, byte a byte, no pendrive inteiro, e **tudo o que houver no pendrive é apagado**. Copiar o arquivo para dentro do pendrive não funciona.

No Linux, descubra o nome do pendrive com `lsblk` (como `/dev/sdb`; nunca uma partição como `/dev/sdb1`, e confira o tamanho para não escolher o seu disco) e rode:

```
sudo dd if=swaydesk-debian13-amd64.hybrid.iso of=/dev/sdX bs=4M status=progress oflag=sync
```

No Windows ou no macOS, o [balenaEtcher](https://etcher.balena.io/) faz o mesmo com uma janela: escolha a ISO, o pendrive e grave. O [Rufus](https://rufus.ie/), no Windows, também serve: quando ele perguntar, escolha o modo **imagem DD**.

## Dar o boot e instalar

1. Com o pendrive conectado, ligue o computador com a tecla do menu de boot (em geral F12, F11, F8 ou Esc, conforme o fabricante) e escolha o pendrive.
2. A sessão live abre sozinha, sem senha e sem bloqueio automático.
3. O ícone **Instalar o Swaydesk** na dock abre o instalador. Ele escolhe o fuso horário pelo seu endereço IP (sem rede, America/Sao_Paulo; dá para trocar) e tem uma caixa de codecs e drivers proprietários, desmarcada por padrão. Essa caixa precisa de rede durante a instalação; sem rede, o sistema instalado lembra você no login, e dá para rodar `sudo swaydesk-extras` depois.

**Secure Boot:** as ISOs do Debian e do Ubuntu dão o boot com ele ligado. Com o Secure Boot ligado, o instalador do Debian não instala o driver da NVIDIA (o módulo dele não é assinado): desligue o Secure Boot, ou registre uma chave MOK, e rode `sudo swaydesk-extras`. A ISO do Arch precisa do Secure Boot desligado.

Depois de instalar, os [primeiros passos](/pt-br/guide/first-steps/) cobrem o resto. As ISOs e os pacotes são a versão 0.1.0.
