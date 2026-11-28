---
title: Descargar
prompt: "sha256sum -c --ignore-missing SHA256SUMS"
crumb: download
description: Las ISO live de Swaydesk, versión estable 0.2.0, con instalador.
---
Cada ISO arranca una sesión live de Swaydesk: pruébala sin tocar el disco y, si te gusta, instálala con el icono **Instalar Swaydesk** de la dock. Son ISO estables, de la versión 0.2.0. ¿Ya tienes Debian 13 o testing, Ubuntu 26.04, Linux Mint 27 o Arch? Entonces no necesitas una ISO: [instala los paquetes](/es/install/) en el sistema que tienes. Debian testing, Ubuntu 26.04 y Linux Mint 27 no tienen ISO de Swaydesk; allí, Swaydesk llega solo por los paquetes.

## Requisitos

- Una computadora de 64 bits (x86_64), con UEFI o BIOS
- 2 GB de RAM
- 22 GB de disco
- Una tarjeta gráfica Intel, AMD o NVIDIA con un controlador para Wayland

## Las ISO

{{< isos >}}
{{< iso id="debian" >}}
Debian 13 con Swaydesk. Con Secure Boot activado, también se instala el controlador de NVIDIA, firmado con una clave de tu computadora: después del primer inicio de sesión, un aviso te pide ejecutar `sudo swaydesk-extras`, que muestra una contraseña de un solo uso, y en el siguiente reinicio registras la clave en una pantalla azul (MokManager) con esa contraseña.
{{< /iso >}}
{{< iso id="arch" >}}
Arch Linux con Swaydesk. Desactiva Secure Boot en la configuración del firmware antes de arrancarla. El controlador de NVIDIA (nvidia-open) solo se instala para tarjetas Turing (GTX 16xx, RTX 20xx) y más nuevas; las más antiguas se quedan con nouveau.
{{< /iso >}}
{{< /isos >}}

## Verificar la descarga

Descarga también `SHA256SUMS` (el enlace está junto a cada ISO) en la misma carpeta que la ISO y, en esa carpeta, ejecuta:

```
sha256sum -c --ignore-missing SHA256SUMS
```

Debe mostrar el nombre de la ISO seguido de `OK`. Si muestra `FAILED`, o nada, borra la ISO y descárgala de nuevo. El SHA-256 de cada ISO también está en su tarjeta, más arriba: debe coincidir con la línea de la ISO en `SHA256SUMS`. Esto detecta una descarga dañada o incompleta; no es una firma (los dos se publican desde la misma cuenta de GitHub).

## Grabarla en una memoria USB

La ISO se graba tal cual, byte por byte, en toda la memoria USB, y **todo lo que hay en la memoria se borra**. Copiar el archivo a la memoria no funciona.

En Linux, busca el nombre de la memoria con `lsblk` (como `/dev/sdb`; nunca una partición como `/dev/sdb1`, y revisa el tamaño para no elegir tu disco) y ejecuta el comando de abajo, reemplazando `swaydesk.iso` por el nombre de la ISO que descargaste y `/dev/sdX` por la memoria:

```
sudo dd if=swaydesk.iso of=/dev/sdX bs=4M status=progress oflag=sync
```

En Windows o macOS, [balenaEtcher](https://etcher.balena.io/) hace lo mismo con una ventana: elige la ISO, la memoria y graba. [Rufus](https://rufus.ie/), en Windows, también sirve: cuando lo pregunte, elige el modo **imagen DD**.

## Arrancar e instalar

1. Conecta la memoria USB y enciende la computadora con la tecla del menú de arranque (por lo general F12, F11, F8 o Esc, según el fabricante) y elige la memoria.
2. La sesión live se abre sola, sin contraseña y sin bloqueo automático.
3. El icono **Instalar Swaydesk** de la dock abre el instalador. Elige la zona horaria según tu dirección IP (si no hay red, America/Sao_Paulo; puedes cambiarla) y tiene una casilla de códecs y controladores propietarios, desmarcada por defecto. Esa casilla necesita red durante la instalación; sin red, el sistema instalado te lo recuerda al iniciar sesión y puedes ejecutar `sudo swaydesk-extras` más tarde.

La impresión y el escaneo vienen listos (CUPS, impresoras de red mediante avahi y Escáner de documentos), y también las páginas de manual (`man`).

### Junto a otro sistema (dual boot)

El GRUB del sistema instalado muestra los otros sistemas de los discos. La opción **Instalar junto a** del instalador solo aparece cuando el disco tiene espacio para Swaydesk (22 GB más un margen), y reduce la partición del otro sistema. En un disco justo, el instalador puede calcular mal el mínimo de esa partición: el cambio de tamaño falla antes de modificar nada, los datos quedan como estaban y la instalación se detiene. Para evitarlo, reduce primero el otro sistema, con sus propias herramientas, e instala en el espacio libre.

Después de instalar, los [primeros pasos](/es/guide/first-steps/) explican el resto.
