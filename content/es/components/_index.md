---
title: Componentes
prompt: "ls /usr/bin/swaydesk-*"
crumb: components
description: Las piezas de Swaydesk, una por una.
---
Swaydesk está hecho de componentes propios, casi todos escritos en Rust con GTK 4. Cada uno tiene su atajo y una parte en la [guía](/es/guide/).

Los atajos de esta página son los del perfil **Swaydesk**, el predeterminado. Los otros perfiles (i3, Hyprland, niri y dwm) cambian muchos de ellos: míralos todos en [Atajos](/es/shortcuts/).

Casi todos los componentes se pueden desactivar. La última línea de cada uno muestra la clave, que va en `~/.config/swaydesk/config.toml`; mira [Desactivar componentes](/es/guide/config/#desactivar-componentes).

{{< components >}}

## Aplicaciones que vienen incluidas

| Aplicación | Para qué |
| --- | --- |
| kitty | Terminal (`Ctrl`+`Alt`+`T`) |
| Thunar | Administrador de archivos (`Ctrl`+`Alt`+`E`) |
| rofi | El lanzador (`Alt`+`Space`) |
| qalc | Cálculos y conversiones de unidades en la búsqueda de la cuadrícula de aplicaciones |
| Blueman | Vinculación de Bluetooth (solicitudes de PIN y de confirmación) |
| pavucontrol | Ajustes de audio detallados, más allá de la ventana emergente de la barra (clic central en el volumen) |
| gammastep | La luz nocturna |
| mate-polkit | La ventana de la contraseña de administrador (en Debian y Ubuntu, lxpolkit también funciona) |
| gnome-text-editor | El botón **Abrir** de la Ayuda, que edita `50-local.conf`; sin él, la Ayuda abre un editor en la terminal. Recomendado en Debian y Ubuntu; opcional en Arch |
| grim, slurp y wf-recorder | Capturas y grabación de pantalla |
| gtklock | El último recurso del bloqueo, si el de Swaydesk no puede abrirse |

Las imágenes de instalación también traen una tienda de aplicaciones, GNOME Software, con Flathub. En Debian también instala y actualiza los paquetes de la distribución y el firmware; en Arch se encarga de las aplicaciones Flatpak, y el aviso de Swaydesk se encarga del resto. Con los paquetes, instala `gnome-software` tú mismo si lo quieres.
