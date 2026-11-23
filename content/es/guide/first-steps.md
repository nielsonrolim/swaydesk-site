---
title: Primeros pasos
prompt: "swaydesk-desktop-config setup"
crumb: guide/first-steps
weight: 1
description: Cómo iniciar sesión en Swaydesk y qué hacer la primera vez.
---
Con los paquetes instalados, Swaydesk aparece como una sesión más en la pantalla de inicio de sesión. El escritorio que ya tenías sigue ahí, y los dos mantienen su configuración por separado.

## Iniciar sesión

Si ya usas una pantalla de inicio de sesión, como la de GNOME (GDM), la de KDE (SDDM) o la de Mint y Xfce (LightDM), **no hay nada que hacer más que elegir la sesión**. Swaydesk aparece ahí como una opción más, y el escritorio que ya tenías se queda:

- **GDM:** haz clic en tu nombre y, antes de escribir la contraseña, en el icono del engranaje de la esquina inferior derecha;
- **SDDM:** usa el menú de sesión de la esquina inferior izquierda;
- **LightDM:** usa el icono o el menú de sesión (en Mint, junto a tu nombre; en otros temas, en el panel superior).

Elige **Sway Desktop** y escribe tu contraseña. La pantalla de inicio de sesión recuerda la elección para la próxima vez. Si también ves una sesión llamada solo **Sway**, esa viene del paquete de Sway y no tiene nada de Swaydesk: usa **Sway Desktop**.

### La pantalla de inicio de sesión de Swaydesk

Swaydesk también tiene una pantalla de inicio de sesión propia, el paquete `swaydesk-greeter`, con el mismo aspecto que la pantalla de bloqueo. Con GDM, SDDM o LightDM es opcional. Sin un gestor de inicio de sesión, como en una instalación mínima o de servidor, el sistema arranca en una consola de texto, y es la que te da un inicio de sesión gráfico. Lo que hace:

- lista las cuentas de la computadora con sus imágenes, además de **Otro usuario…** para escribir un nombre;
- recuerda la última cuenta y la sesión de cada persona, con **Sway Desktop** al principio de la lista;
- después de la contraseña, pide lo que el sistema necesite, como un código o una contraseña nueva cuando la anterior venció;
- usa la distribución del teclado y el idioma del sistema, y tiene botones para suspender, reiniciar y apagar.

Funciona sobre greetd. En Debian y Ubuntu, greetd se activa por sí mismo solo cuando la computadora no tiene otra pantalla de inicio de sesión; con GDM, SDDM o LightDM, nada cambia hasta que hagas el cambio:

```
sudo apt install swaydesk-greeter
sudo systemctl disable gdm      # or sddm, or lightdm
sudo systemctl enable greetd
```

En Arch, pacman no activa servicios: después de instalar, ejecuta `sudo systemctl enable greetd`. En todas las distribuciones, las sesiones que abres desde esta pantalla de inicio de sesión usan el servicio PAM propio del paquete, `/etc/pam.d/swaydesk-greeter`, que también desbloquea tu llavero cuando inicias sesión. Si personalizaste `/etc/pam.d/greetd` (un lector de huellas, una llave de seguridad), haz ese cambio en `/etc/pam.d/swaydesk-greeter`.

Para volver a la pantalla de inicio de sesión que tenías, desactiva greetd y activa la otra (`sudo systemctl disable greetd` y `sudo systemctl enable gdm`, por ejemplo). Mira también las [preguntas frecuentes](/es/guide/faq/#cómo-vuelvo-a-la-pantalla-de-inicio-de-sesión-que-usaba-antes).

## Lo que verás

- **La barra de arriba:** los espacios de trabajo del 1 al 9 a la izquierda, el clima y el reloj en el centro, y a la derecha los iconos de la bandeja, el portapapeles, la distribución del teclado, el sistema, el brillo, la cafeína, el Bluetooth, la red, el volumen y la batería, además del botón de apagado. Haz clic en cualquier icono para abrir su ventana emergente.
- **La dock de abajo:** tus aplicaciones fijadas, las abiertas y el botón de la cuadrícula de aplicaciones. Se aparta cuando una ventana necesita su espacio y vuelve cuando empujas el puntero contra el centro del borde inferior.
- **La cuadrícula de aplicaciones:** presiona y suelta `Super` (la tecla del logotipo) para mostrar u ocultar todas las aplicaciones instaladas, con búsqueda.

Los atajos siguen a KDE Plasma con Krohnkite, y puedes cambiarlos por las teclas de i3, Hyprland, niri o dwm. La lista completa, perfil por perfil, está en la página de [atajos](/es/shortcuts/), y hay un recorrido por cada pieza en [El escritorio](/es/guide/desktop/).

## Lo que prepara el primer inicio de sesión

La primera vez que inicias sesión, la sesión copia a tu carpeta personal los archivos que todavía no tienes. Nunca sobrescribe nada, y lo que copia es tuyo para editar:

- `~/.config/swaydesk/config.toml`, la configuración del escritorio: idioma, tema, iconos y color de acento. Si el tema predeterminado no está instalado, empieza con `Adwaita-dark`;
- `~/.config/sway/config.d/50-local.conf`, la configuración de esta computadora, con ejemplos comentados y la distribución del teclado del sistema;
- el primer conjunto de aplicaciones fijadas en la dock: el administrador de archivos y la terminal.

También aplica el tema y el color de acento a las aplicaciones GTK, la barra, la dock y las ventanas emergentes. Mira [Configuración](/es/guide/config/) para los detalles.

**El llavero en Debian 13:** en el primer inicio de sesión de cada usuario, un aviso ("Primer inicio de sesión: escribe tu contraseña una vez para activar el llavero. A partir del próximo inicio de sesión, se abre solo.") va seguido de la petición de contraseña del llavero (**Desbloquear el depósito de claves de inicio**). Escribe tu contraseña de inicio de sesión. Pasa solo una vez: a partir del próximo inicio de sesión, el llavero se abre solo. Es una limitación de gnome-keyring 48 en Debian; Ubuntu 26.04 y Arch no están afectados.

## Lo primero que hacer

- **Tema y color de acento:** abre la aplicación **Tema del escritorio** desde la cuadrícula de aplicaciones. Elige una familia de temas, clara u oscura, y un color; **Aplicar** cambia todo de una vez, y la ventana sigue abierta para que pruebes otra combinación.
- **Pantallas:** abre la aplicación **Pantallas** desde la cuadrícula de aplicaciones para ajustar la posición, la resolución y la escala de tus pantallas. Cada conjunto de monitores guarda tu elección, que vuelve sola cuando conectas las mismas pantallas.
- **Teclado:** Swaydesk empieza con la distribución del sistema. Para usar dos distribuciones, por ejemplo US y US International, edita `50-local.conf` (mira [Configuración](/es/guide/config/)). `Super`+`Space` cambia entre ellas, y el icono del teclado de la barra muestra la actual.
- **Wi-Fi:** haz clic en el icono de red de la barra, elige la red y escribe la contraseña.
- **Bluetooth:** haz clic en el icono de Bluetooth, actívalo y busca para vincular un dispositivo nuevo.
- **Sonido:** haz clic en el icono del volumen para elegir la salida y el micrófono.
