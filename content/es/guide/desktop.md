---
title: El escritorio
prompt: "man swaydesk-dock"
crumb: guide/desktop
weight: 2
description: Un recorrido por la barra, las ventanas emergentes, la dock, la cuadrícula de aplicaciones y el resto de la sesión.
---
Cada pieza de Swaydesk es un programa propio, con el mismo aspecto y el mismo color de acento. Los atajos de teclado de todas están en la página de [atajos](/es/shortcuts/).

## La barra

La barra está en la parte superior de cada monitor. Los espacios de trabajo del 1 al 9 están a la izquierda, y los vacíos aparecen atenuados. El clima y el reloj están en el centro, y los iconos del sistema, a la derecha.

Los iconos abren ventanas emergentes justo debajo de la barra. Abrir una cierra cualquier otra, y se cierra al hacer clic otra vez en el icono, al presionar `Esc`, al hacer clic afuera o al cambiar de espacio de trabajo. Pasa el puntero sobre un icono para ver un resumen rápido.

- **Red:** activa y desactiva el Wi-Fi, lista las redes Wi-Fi, las conexiones cableadas y las VPN, conecta, desconecta y muestra los detalles de la conexión activa (IP, puerta de enlace, DNS, señal). Haz clic en una red para conectarte. Funciona con NetworkManager y, sin él, con iwd para el Wi-Fi y systemd-networkd para el cable; en ese caso no hay VPN ni editor de conexiones. El clic central abre el editor de conexiones de NetworkManager.
- **Bluetooth:** activa el Bluetooth y la visibilidad, lista los dispositivos vinculados, conecta, desconecta, busca y vincula dispositivos nuevos, olvida un dispositivo y envía archivos. La búsqueda solo se ejecuta cuando la pides y se detiene sola después de 30 segundos. Los códigos de vinculación aparecen en un diálogo de blueman, y la ventana emergente sigue abierta hasta que termina la vinculación. El clic central abre el administrador de blueman.
- **Audio:** volumen y silencio de la salida y del micrófono, y la elección del dispositivo de salida y de entrada, con el actual en el color de acento. Desplaza la rueda sobre el icono para cambiar el volumen, haz clic derecho para silenciar y clic central para abrir `pavucontrol`.
- **Batería:** carga, tiempo restante, consumo, salud de la batería, un gráfico de las últimas 12 horas, los perfiles de energía y la batería de otros dispositivos, como unos auriculares o un ratón. El clic derecho cambia el perfil de energía, y el clic central muestra el estado en una notificación.
- **Brillo y luz nocturna:** el control deslizante del brillo y la luz nocturna, que hace la pantalla más cálida: apagada, encendida todo el tiempo o solo en el horario que elijas. Desplaza la rueda sobre el icono para cambiar el brillo.
- **Cafeína:** mientras está activada, la pantalla no se bloquea ni se apaga y la computadora no se suspende por inactividad. Elige 1 hora, 2 horas o siempre. El clic derecho la activa y la desactiva. Cerrar la tapa igual bloquea.
- **Multimedia:** el icono solo aparece cuando algo se está reproduciendo o está en pausa. La ventana emergente tiene la portada, la pista, el progreso y los controles; con más de un reproductor, una fila de botones cambia entre ellos. El clic central reproduce o pausa, y el clic derecho salta a la siguiente pista.
- **Sistema:** CPU, memoria, disco, temperatura y los procesos que más consumen. Puedes terminar uno de tus propios procesos: haz clic en **Terminar** y otra vez para confirmar. El clic derecho abre el monitor del sistema.
- **Clima:** las condiciones actuales, las próximas horas y los próximos tres días, de wttr.in. La ciudad sale de tu dirección IP o de la configuración (mira [Configuración](/es/guide/config/)).
- **Calendario:** haz clic en el reloj para ver el mes, con el día de hoy en el color de acento y los días festivos de tu país. Las flechas y la rueda del ratón cambian el mes, y **Hoy** te lleva de vuelta.
- **Notificaciones y portapapeles:** la campana y el icono del portapapeles abren las ventanas emergentes que se describen más abajo.
- **Teclado:** muestra la distribución actual; haz clic para cambiar a la siguiente.
- **Botón de apagado:** el botón del extremo derecho abre el menú de la sesión.

Cuando cambias el volumen o el brillo con las teclas o con la rueda, aparece un indicador durante un segundo cerca de la parte inferior de la pantalla, encima de la dock.

## La dock

La dock está en la parte inferior, con tus aplicaciones fijadas, luego las abiertas y, al final, el botón de la cuadrícula de aplicaciones. Un punto debajo de un icono indica una ventana abierta, y dos puntos, varias. El punto toma el color de acento cuando esa ventana tiene el foco.

| Acción | Qué pasa |
| --- | --- |
| Clic en una aplicación cerrada | La abre |
| Clic en una aplicación con una ventana | Le da el foco a la ventana, cambiando de espacio de trabajo si hace falta |
| Clic en una aplicación con varias ventanas | Lista sus títulos para que elijas una |
| Clic derecho | Fijar o dejar de fijar, nueva ventana, cerrar o cerrar todas |
| Arrastrar una aplicación fijada | Cambia el orden |

La dock tiene tres modos:

- **Superposición** (`overlap`, el predeterminado): visible, y solo se oculta cuando una ventana necesita su espacio. En la práctica, la verás en un espacio de trabajo vacío o con ventanas flotantes pequeñas.
- **Ocultar automáticamente** (`auto-hide`): oculta hasta que empujas el puntero contra el centro del borde inferior.
- **Siempre** (`always`): siempre visible, con las ventanas por encima.

El modo, el tamaño de los iconos y qué monitores tienen dock se configuran en `~/.config/sway-dock/config.toml` (mira [Configuración](/es/guide/config/)). La dock no aparece sobre una ventana en pantalla completa.

## La cuadrícula de aplicaciones

Presiona y suelta `Super` para abrir la cuadrícula, o haz clic en el botón de la dock. Muestra todas las aplicaciones instaladas, incluidas las de Flatpak y Snap.

- **Búsqueda:** solo empieza a escribir. La búsqueda mira los nombres, las descripciones y las palabras clave de las aplicaciones, y también encuentra archivos en tus carpetas, que aparecen debajo de la cuadrícula. Un cálculo como `2*21` muestra el resultado, y `Enter` lo copia. Con `qalc` instalado, también convierte unidades, como en `5 km to mi`.
- **Grupos:** la fila inferior tiene **Inicio**, con todas las aplicaciones, y tus grupos. Los primeros son Oficina, Sistema y Utilidades. Crea uno con **Añadir grupo**, y haz clic derecho en una aplicación para agregarla a un grupo o sacarla. `Ctrl`+`Page Up` y `Ctrl`+`Page Down` pasan de un grupo a otro.
- **Favoritos:** haz clic derecho en una aplicación y elige **Añadir a favoritos**. Los favoritos están arriba de todo en Inicio.
- **Dock:** haz clic derecho en una aplicación y elige **Fijar en la dock**.

`Esc`, un clic lejos de los iconos o abrir una aplicación cierra la cuadrícula.

## El lanzador

`Alt`+`Space` abre el lanzador, un campo de búsqueda en el centro de la pantalla con cuatro pestañas: aplicaciones, ventanas abiertas, el historial del portapapeles y la web. `Tab` pasa de una pestaña a otra, y `Enter` abre el elemento seleccionado. `Super`+`` ` `` (la tecla a la izquierda del 1) va directo a la lista de ventanas. El mismo atajo cierra el lanzador.

En la pestaña **Web**, lo que escribes se convierte en una búsqueda. Un prefijo y un espacio eligen el sitio: `g` Google, `d` DuckDuckGo, `w` Wikipedia, `yt` YouTube, `gt` Google Translate, `cl` Claude y `gpt` ChatGPT. Algo que parece una dirección, como `kde.org`, se abre directamente, y el texto simple va a Google. Tu texto solo va a un servicio de IA (Claude o ChatGPT) cuando escribes el prefijo `cl` o `gpt`. Puedes agregar tus propias búsquedas y cambiar la predeterminada en [la configuración del lanzador](/es/guide/config/#búsquedas-del-lanzador).

## Cambiar de ventana

`Alt`+`Tab` cambia de ventana en el orden en que las usaste, como en KDE y GNOME. Mientras mantienes `Alt` presionada, una tarjeta en el centro de la pantalla muestra el icono, el título y el espacio de trabajo de cada ventana. Cada `Tab` avanza un paso, y al soltar `Alt` la ventana seleccionada recibe el foco, cambiando de espacio de trabajo si hace falta. `Esc` cancela.

Un toque rápido vuelve directo a la ventana que usaste antes, sin mostrar la tarjeta. `Alt`+`Shift`+`Tab` empieza por la más antigua.

## Notificaciones

Las notificaciones aparecen en la esquina superior derecha y desaparecen después de 10 segundos (las críticas se quedan hasta que las cierras). Hacer clic en una notificación ejecuta la acción predeterminada de la aplicación.

La campana de la barra muestra un punto cuando hay notificaciones. Haz clic en ella, o presiona `Super`+`C`, para abrir el centro de notificaciones: las notificaciones agrupadas por aplicación, con **Borrar** para cada grupo y **Borrar todo**.

**No molestar** está en el centro de notificaciones: desactivado, durante 1 hora, durante 2 horas o hasta que lo desactives. Mientras está activado, solo aparecen las notificaciones críticas; las demás van directo al centro. Haz clic derecho en la campana para activarlo o desactivarlo.

La lista solo vive en la memoria: no se escribe nada en el disco, y desaparece cuando cierras la sesión.

## Historial del portapapeles

Swaydesk guarda un historial de lo que copias: texto, imágenes y otro contenido de hasta 5 MB. `Super`+`V`, o el icono de la barra, lo abre.

- Escribe para buscar en el texto completo de cada elemento. Las flechas eligen un elemento, y `Enter` lo copia, listo para pegar.
- Las imágenes muestran una miniatura.
- Los botones de cada elemento lo fijan o lo borran del historial. Los elementos fijados se quedan arriba y sobreviven cuando borras el historial.
- **Borrar historial** te pide hacer clic otra vez para confirmar.

## Menú de la sesión

`Ctrl`+`Alt`+`Delete`, o el botón de apagado de la barra, abre el menú de la sesión en el centro de la pantalla: **Bloquear**, **Cerrar sesión**, **Suspender**, **Reiniciar** y **Apagar**, también con las teclas `L`, `E`, `S`, `R` y `P`. Las flechas y `Tab` pasan de un botón a otro, y `Esc` o un clic afuera cierra el menú. No hay confirmación: hacer clic en **Apagar** apaga. Cuando una aplicación pide reiniciar o apagar, como el **Reiniciar y actualizar** de la tienda, Swaydesk pregunta antes, con una cuenta regresiva de 60 segundos y un botón para cancelar; si cancelas no se instala nada y la actualización queda descargada.

## Pantalla de bloqueo e inactividad

`Ctrl`+`Alt`+`L` bloquea la pantalla. La pantalla de bloqueo muestra la hora y la fecha sobre una copia desenfocada de tu fondo de pantalla, con un campo de contraseña en cada monitor. En el monitor principal, también muestra la batería, la red, la distribución del teclado (haz clic para cambiarla) y lo que se esté reproduciendo.

Esta pantalla de bloqueo necesita gtk4-layer-shell 1.2 o posterior. En un sistema con una versión anterior, como Debian 13, el swaylock más sencillo bloquea la pantalla en su lugar. De cualquier forma, si la pantalla de bloqueo falla, swaylock toma su lugar, así que la pantalla nunca queda desbloqueada.

Cuando no estás, la computadora:

- bloquea la pantalla después de 10 minutos;
- apaga la pantalla después de 15 minutos;
- se suspende después de 30 minutos, solo con batería y solo si no se está reproduciendo ningún sonido.

También bloquea antes de suspenderse. Cafeína, en la barra, detiene todo esto mientras está activada. Si la pantalla se queda oscura después de apagarse, `Super`+`Shift`+`O` la vuelve a encender, incluso con la sesión bloqueada.

## Capturas de pantalla y grabación

`Print` captura una región, y hay atajos para toda la pantalla y para una ventana. Las capturas van a `~/Pictures/Screenshots` y al portapapeles, y aparecen en una notificación. Si Gradia está instalado, puedes abrir la captura en él para hacer anotaciones.

`Super`+`Shift`+`E` abre el panel de captura de pantalla y `Super`+`Shift`+`R` el panel de grabación, con opciones de retraso y de sonido. Mientras grabas, la barra muestra el tiempo transcurrido en rojo; haz clic en él, o presiona el atajo otra vez, para detener. Los videos van a `~/Videos/Screencasts`. Las teclas de los paneles están en la página de [atajos](/es/shortcuts/).

## Compartir pantalla

Compartir la pantalla funciona a través del portal, como en otros escritorios. Cuando una aplicación, como tu navegador durante una llamada, pide compartir la pantalla, el puntero se convierte en una cruz: haz clic en el monitor que quieres mostrar.

Los navegadores basados en Chromium abren una barra "… está compartiendo tu pantalla" cuyos botones no responden en Sway. Swaydesk la esconde; para dejar de compartir, usa el botón de la propia página web. `Super`+`Z` vuelve a mostrar la barra si la necesitas.

## Contraseñas y llavero

- **Llavero:** gnome-keyring guarda las contraseñas de tu navegador, de Git y de otras aplicaciones, y se desbloquea cuando inicias sesión. Si el primer inicio de sesión lo creó sin desbloquearlo, Swaydesk te pide la contraseña una vez, y los siguientes inicios de sesión lo desbloquean solos.
- **Acciones de administrador:** cuando una aplicación necesita permiso, por ejemplo para montar un disco, una ventana te pide la contraseña. Viene del agente de polkit; si no hay ninguno instalado, una notificación te avisa.
- **Contraseñas de Wi-Fi:** con NetworkManager, la ventana de contraseña es la de `nm-applet`. Con iwd, escribes la contraseña de una red nueva directamente en la ventana emergente de red.
