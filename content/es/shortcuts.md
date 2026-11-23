---
title: Atajos
prompt: "grep '^## ' keys/*.conf"
crumb: shortcuts
description: Todos los atajos de teclado de la sesión de Swaydesk.
---
Swaydesk viene con cinco perfiles de atajos: **Swaydesk** (el predeterminado, que sigue a KDE Plasma con Krohnkite), **i3**, **Hyprland**, **niri** y **dwm**. Cada uno trae a Swaydesk las teclas de ese gestor de ventanas, y todos los perfiles tienen 9 espacios de trabajo. Los atajos que no usan Super con una letra (el menú de la sesión, la terminal, las capturas de pantalla, las teclas multimedia) son iguales en todos. `Super` es la tecla del logotipo.

**Elegir un perfil:** en la **Ayuda** (`Super`+`F1`), la lista desplegable de arriba, junto al campo de búsqueda, muestra el perfil en uso. Elige otro y se aplica al instante, sin cerrar la sesión; la Ayuda pasa a mostrar los atajos nuevos. Elegir dwm pide confirmación antes, porque su modificador es Alt. Desde una terminal, pon `shortcuts = "i3"` (o `swaydesk`, `hyprland`, `niri`, `dwm`) en `~/.config/swaydesk/config.toml` y recarga Sway con `swaymsg reload` o con la tecla de recargar del perfil, o vuelve a iniciar sesión.

Las tablas de abajo salen de los mismos archivos y descripciones que muestra la aplicación **Ayuda** (`Super`+`F1`).

{{< profiles >}}

**Dentro de los paneles de captura y grabación**, iguales en todos los perfiles, las teclas son las iniciales en inglés: `R` región, `S` pantalla, `W` ventana, `Esc` cierra. En el panel de captura de pantalla, `G` activa o desactiva Gradia y `D` cambia el retraso. En el panel de grabación, `Shift`+tecla graba con el sonido del sistema, `Ctrl`+tecla con el micrófono, y `A` cambia el audio.

## Personalizar los atajos

Tus atajos están en `~/.config/sway/config.d/50-local.conf`. El archivo se crea en tu primer inicio de sesión, solo con comentarios y ejemplos, y es tuyo: ni las actualizaciones ni una reinstalación lo sobrescriben. Sway lo lee después de los atajos de Swaydesk y del perfil de atajos que elegiste, así que lo que contenga tiene prioridad.

**Cambiar lo que hace un atajo:** repite la tecla con `--no-warn`. Sin eso, Sway avisa que la tecla ya tenía un atajo.

```
## Open foot
bindsym --no-warn Ctrl+Alt+t exec foot
```

**Quitar un atajo:** usa `unbindsym` con la tecla exactamente como la define el perfil activo, incluidas opciones como `--locked`. Quitar una tecla que no tiene atajo es un error de configuración.

```
unbindsym Print
```

**Agregar un atajo:** elige una tecla libre. De `Super`+`F2` a `Super`+`F12` y `Super`+`Ctrl`+`Alt`+una letra están libres en todos los perfiles.

```
## Open another terminal
bindsym Mod4+F12 exec kitty
```

El comentario `##` justo encima de un atajo es la descripción que muestra la Ayuda.

**Aplicar:** guarda el archivo y ejecuta `swaymsg reload` en una terminal, o vuelve a iniciar sesión. Si algo está mal, Sway muestra una barra en la parte de arriba de la pantalla con la línea que falla.

**Comprobar:** la Ayuda de Swaydesk (`Super`+`F1`) muestra los atajos en uso, incluidos tus cambios. Al final de la pestaña Atajos, la Ayuda muestra la ruta del archivo y, cuando el archivo ya existe, un botón **Abrir** que lo abre en tu editor predeterminado.

El mismo archivo también guarda los ajustes de esta máquina: pantalla, teclado, ratón, programas al iniciar sesión y aplicaciones en los espacios de trabajo. Los ejemplos están en sus comentarios, y la [guía de configuración](/es/guide/config/#ajustes-de-la-máquina) los explica.
