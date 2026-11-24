---
title: Configuración
prompt: "cat ~/.config/swaydesk/config.toml"
crumb: guide/config
weight: 3
description: Los archivos que editas para ajustar Swaydesk a tu computadora y a tu gusto.
---
La configuración de Sway y de la barra viene con el paquete y se actualiza con él. Lo tuyo vive en unos pocos archivos de tu carpeta personal, que el primer inicio de sesión crea y que las actualizaciones nunca sobrescriben.

| Archivo | Qué guarda |
| --- | --- |
| `~/.config/swaydesk/config.toml` | Idioma, tema, iconos, color de acento, ciudad del clima, días festivos, administrador de archivos, perfil de atajos y los componentes desactivados |
| `~/.config/sway/config.d/50-local.conf` | Monitores, teclado, ratón, aplicaciones al iniciar y espacios de trabajo de las aplicaciones |
| `~/.config/swaydesk/displays.json` | Tus pantallas para cada conjunto de monitores, guardadas por la aplicación **Pantallas** |
| `~/.config/sway-dock/config.toml` | El modo y el tamaño de la dock |

Antes de la 0.1.4, las carpetas `swaydesk` se llamaban `sway-desktop`: `~/.config/sway-desktop`, y lo mismo en `~/.local/share` y `~/.local/state`. El primer inicio de sesión en la 0.1.4 las mueve a `swaydesk` y deja los nombres antiguos como enlaces a las carpetas nuevas, así que las rutas antiguas siguen funcionando. Si un archivo está en la carpeta antigua y en la nueva, no se mueve nada, la carpeta antigua sigue en uso y el registro de la sesión lo indica (`grep kept: ~/.local/state/sway/sway.log`); combina las dos carpetas a mano para cambiar.

## Configuración del escritorio

`~/.config/swaydesk/config.toml` vale para todas las piezas de Swaydesk. La forma más fácil de cambiar el tema y el color es la aplicación **Tema del escritorio**, que escribe este archivo por ti. Desde una terminal, `swaydesk-theme` hace lo mismo:

```
swaydesk-theme families                  # las familias de temas instaladas
swaydesk-theme pick Adwaita dark teal    # familia, claro u oscuro, y el color
swaydesk-theme current                   # el tema, los iconos y el color en uso
swaydesk-theme cursor 32                 # el tamaño del cursor; sin número, los tamaños que tiene el tema del cursor
```

Los colores son los de las carpetas de Papirus; `swaydesk-theme colors` los muestra todos.

El tamaño del cursor también está en la aplicación, en la lista **Tamaño del cursor** debajo de los iconos, que solo muestra los tamaños que tiene el tema del cursor. La elección se aplica al instante, sin **Aplicar**: las aplicaciones GTK 4 y Qt 6 cambian enseguida, y las más antiguas (GTK 3, Qt 5, Electron y las aplicaciones X11) cuando las vuelves a abrir.

Este es un archivo de ejemplo con las claves que puedes cambiar a mano:

```
# Idioma de los textos, las fechas y el clima. Vacío: el idioma del sistema
locale = "en_US"

# Ciudad del pronóstico del clima. Vacío: según tu dirección IP
weather_location = "Denver"

# País de los días festivos del calendario. Vacío: el del idioma. "none": ninguno
holidays = "US"

# Tema GTK, iconos y color de acento
gtk_theme = "Adwaita-dark"
icon_theme = "Papirus-Dark"
accent = "#199ca8"

# true: el color de acento viene del fondo de pantalla y cambia con él. Sin esta clave, está activado mientras
# el acento es el predeterminado y hay fondo de pantalla, y desactivado en los demás casos
accent_auto = true

# Color de las carpetas de Papirus, como "teal". Vacío: el más cercano al acento
folder_color = ""

# Administrador de archivos de Ctrl+Alt+E, de la cuadrícula de aplicaciones y de la dock. Vacío: el primero instalado
file_manager = "thunar"

# Perfiles de energía en la ventana emergente Sistema: "auto" (el predeterminado) solo sin batería, "always" o "never"
power_profiles_in_system = "auto"

# Tamaño del cursor en píxeles, de 16 a 96 (24 por defecto)
cursor_size = 24
```

Los programas leen el archivo al iniciar. Después de editarlo a mano:

- para el color de acento, primero pon `accent_auto = false`, o el siguiente fondo de pantalla traerá de vuelta su propio color; luego ejecuta `swaydesk-desktop-config apply`, que escribe los colores y recarga Sway; las ventanas emergentes toman el nuevo color de inmediato, y el resto cambia en tu próximo inicio de sesión;
- para el administrador de archivos, ejecuta `swaydesk-desktop-config generate`, para que las carpetas que abren otras aplicaciones también vayan a él;
- para el idioma, la ciudad y los días festivos, cierra sesión y vuelve a iniciarla;
- para `power_profiles_in_system`, nada: se aplica la próxima vez que se abre la ventana emergente Sistema;
- para `cursor_size`, usa en su lugar `swaydesk-theme cursor <tamaño>`, que además lo aplica al instante.

Un valor incorrecto no rompe nada: esa pieza simplemente usa el valor predeterminado de esa clave.

En una computadora sin batería, el ícono de la batería sale de la barra, y con él los botones de perfil de su ventana emergente. Por eso la ventana emergente Sistema gana una fila **Perfil de energía** con los perfiles que ofrece `power-profiles-daemon` (Ahorro de energía, Equilibrado y, donde el hardware lo permite, Rendimiento): un clic cambia el perfil sin cerrar la ventana emergente. Sin el daemon, la fila no aparece. Con `"always"` aparece también en las laptops; la ventana emergente de la batería conserva sus botones en cualquier caso.

## Desactivar componentes

Todos los componentes de Swaydesk vienen activados, menos el método de entrada ([abajo](#metodo-de-entrada)). Para desactivar uno, pon su clave en `false` en la sección `[enabled]` de `~/.config/swaydesk/config.toml`; los módulos de la barra van en `[enabled.bar]`:

```
[enabled]
dock = false            # la dock
bing_wallpaper = false  # el fondo de pantalla del día

[enabled.bar]
weather = false         # el clima en la barra
```

| Clave de `[enabled]` | Qué desactiva |
| --- | --- |
| `dock` | La dock |
| `app_grid` | La cuadrícula de aplicaciones (al tocar `Super`) |
| `switcher` | La tarjeta de `Alt`+`Tab` |
| `notifications` | El servicio de notificaciones |
| `osd` | El indicador de volumen y brillo |
| `clipboard_history` | El historial del portapapeles |
| `nightlight` | La luz nocturna |
| `bing_wallpaper` | El fondo de pantalla del día |
| `polkit_agent` | El agente de polkit (la contraseña de administrador) |
| `update_notifier` | El aviso de actualizaciones |
| `displays` | Los perfiles automáticos de las pantallas; la aplicación **Pantallas** se queda |
| `autostart` | Las aplicaciones de `~/.config/autostart` y `/etc/xdg/autostart` (ver abajo) |
| `input_method` | Desactivada salvo que sea `true`: entonces la sesión arranca el método de entrada fcitx5 (ver abajo) |

Las claves de `[enabled.bar]` son los módulos de la barra: `weather`, `clock`, `media`, `recording`, `notifications`, `clipboard`, `language`, `system`, `brightness`, `caffeine`, `bluetooth`, `network`, `volume`, `battery`, `power` y, en Arch, `updates`. Los espacios de trabajo y la bandeja están siempre.

Un cambio se aplica en tu próximo inicio de sesión. Una clave que falta queda activada (menos `input_method`), y un error en el archivo nunca desactiva nada. En la Ayuda (`Super`+`F1`), la tarjeta de un componente desactivado dice "Desactivado" y cómo volver a activarlo. La página [Componentes](/es/components/) muestra la clave de cada uno.

### Aplicaciones que se inician al iniciar sesión

La sesión inicia las aplicaciones de las carpetas de inicio automático XDG, `~/.config/autostart` y `/etc/xdg/autostart`, como lo hacen GNOME y KDE, y las cierra cuando cierras sesión. Las entradas de lo que Swaydesk ya cubre (blueman, nm-applet, los agentes de polkit de mate y lxpolkit, xapp-sn-watcher) se omiten, solo en la sesión de Swaydesk: GNOME o KDE en la misma cuenta las siguen iniciando. La entrada del propio PulseAudio también se omite ahí, pero solo cuando PipeWire es el servidor de sonido, caso en el que solo fallaría.

Para que una aplicación no se inicie, pon una copia de su archivo `.desktop` en `~/.config/autostart` con `Hidden=true`, o con `NotShowIn=sway;` para omitirla solo en las sesiones de Sway, de modo que GNOME o KDE la sigan iniciando. Para desactivarlas todas, pon `autostart = false` en `[enabled]`. Un `config.toml` de una versión anterior no tiene esa clave: agrega la línea dentro de `[enabled]`, antes de la parte `[enabled.bar]`, porque una línea debajo de `[enabled.bar]` pertenece a la barra.

### Método de entrada (fcitx5) {#metodo-de-entrada}

En Wayland, Chromium, Chrome, Vivaldi, Brave y las aplicaciones Electron (VS Code, Slack, Discord) ignoran `~/.XCompose` y componen los acentos con una tabla propia, la de en_US, en la que `'` + `c` da `ć`. El método de entrada fcitx5 hace que en ellas salga la `ç`. Con `input_method = true` en `[enabled]` y el paquete `fcitx5` instalado, el inicio de sesión arranca fcitx5 con sus atajos, su icono en la bandeja y sus avisos desactivados, con el teclado de la sesión (la primera distribución). Sigue al teclado cuando lo cambias en `50-local.conf`, hasta que cambies tú mismo los métodos de fcitx5 (en `fcitx5-configtool`, por ejemplo). Quien cambia la distribución sigue siendo Sway, con `Super`+`Espacio`, y las aplicaciones GTK siguen componiendo por sí mismas.

La clave viene desactivada en un sistema que instaló los paquetes, y activada en las imágenes de instalación de Debian 13 y Arch, por `/etc/swaydesk/config.toml`, que solo trae los valores predeterminados del sistema para `[enabled]`. Una línea en tu propio `config.toml` tiene prioridad.

Los navegadores también necesitan dos opciones, `--enable-wayland-ime --wayland-text-input-version=3`:

- **En Arch**, el inicio de sesión crea los archivos de opciones que leen los lanzadores, en `~/.config`: `chromium-flags.conf`, `chrome-flags.conf`, `vivaldi-stable.conf`, `brave-flags.conf`, `electron-flags.conf` y `code-flags.conf`, solo para lo que esté instalado y solo cuando el archivo no existe. En un archivo tuyo, agrega las dos opciones. Un navegador instalado a mitad de la sesión recibe su archivo en el próximo inicio de sesión: cierra la sesión y vuelve a entrar (o crea el archivo) antes de abrirlo.
- **En Debian**, Chromium no lee esos archivos y llega a fcitx5 por el `GTK_IM_MODULE=fcitx` que exporta im-config, que viene con fcitx5. Chrome y Vivaldi de los `.deb` de sus fabricantes, y las aplicaciones Electron, necesitan las opciones en su acceso directo: copia el `.desktop` a `~/.local/share/applications` y agrégalas a su línea `Exec`.

No arranca nada si hay otro método de entrada configurado (`GTK_IM_MODULE`, `QT_IM_MODULE` o `XMODIFIERS` apuntando a otro, como el ibus que exporta el im-config de Linux Mint) o si `ibus-daemon` ya está en ejecución. Si arrancas ibus desde `50-local.conf`, desactiva `input_method`. En Linux Mint, para usar fcitx5, elígelo con `im-config -n fcitx5` (con los paquetes `fcitx5-frontend-gtk3` y `fcitx5-frontend-gtk4`) y activa la clave.

Para desactivarlo, pon `input_method = false`: se aplica en el próximo inicio de sesión, y los archivos creados se quedan. En Arch, la entrada de inicio automático del propio paquete fcitx5 lo sigue arrancando, como en cualquier sesión: quita el paquete, o pon una copia de `/etc/xdg/autostart/org.fcitx.Fcitx5.desktop` en `~/.config/autostart` con `NotShowIn=sway;` (solo en Swaydesk) o `Hidden=true` (en todos los escritorios de la cuenta). En Debian, im-config exporta `GTK_IM_MODULE=fcitx` en toda sesión Wayland mientras fcitx5 esté instalado, en cualquier escritorio; `im-config -n none` (o quitar fcitx5) vuelve al valor predeterminado.

## Ajustes de la máquina

Sway lee los archivos de `~/.config/sway/config.d/` al final, así que lo que haya ahí tiene prioridad sobre la configuración del paquete. El primer inicio de sesión crea `50-local.conf` con ejemplos comentados y la distribución de teclado del sistema. Edítalo y aplícalo con `Super`+`R` (o `swaymsg reload`).

Un ejemplo completo:

```
# Pantalla: el nombre de la salida viene de `swaymsg -t get_outputs`
output eDP-1 mode 1920x1080@60Hz scale 1

# Teclado: ABNT2 brasileño y US internacional, alternados con Super+Espacio
input type:keyboard {
    xkb_layout  br,us
    xkb_variant abnt2,intl
}

# Ratón: para zurdos y con desplazamiento natural
input type:pointer {
    left_handed    enabled
    natural_scroll enabled
}

# Aplicaciones al iniciar sesión que no tienen entrada de inicio automático (las de ~/.config/autostart ya se inician)
exec foot --server

# Espacios de trabajo de las aplicaciones: la aplicación se abre ahí, y tú te quedas donde estás
assign [app_id="^org.mozilla.firefox$"] workspace number 2
assign [app_id="^thunderbird$"]         workspace number 9

# Para cambiar un atajo que ya existe, usa --no-warn
bindsym --no-warn Ctrl+Alt+t exec foot
```

Algunos consejos:

- Con dos distribuciones en `xkb_layout`, la sesión siempre empieza con la primera.
- Para encontrar el `app_id` de una ventana abierta, ejecuta `swaymsg -t get_tree | grep app_id`. Las aplicaciones que se ejecutan con XWayland usan `class=` en lugar de `app_id=`.
- Swaydesk genera `00-accent.conf` y `00-font.conf` en la misma carpeta: no los edites, porque se vuelven a escribir.
- La referencia completa de estos comandos está en `man 5 sway` y `man 5 sway-input`.

### Teclado y acentos

- **El teclado del sistema.** El bloque de teclado que el primer inicio de sesión escribe al final de `50-local.conf` sigue al teclado del sistema en cada inicio de sesión, mientras nadie lo edite. Un cambio con `localectl set-x11-keymap` o `sudo dpkg-reconfigure keyboard-configuration` llega a las cuentas existentes en su siguiente inicio de sesión, y la pantalla de inicio de sesión y las cuentas nuevas también lo siguen. Un bloque que editaste se queda como está, y un bloque tuyo más abajo en el archivo tiene prioridad sobre el nuestro.
- **Debian y Ubuntu.** Ahí, `localectl` solo cambia `/etc/vconsole.conf`, que el arranque reescribe a partir de `/etc/default/keyboard`: el cambio que sobrevive a un reinicio es `sudo dpkg-reconfigure keyboard-configuration`. En Arch, `localectl` se mantiene.
- **`ç` en US internacional.** Con la sesión en US internacional (`intl` o `altgr-intl`), `'` + `c` da `ç` (y `'` + `C` da `Ç`) en las aplicaciones GTK y Qt, en las terminales y en la pantalla de inicio de sesión. Para eso, el inicio de sesión crea este `~/.XCompose`, si no hay nada en esa ruta:

  ```
  include "%L"
  <dead_acute> <c> : "ç" ccedilla
  <dead_acute> <C> : "Ç" Ccedilla
  ```

  Un archivo tuyo nunca se toca. Si la sesión deja de usar US internacional, el archivo desaparece en el siguiente inicio de sesión, mientras no se haya editado. Si escribes uno a mano, deja la línea `include` primero: sin ella, el archivo reemplaza toda la tabla y los demás acentos (`'` + `e`, `~` + `a`) dejan de funcionar.
- **Acentos y métodos de entrada.** Sin un método de entrada (ibus, fcitx) configurado, la sesión usa `GTK_IM_MODULE=simple`, así que GTK compone las teclas muertas por sí mismo, también en las aplicaciones GTK 4. Si usas un método de entrada, define `GTK_IM_MODULE`, `QT_IM_MODULE` o `XMODIFIERS` en `~/.profile` (por ejemplo, `export GTK_IM_MODULE=wayland` para fcitx5), y la sesión no los toca. Para la `ç` en Chromium y en las aplicaciones Electron, consulta [Método de entrada (fcitx5)](#metodo-de-entrada). Lo mismo vale para un teclado en pantalla que escribe a través del método de entrada, como squeekboard: necesita `export GTK_IM_MODULE=wayland` en `~/.profile`.

## Búsquedas del lanzador

Las búsquedas de la pestaña **Web** del lanzador se pueden cambiar en `~/.config/swaydesk/launcher.conf`, un `clave = valor` por línea (`#` empieza un comentario):

```
# un prefijo y la dirección de la búsqueda; %s es el texto que escribes
search = gh https://github.com/search?q=%s
# la búsqueda del texto sin prefijo (sin esta línea, Google)
default = d
```

Una línea `search` con un prefijo nuevo agrega una búsqueda, y una con un prefijo existente (`g`, `d`, `w`, `yt`, `gt`, `cl`, `gpt`) la reemplaza. La dirección debe empezar con `http://` o `https://`, contener `%s` y no tener espacios; si no, la línea se ignora; un `default` con un prefijo desconocido vuelve a Google. El cambio se aplica la próxima vez que abras el lanzador.

## Pantallas

La forma más fácil de configurar tus pantallas es la aplicación **Pantallas**, en la cuadrícula de aplicaciones. Arrastra las pantallas en el mapa, elige la resolución, la frecuencia de actualización, la escala y la rotación de cada una, y haz clic en **Aplicar**. Si no haces clic en **Mantener** en 15 segundos, todo vuelve a como estaba.

Cada conjunto de monitores (la laptop sola, la laptop con el monitor de la oficina…) guarda su propia disposición en `~/.config/swaydesk/displays.json`, que se aplica sola cuando conectas o desconectas una pantalla. Con la tapa cerrada y un monitor externo encendido, la pantalla de la laptop se apaga. La última disposición que mantuviste también va a `~/.config/sway/config.d/90-displays.conf`, que se lee después de `50-local.conf`, así que tiene prioridad sobre una línea `output` de ahí. No edites ese archivo a mano: el siguiente **Mantener** lo vuelve a escribir.

## La dock

La dock lee `~/.config/sway-dock/config.toml`, que al principio no existe: créalo solo con lo que quieras cambiar. Después de editarlo, ejecuta `swaydesk-dock reload`.

```
# overlap: se oculta cuando una ventana necesita su espacio
# auto-hide: oculta hasta que empujas el puntero contra el borde
# always: siempre visible
mode = "auto-hide"

icon_size = 40          # de 16 a 128
hide_delay_ms = 400     # espera antes de ocultarse, en milisegundos
animation_ms = 200      # duración del deslizamiento; 0 lo desactiva

ignore = []             # app_ids que nunca aparecen en la dock
outputs = ["eDP-1"]     # monitores con dock; vacío: todos
```

Las aplicaciones fijadas se listan en `~/.local/share/sway-dock/pinned`, pero es más sencillo fijarlas con un clic derecho en la dock o en la cuadrícula de aplicaciones. La cuadrícula de aplicaciones guarda sus grupos y favoritos en `~/.local/share/sway-drawer/`.

## Actualizaciones en Arch

En Arch, la parte de actualizaciones de la tienda (GNOME Software) está desactivada, porque el aviso de Swaydesk se encarga de todo: los repositorios oficiales, el AUR (con paru o yay, si ya tienes uno instalado), las aplicaciones Flatpak y el firmware (fwupd). Revisa en segundo plano, muestra en la barra un icono con la cantidad y envía una notificación cuando hay algo nuevo; nada se actualiza solo. Un clic (o el botón **Actualizar** de la notificación) abre una terminal con la actualización.

- **Para desactivar el aviso de Swaydesk** (si prefieres actualizar a mano o con otra herramienta): pon `update_notifier = false` en la sección `[enabled]` de `~/.config/swaydesk/config.toml` y vuelve a iniciar sesión. La revisión, la notificación y el icono se detienen, y la tienda vuelve a encargarse de las actualizaciones por su cuenta.
- **Para volver a activar a mano la parte de actualizaciones de la tienda**, conservando el aviso de Swaydesk: `gsettings set org.gnome.software allow-updates true` (para deshacerlo: `gsettings reset org.gnome.software allow-updates`). Con ambos activados, las actualizaciones de Flatpak aparecen dos veces.
- **Solo el icono:** `updates = false` en la sección `[enabled.bar]` oculta el icono y mantiene la revisión y la notificación.

## SwayFX en Arch (opcional)

[SwayFX](https://github.com/WillPower3309/swayfx) es Sway con esquinas redondeadas, desenfoque y sombras. En Arch puede ocupar el lugar de Sway, con la misma configuración. Viene del AUR, a través de un AUR helper:

```
yay -S swayfx           # o: paru -S swayfx; pacman cambia sway por él
sudo pacman -S sway     # para volver a Sway
```

`swaydesk-desktop` sigue instalado en ambos casos, porque `swayfx` provee `sway`.

**Advertencia:** SwayFX viene del AUR y lo mantienen terceros, fuera del soporte del proyecto. Puede quedarse atrás respecto a las versiones de Sway, y un `pacman -Syu` que traiga un wlroots nuevo puede romperlo hasta que el AUR se ponga al día. Si la sesión no inicia después de una actualización, vuelve a Sway con `sudo pacman -S sway` desde una consola de texto (Ctrl+Alt+F2).

Swaydesk activa los efectos por sí mismo en el siguiente inicio de sesión. Detecta SwayFX y escribe `~/.config/sway/config.d/10-effects.conf`; con Sway normal, el archivo solo contiene un comentario. El archivo se vuelve a escribir en cada inicio de sesión, cuando cambia el tema y con `swaydesk-desktop-config generate` (después ejecuta `swaymsg reload`).

Los efectos están en la sección `[effects]` de `~/.config/swaydesk/config.toml`. Una clave que falta conserva su valor predeterminado:

```
[effects]
corner_radius = 10      # esquinas de las ventanas y de las capas, en píxeles, de 0 (rectas) a 30
blur = true             # desenfoque detrás de las ventanas transparentes
shadows = true          # una sombra suave en las ventanas
layer_blur = false      # desenfoque detrás de la barra, la dock, las ventanas emergentes, las notificaciones y los menús
dim_inactive = 0.0      # oscurecer las ventanas sin foco, de 0.0 (nada) a 1.0
```

El desenfoque detrás de la barra, la dock y las ventanas emergentes está desactivado por defecto, porque mostraba basura visual en una máquina virtual (virgl). Actívalo con `layer_blur = true`. Dos cosas nunca tienen desenfoque: la capa invisible que cierra las ventanas emergentes cuando haces clic fuera de ellas, y el selector de captura de pantalla, que tiene que mostrar la pantalla nítida.

## La pantalla de inicio de sesión

Con `swaydesk-greeter`, la pantalla de inicio de sesión tiene su propia configuración, para toda la computadora:

- `/etc/swaydesk-greeter/config.toml` acepta el color de acento y el idioma, en el mismo formato que la configuración del escritorio (`accent = "#8e44ad"`, `locale = "en_US"`);
- los archivos de `/etc/swaydesk-greeter/sway.d/*.conf` aceptan comandos de Sway para las pantallas de la pantalla de inicio de sesión, como `output eDP-1 scale 1.25`.
