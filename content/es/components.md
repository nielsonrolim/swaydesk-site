---
title: Componentes
prompt: "ls /usr/bin/swaydesk-*"
crumb: components
description: Las piezas de Swaydesk, una por una.
---
Swaydesk está hecho de componentes propios, casi todos escritos en Rust con GTK 4. Cada uno tiene su atajo y una parte en la [guía](/en-us/guide/).

Los atajos de esta página son los del perfil **Swaydesk**, el predeterminado. Los otros perfiles (i3, Hyprland, niri y dwm) cambian muchos de ellos: míralos todos en [Atajos](/es/shortcuts/).

Casi todos los componentes se pueden desactivar. La última línea de cada uno muestra la clave, que va en `~/.config/sway-desktop/config.toml`; mira [Desactivar componentes](/en-us/guide/config/#turning-components-off).


## Barra y ventanas emergentes

{{< component title="Red" shot="network" keys="Haz clic en el icono de red" guide="/en-us/guide/desktop/#the-bar" bin="swaydesk-network-popup" src="rust/network-popup" tech="rust" off="bar.network" >}}Wi-Fi, red cableada y VPN: actívalas y desactívalas, conéctate, escribe la contraseña y mira los detalles. Funciona con NetworkManager, y también con iwd y systemd-networkd (la VPN, solo con NetworkManager).{{< /component >}}

{{< component title="Bluetooth" shot="bluetooth" keys="Haz clic en el icono de Bluetooth" guide="/en-us/guide/desktop/#the-bar" bin="swaydesk-bluetooth-popup" src="rust/bluetooth-popup" tech="rust" off="bar.bluetooth" >}}Activa el Bluetooth, busca dispositivos, los vincula, los conecta, los olvida y envía archivos.{{< /component >}}

{{< component title="Audio" shot="audio" keys="Haz clic en el volumen (clic central: pavucontrol)" guide="/en-us/guide/desktop/#the-bar" bin="swaydesk-audio-popup" src="rust/audio-popup" tech="rust" off="bar.volume" >}}Volumen y silencio de la salida y del micrófono, y qué dispositivo usa cada uno.{{< /component >}}

{{< component title="Batería" shot="battery" keys="Haz clic en la batería" guide="/en-us/guide/desktop/#the-bar" bin="swaydesk-battery-popup" src="rust/battery-popup" tech="rust" off="bar.battery" >}}Carga, tiempo restante, consumo, salud, un gráfico de 12 horas y el perfil de energía.{{< /component >}}

{{< component title="Brillo y luz nocturna" shot="brightness" keys="Haz clic en el icono de brillo; teclas de brillo" guide="/en-us/guide/desktop/#the-bar" bin="swaydesk-brightness-popup" src="rust/brightness-popup" tech="rust" off="bar.brightness" >}}El brillo de la pantalla y la luz nocturna: apagada, encendida o en el horario que elijas.{{< /component >}}

{{< component title="Multimedia" shot="media" keys="Haz clic en el icono de multimedia (solo aparece mientras algo se reproduce)" guide="/en-us/guide/desktop/#the-bar" bin="swaydesk-media-popup" src="rust/media-popup" tech="rust" off="bar.media" >}}Portada, título, progreso y los controles del reproductor que esté sonando.{{< /component >}}

{{< component title="Clima" shot="weather" keys="Haz clic en la temperatura" guide="/en-us/guide/desktop/#the-bar" bin="swaydesk-weather-popup" src="rust/weather-popup" tech="rust" off="bar.weather" >}}El pronóstico de hoy y de los próximos días, para la ciudad que configures o la que indique tu IP.{{< /component >}}

{{< component title="Calendario" shot="calendar" keys="Haz clic en la fecha" guide="/en-us/guide/desktop/#the-bar" bin="swaydesk-calendar" src="rust/calendar" tech="rust" off="bar.clock" >}}El mes, con los días festivos de tu país.{{< /component >}}

{{< component title="Sistema" shot="system" keys="Haz clic en el icono del sistema" guide="/en-us/guide/desktop/#the-bar" bin="swaydesk-system-popup" src="rust/system-popup" tech="rust" off="bar.system" >}}CPU, memoria, disco, temperatura y los procesos que más consumen, con "Terminar". El icono se pone naranja cuando algo está al límite.{{< /component >}}

{{< component title="Cafeína" shot="caffeine" keys="Haz clic en la taza" guide="/en-us/guide/desktop/#the-bar" bin="swaydesk-caffeine-popup" src="rust/caffeine-popup" tech="rust" off="bar.caffeine" >}}Evita que la pantalla se bloquee y que la computadora se suspenda durante 1 hora, 2 horas o siempre.{{< /component >}}

{{< component title="Centro de notificaciones" shot="notifications" keys="`Super`+`C`; haz clic en la campana" guide="/en-us/guide/desktop/#notifications" bin="swaydesk-notifications-popup" src="rust/notifications-popup" tech="rust" off="bar.notifications" >}}Las notificaciones agrupadas por aplicación, con sus acciones, y No molestar.{{< /component >}}

{{< component title="Portapapeles" shot="clipboard" keys="`Super`+`V`" guide="/en-us/guide/desktop/#clipboard-history" bin="swaydesk-clipboard-popup" src="rust/clipboard-popup" tech="rust" off="clipboard_history" >}}El historial de lo que copiaste, con búsqueda, miniaturas y elementos fijados. Si lo desactivas, no se guarda nada más en el historial.{{< /component >}}

La barra también muestra la distribución del teclado cuando hay dos o más; un clic cambia la distribución. Para quitarla de la barra: `[enabled.bar] language = false`. En Arch, también muestra el número de actualizaciones, cuando las hay; `[enabled.bar] updates = false` lo quita.


## Ventanas y aplicaciones

{{< component title="Dock" shot="desktop" keys="Empuja el puntero contra el borde inferior" guide="/en-us/guide/desktop/#the-dock" bin="swaydesk-dock" src="rust/dock" tech="rust" off="dock" >}}Aplicaciones fijadas y abiertas, con un menú de clic derecho. Se oculta cuando una ventana necesita el espacio, o se queda visible.{{< /component >}}

{{< component title="Cuadrícula de aplicaciones" shot="drawer" keys="`Super`" guide="/en-us/guide/desktop/#the-app-grid" bin="swaydesk-drawer" src="rust/drawer" tech="rust" off="app_grid" >}}Todas las aplicaciones instaladas, con búsqueda, grupos y favoritos. La búsqueda también encuentra archivos, hace cálculos y convierte unidades.{{< /component >}}

{{< component title="Lanzador" shot="launcher-apps" keys="`Alt`+`Space`" guide="/en-us/guide/desktop/#the-launcher" bin="sway-launcher (rofi)" src="home/.local/bin/sway-launcher" tech="script" >}}rofi con cuatro pestañas: aplicaciones, ventanas abiertas, portapapeles y búsqueda web (con prefijos como `w` para Wikipedia). Un clic abre una entrada, y un clic afuera lo cierra.{{< /component >}}

{{< component title="Selector de ventanas" shot="switcher" keys="`Alt`+`Tab`" guide="/en-us/guide/desktop/#switching-windows" bin="swaydesk-switcher" src="rust/switcher" tech="rust" off="switcher" >}}Las ventanas en el orden en que las usaste, de todos los espacios de trabajo, en una tarjeta en el centro de la pantalla.{{< /component >}}


## Sesión

{{< component title="Notificaciones" guide="/en-us/guide/desktop/#notifications" bin="swaydesk-notifd" src="rust/notifd" tech="rust" off="notifications" >}}El servicio que recibe las notificaciones de las aplicaciones y muestra los avisos emergentes en la esquina.{{< /component >}}

{{< component title="Indicador de volumen y brillo" shot="osd" keys="Teclas de volumen y brillo" bin="swaydesk-osd-bar" src="rust/osd-bar" tech="rust" off="osd" >}}Icono, barra y porcentaje en pantalla durante un segundo.{{< /component >}}

{{< component title="Menú de la sesión" shot="session" keys="`Ctrl`+`Alt`+`Delete`; el botón de apagado de la barra" guide="/en-us/guide/desktop/#session-menu" bin="swaydesk-session-menu" src="rust/session-menu" tech="rust" >}}Bloquear, cerrar sesión, suspender, reiniciar y apagar. Cuando una aplicación pide reiniciar o apagar, como el **Reiniciar y actualizar** de la tienda, pregunta antes, con una cuenta regresiva de 60 segundos y un botón para cancelar.{{< /component >}}

{{< component title="Pantalla de bloqueo" shot="lock" keys="`Ctrl`+`Alt`+`L`; sola después de 10 minutos" guide="/en-us/guide/desktop/#lock-screen-and-idle" bin="swaydesk-lock" src="rust/lock" tech="rust" >}}Hora, fecha y el campo de contraseña en cada monitor, sobre el fondo de pantalla difuminado. Necesita gtk4-layer-shell 1.2; antes de eso, como en Debian 13, swaylock bloquea la pantalla.{{< /component >}}

{{< component title="Pantalla de inicio de sesión" shot="greeter" guide="/en-us/guide/first-steps/#the-swaydesk-login-screen" bin="swaydesk-greeter" src="rust/greeter" tech="rust" >}}Una pantalla de inicio de sesión sobre greetd, con el mismo aspecto que la pantalla de bloqueo, en todas las distribuciones compatibles, Arch incluido. Desbloquea el llavero con tu contraseña de inicio de sesión. La pantalla de inicio de sesión que ya usas también funciona; sin una, como en una instalación mínima o de servidor, esta es la que te da un inicio de sesión gráfico.{{< /component >}}

{{< component title="Llavero" guide="/en-us/guide/desktop/#passwords-and-keyring" bin="swaydesk-keyring" src="rust/keyring" tech="rust" >}}gnome-keyring guarda las contraseñas de las aplicaciones y se desbloquea cuando inicias sesión. En Debian 13, el primer inicio de sesión de cada usuario muestra un aviso y pide la contraseña una vez; desde entonces, el llavero se desbloquea solo. En Ubuntu y Arch, no pide nada.{{< /component >}}

{{< component title="Contraseña de administrador" keys="Cuando una aplicación pide permiso" guide="/en-us/guide/desktop/#passwords-and-keyring" bin="sway-polkit-agent (mate-polkit)" src="home/.local/bin/sway-polkit-agent" tech="script" off="polkit_agent" >}}Inicia el agente de polkit: la ventana que pide tu contraseña para acciones de administrador, como montar un disco. Si no hay ningún agente instalado, una notificación lo avisa.{{< /component >}}

{{< component title="Aviso de actualizaciones" keys="Al iniciar sesión" bin="sway-update-notifier" src="home/.local/bin/sway-update-notifier" tech="script" off="update_notifier" >}}Inicia el aviso de actualizaciones de la distribución, que Sway no inicia por sí solo: el de GNOME Software, el Actualizador de software de Ubuntu o el de Discover. En Arch, Swaydesk tiene su propio aviso, con un icono en la barra: los repositorios oficiales, el AUR (a través de paru o yay, si están instalados), las aplicaciones Flatpak y el firmware; mira [Actualizaciones en Arch](/en-us/guide/config/#updates-on-arch). Nada se actualiza por sí solo.{{< /component >}}

{{< component title="Luz nocturna" keys="En la ventana emergente de brillo" guide="/en-us/guide/desktop/#the-bar" bin="sway-nightlight (gammastep)" src="home/.local/bin/sway-nightlight" tech="script" off="nightlight" >}}Calienta los colores de noche con gammastep, y vuelve en su último modo cuando inicias sesión.{{< /component >}}

{{< component title="Fondo de pantalla del día" keys="Al iniciar sesión" bin="bing-wallpaper" src="home/.local/bin/bing-wallpaper" tech="script" off="bing_wallpaper" >}}Descarga la imagen del día de Bing y la pone como fondo de pantalla.{{< /component >}}


## Aplicaciones propias

{{< component title="Tema del escritorio" shot="theme" keys="En la cuadrícula de aplicaciones" guide="/en-us/guide/config/" bin="swaydesk-theme-app" src="rust/theme-app" tech="rust" >}}Elige el tema GTK, los iconos y el color de acento, y los aplica todos a la vez, incluidas las aplicaciones GTK y libadwaita. De forma predeterminada, el color de acento sigue al fondo de pantalla, incluido el del día (**Usar el color del fondo de pantalla**); elegir un color tú mismo lo desactiva.{{< /component >}}

{{< component title="Pantallas" shot="displays" keys="En la cuadrícula de aplicaciones" guide="/en-us/guide/config/#displays" bin="swaydesk-displays" src="rust/displays" tech="rust" off="displays" >}}Tus pantallas en un mapa, para arrastrarlas, con la resolución, la frecuencia de actualización, la escala y la rotación de cada una, y si está encendida. Un cambio se deshace solo después de 15 segundos, a menos que lo conserves. Cada conjunto de monitores guarda su propia disposición, que se aplica cuando conectas o desconectas una pantalla, y la pantalla de la laptop se apaga con la tapa cerrada y un monitor externo encendido. La clave desactiva solo estos perfiles automáticos; la aplicación se queda.{{< /component >}}

{{< component title="Ayuda" shot="help" keys="`Super`+`F1`; `Super`+`/`" guide="shortcuts/" bin="swaydesk-help" src="rust/help" tech="rust" >}}Los atajos del perfil en uso, con búsqueda, leídos de la propia configuración de Sway, y una tarjeta para cada parte del escritorio, con su atajo y un botón que la abre. También es donde cambias el perfil de atajos y abres tu `50-local.conf` para editarlo.{{< /component >}}

{{< component title="Perfiles de atajos" keys="En la Ayuda; o `shortcuts` en `config.toml`" guide="shortcuts/" src="home/.config/sway/keys/" tech="Sway" >}}Los atajos de Swaydesk, i3, Hyprland, niri o dwm (que usa `Alt` como modificador), todos con 9 espacios de trabajo. El cambio se aplica al instante, sin cerrar sesión, y tu `50-local.conf` tiene prioridad sobre cualquier perfil.{{< /component >}}

{{< component title="Captura de pantalla" shot="capture" keys="`Super`+`Shift`+`E`; `Print`" guide="/en-us/guide/desktop/#screenshots-and-recording" bin="swaydesk-capture" src="rust/capture" tech="rust" >}}Una región, la pantalla completa o una ventana, con retardo. Va al portapapeles y a `~/Pictures/Screenshots`; con Gradia, se abre para editarla.{{< /component >}}

{{< component title="Grabación de pantalla" shot="recording" keys="`Super`+`Shift`+`R`" guide="/en-us/guide/desktop/#screenshots-and-recording" bin="swaydesk-capture" src="rust/capture" tech="rust" >}}Una región, la pantalla completa o una ventana, con el sonido del sistema, el micrófono o sin audio. El video va a `~/Videos/Screencasts`.{{< /component >}}

{{< component title="Configuración del escritorio" keys="En la terminal" guide="/en-us/guide/config/" bin="swaydesk-desktop-config" src="rust/desktop-config" tech="rust" >}}Lee `~/.config/sway-desktop/config.toml` y escribe los archivos que usan Sway, la barra y las aplicaciones. Después de editar el archivo a mano, `swaydesk-desktop-config apply` escribe todo y recarga Sway; `swaydesk-desktop-config generate` solo escribe los archivos.{{< /component >}}


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
| swaylock | La pantalla de bloqueo de reserva; en Debian 13, la que se usa |

Las imágenes de instalación también traen una tienda de aplicaciones, GNOME Software, con Flathub. En Debian y Ubuntu también instala y actualiza los paquetes de la distribución y el firmware; en Arch se encarga de las aplicaciones Flatpak, y el aviso de Swaydesk se encarga del resto. Con los paquetes, instala `gnome-software` tú mismo si lo quieres.
