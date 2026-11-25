---
title: Baixar
prompt: "sha256sum -c --ignore-missing SHA256SUMS"
crumb: download
description: As ISOs live do Swaydesk, versão 0.1.7 estável, com instalador.
---
Cada ISO abre uma sessão live do Swaydesk: experimente sem mexer no disco e, se gostar, instale pelo ícone **Instalar o Swaydesk** na dock. São ISOs estáveis, da versão 0.1.7. Já tem Debian 13 ou testing, Ubuntu 26.04, Linux Mint 27 ou Arch? Então não precisa de ISO: [instale os pacotes](/pt-br/install/) no sistema que você já usa. O Debian testing, o Ubuntu 26.04 e o Linux Mint 27 não têm ISO do Swaydesk; neles, o Swaydesk entra só pelos pacotes.

## Requisitos

- Um PC de 64 bits (x86_64), com UEFI ou BIOS
- 2 GB de RAM
- 22 GB de disco
- Placa de vídeo Intel, AMD ou NVIDIA com driver para Wayland

## As ISOs

{{< isos >}}
{{< iso id="debian" >}}
Debian 13 com o Swaydesk. Com o Secure Boot ligado, o driver da NVIDIA também é instalado, assinado com uma chave do seu computador: depois do primeiro login, um aviso pede para rodar `sudo swaydesk-extras`, que mostra uma senha de uso único, e no reinício seguinte você cadastra a chave numa tela azul (o MokManager) com essa senha.
{{< /iso >}}
{{< iso id="arch" >}}
Arch Linux com o Swaydesk. Desligue o Secure Boot nas configurações do firmware antes de dar o boot. O driver da NVIDIA (nvidia-open) entra só para placas Turing (GTX 16xx, RTX 20xx) e mais novas; as mais antigas ficam no nouveau.
{{< /iso >}}
{{< /isos >}}

## Conferir o download

Baixe também o `SHA256SUMS` (o link fica ao lado de cada ISO) para a mesma pasta da ISO e, nessa pasta, rode:

```
sha256sum -c --ignore-missing SHA256SUMS
```

Tem de aparecer o nome da ISO seguido de `OK`. Se aparecer `FAILED`, ou nada, apague a ISO e baixe de novo. O SHA-256 de cada ISO também está no cartão dela, acima: tem de ser igual à linha da ISO no `SHA256SUMS`. Isso pega um download corrompido ou incompleto; não é uma assinatura (os dois são publicados pela mesma conta do GitHub).

## Gravar num pendrive

A ISO é gravada como está, byte a byte, no pendrive inteiro, e **tudo o que houver no pendrive é apagado**. Copiar o arquivo para dentro do pendrive não funciona.

No Linux, descubra o nome do pendrive com `lsblk` (como `/dev/sdb`; nunca uma partição como `/dev/sdb1`, e confira o tamanho para não escolher o seu disco) e rode o comando abaixo, trocando `swaydesk.iso` pelo nome da ISO que você baixou e `/dev/sdX` pelo pendrive:

```
sudo dd if=swaydesk.iso of=/dev/sdX bs=4M status=progress oflag=sync
```

No Windows ou no macOS, o [balenaEtcher](https://etcher.balena.io/) faz o mesmo com uma janela: escolha a ISO, o pendrive e grave. O [Rufus](https://rufus.ie/), no Windows, também serve: quando ele perguntar, escolha o modo **imagem DD**.

## Dar o boot e instalar

1. Com o pendrive conectado, ligue o computador com a tecla do menu de boot (em geral F12, F11, F8 ou Esc, conforme o fabricante) e escolha o pendrive.
2. A sessão live abre sozinha, sem senha e sem bloqueio automático.
3. O ícone **Instalar o Swaydesk** na dock abre o instalador. Ele escolhe o fuso horário pelo seu endereço IP (sem rede, America/Sao_Paulo; dá para trocar) e tem uma caixa de codecs e drivers proprietários, desmarcada por padrão. Essa caixa precisa de rede durante a instalação; sem rede, o sistema instalado lembra você no login, e dá para rodar `sudo swaydesk-extras` depois.

A impressão e o scanner já vêm prontos (CUPS, impressoras da rede pelo avahi e o Digitalizador de documentos), assim como as páginas de manual (`man`).

### Junto com outro sistema (dual boot)

O GRUB do sistema instalado lista os outros sistemas dos discos. A opção do instalador de instalar ao lado do outro sistema só aparece quando o disco tem espaço para o Swaydesk (22 GB e uma folga) e encolhe a partição do outro sistema. Num disco apertado, o instalador pode estimar errado o mínimo dessa partição: o redimensionamento falha antes de mudar qualquer coisa, os dados ficam como estavam e a instalação para. Para evitar isso, encolha o outro sistema antes, pelas ferramentas dele, e instale no espaço livre.

Depois de instalar, os [primeiros passos](/pt-br/guide/first-steps/) cobrem o resto.
