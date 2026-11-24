---
title: Preguntas frecuentes
prompt: "less ~/.local/state/sway/sway.log"
crumb: guide/faq
weight: 4
description: Problemas conocidos y qué hacer con cada uno.
---
## Sesión e inicio de sesión

### Al iniciar sesión vuelvo a la pantalla de inicio de sesión, o la pantalla se pone negra

Inicia sesión en tu otra sesión (GNOME, KDE o la que tengas) y busca el error en `~/.local/state/sway/sway.log`. El registro del intento anterior está al lado, en `sway.log.old`.

### La pantalla de inicio de sesión muestra "Sway" y "Sway Desktop". ¿Cuál elijo?

**Sway Desktop**. La sesión **Sway** viene del paquete de Sway e inicia Sway sin más, sin el entorno que prepara Swaydesk.

### ¿Cómo vuelvo a la pantalla de inicio de sesión que usaba antes?

Sin quitar el paquete `swaydesk-greeter`:

```
sudo mkdir -p /etc/systemd/system/greetd.service.d
sudo ln -s /dev/null /etc/systemd/system/greetd.service.d/swaydesk-greeter.conf
sudo systemctl daemon-reload
```

greetd vuelve a `/etc/greetd/config.toml` en el siguiente arranque. Si usabas GDM o SDDM, desactiva greetd y vuelve a activar el otro con `systemctl`.

### La sesión me pidió la contraseña del llavero en el primer inicio de sesión. ¿Es normal?

Sí, una vez, en Debian 13. Su gnome-keyring 48 crea el llavero en el primer inicio de sesión, pero no lo pone a disposición de las aplicaciones; Swaydesk lo vuelve a abrir y, para eso, muestra un aviso y te pide una vez tu contraseña de inicio de sesión. Después, el llavero se desbloquea solo. Ubuntu 26.04 y Arch no la piden. Mira [los primeros pasos](/es/guide/first-steps/#lo-que-prepara-el-primer-inicio-de-sesión).

## Pantalla y energía

### La pantalla se queda negra después de apagarse por inactividad

Presiona `Super`+`Shift`+`O`: vuelve a encender las pantallas, incluso con la sesión bloqueada.

### Las teclas de brillo no hacen nada

Agrega tu usuario al grupo `video` y vuelve a iniciar sesión:

```
sudo usermod -aG video $USER
```

### Después de algunas contraseñas incorrectas, dice que la cuenta está bloqueada {#cuenta-bloqueada}

Es una regla del propio Arch (pam_faillock): después de tres inicios de sesión fallidos, la cuenta queda bloqueada durante 10 minutos, sudo incluido, y la pantalla de bloqueo muestra el mensaje del sistema con el tiempo que falta. Espera los 10 minutos, o desbloquéala desde otra cuenta de administrador con `sudo faillock --user <tu-usuario> --reset` (o como root en una consola de texto). Debian y Ubuntu no tienen esta regla.

### La dock no aparece

En el modo predeterminado, se oculta cuando una ventana necesita su espacio. Empuja el puntero contra el centro del borde inferior para que aparezca. No aparece sobre una ventana en pantalla completa. Para que esté siempre visible, pon `mode = "always"` en la [configuración de la dock](/es/guide/config/).

## Red, Bluetooth y contraseñas

### Una red con contraseña no se conecta, y nada pide la contraseña

Con NetworkManager, `nm-applet` pide la contraseña. Instala el paquete `network-manager-applet` y vuelve a iniciar sesión.

Con iwd, la contraseña de una red nueva se escribe en la ventana emergente de red, que tiene que quedarse abierta hasta que se conecte.

### Vincular un dispositivo Bluetooth falla, o no aparece ninguna ventana

blueman muestra el código de vinculación. Instala el paquete `blueman` y vuelve a iniciar sesión.

### Una aplicación pidió una contraseña de administrador y no apareció nada

Falta un agente de polkit, y la sesión te lo avisa con una notificación. Instala `mate-polkit` y vuelve a iniciar sesión.

### VS Code dice "An OS keyring couldn't be identified"

VS Code no reconoce Sway y no encuentra el llavero por sí mismo. No aceptes el cifrado más débil que ofrece. En su lugar, agrega esta línea a `~/.vscode/argv.json` y reinicia VS Code:

```
"password-store": "gnome-libsecret"
```

## Aplicaciones y apariencia

### Compartir pantalla no muestra nada para elegir

Reinicia el portal, o cierra sesión y vuelve a iniciarla:

```
systemctl --user restart xdg-desktop-portal
```

Cuando una aplicación pide la pantalla, el puntero se convierte en una mira: haz clic en el monitor que quieres compartir.

### La barra "… está compartiendo tu pantalla" del navegador no responde a los clics

Los botones de esa barra en los navegadores basados en Chromium no funcionan en Sway, así que Swaydesk la aparta. Deja de compartir con el botón de la propia página web. `Super`+`Z` trae la barra de vuelta.

### Una aplicación Flatpak se ve borrosa

Se está ejecutando con XWayland. Usa Flatseal para darle el permiso de Wayland (`--socket=wayland`).

### Las aplicaciones Qt no siguen el tema

Instala `qt5ct` y `qt6ct`. Swaydesk configura ambos con los colores del tema GTK y tu color de acento.

### La aplicación Tema del escritorio dice que el tema configurado no está instalado

Mientras tanto, la sesión usa `Adwaita-dark`. Elige un tema en la aplicación y aplícalo, y el aviso desaparece.

### Cambié el administrador de archivos, pero la dock sigue con el anterior

La dock no cambia las aplicaciones fijadas por sí misma. Quita el anterior de la dock con un clic derecho en ella, y fija el nuevo con un clic derecho en la cuadrícula de aplicaciones.

### El calendario no muestra días festivos

Los días festivos vienen del paquete `python3-holidays`, para el país de la clave `holidays` o, sin ella, el país de tu idioma. Comprueba que el paquete esté instalado y que el país sea el correcto en la [configuración](/es/guide/config/).

### Los textos o el reloj están en el idioma equivocado

Define `locale` en la [configuración del escritorio](/es/guide/config/) y vuelve a iniciar sesión. El idioma tiene que estar generado en el sistema: `locale -a` muestra los que lo están.

### El clima es de otra ciudad

De forma predeterminada, la ciudad viene de tu dirección IP. Define `weather_location` en la [configuración del escritorio](/es/guide/config/) y vuelve a iniciar sesión. El pronóstico anterior puede quedarse hasta 15 minutos.

### La campana de notificaciones se puso roja

El servicio de notificaciones no responde, y las notificaciones se pierden. Normalmente vuelve solo en un segundo. Si no, revisa si otro servicio de notificaciones, como mako o dunst, se está ejecutando en la sesión: solo uno puede funcionar a la vez.

### Elegí una impresora de red y el diálogo se quedó en "Obteniendo información de la impresora…"

Es normal la primera vez: CUPS está creando la cola de la impresora y preguntándole qué puede hacer, lo que tarda hasta unos 30 segundos. Después imprime con normalidad. CUPS elimina esa cola temporal tras un tiempo sin uso, así que la espera puede volver; para evitarlo, agrega la impresora de forma permanente en **Configuración de impresión** (llamada **Impresoras** en Ubuntu), que viene con las ISO.
