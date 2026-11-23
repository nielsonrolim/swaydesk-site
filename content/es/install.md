---
title: Instalar
prompt: "sudo apt install swaydesk-desktop"
crumb: install
description: Cómo instalar Swaydesk desde los paquetes, en Debian 13 y testing, Ubuntu 26.04, Linux Mint 27 y Arch Linux.
---
Los paquetes vienen de un repositorio en el [Open Build Service](https://build.opensuse.org/), firmado con la clave del proyecto. El escritorio que ya tienes sigue en la pantalla de inicio de sesión, y las actualizaciones llegan con el `apt upgrade` o el `pacman -Syu` de siempre.

Necesitas Debian 13 o testing, Ubuntu 26.04, Linux Mint 27 o Arch Linux, de 64 bits (x86_64), y una tarjeta gráfica Intel, AMD o NVIDIA con un controlador para Wayland. Elige tu distribución y ejecuta un paso a la vez:

{{< distros >}}
{{< distro id="debian" name="Debian 13" >}}
{{< steps >}}
{{< step text="Instala `curl`, que descarga el paquete del repositorio." >}}
sudo apt install curl
{{< /step >}}
{{< step text="Descarga el paquete `swaydesk-archive-keyring`: agrega el repositorio y la clave del proyecto." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13/all/swaydesk-archive-keyring_2026.11.20_all.deb -o ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Verifica el archivo descargado. El comando debe mostrar `OK`; si no lo hace, detente aquí, borra el archivo y no sigas." >}}
echo "2527bebb378c926e631fb367f2ccb18120cea26617c3a90b859c633cb2845700  $HOME/swaydesk-archive-keyring_2026.11.20_all.deb" | sha256sum -c
{{< /step >}}
{{< step text="Instálalo. Pone la clave en `/usr/share/keyrings/` y el repositorio en `/etc/apt/sources.list.d/swaydesk.sources`, y desde entonces mantiene ambos al día." >}}
sudo dpkg -i ~/swaydesk-archive-keyring_2026.11.20_all.deb && rm ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Opcional, antes del paso 6: mira la huella digital de la clave instalada (requiere `gpg`: `sudo apt install gpg`)." fpr="installed" >}}
gpg --show-keys /usr/share/keyrings/swaydesk-archive-keyring.asc
{{< /step >}}
{{< step text="Actualiza la lista de paquetes e instala Swaydesk." >}}
sudo apt update && sudo apt install swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="Después del paso 1 (curl), los demás pasos encadenados: si el archivo descargado no es el esperado, no se instala nada." >}}
deb=swaydesk-archive-keyring_2026.11.20_all.deb
dir=$(mktemp -d) && curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_13/all/$deb -o "$dir/$deb" &&
echo "2527bebb378c926e631fb367f2ccb18120cea26617c3a90b859c633cb2845700  $dir/$deb" | sha256sum -c && sudo dpkg -i "$dir/$deb" && rm -r "$dir" &&
sudo apt update && sudo apt install swaydesk-desktop
{{< /oneline >}}
{{< /distro >}}
{{< distro id="debian-testing" name="Debian testing" >}}
<p class="distro__note">Rolling release: Swaydesk se prueba en ella en cada versión, pero las actualizaciones de la propia distribución pueden requerir correcciones después.</p>
<p class="distro__note">No hay ISO de Swaydesk para Debian testing: en una instalación desde cero, instala primero Debian testing y luego sigue estos pasos.</p>
{{< steps >}}
{{< step text="Instala `curl`, que descarga el paquete del repositorio." >}}
sudo apt install curl
{{< /step >}}
{{< step text="Descarga el paquete `swaydesk-archive-keyring`: agrega el repositorio y la clave del proyecto." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_Testing/all/swaydesk-archive-keyring_2026.11.20_all.deb -o ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Verifica el archivo descargado. El comando debe mostrar `OK`; si no lo hace, detente aquí, borra el archivo y no sigas." >}}
echo "0fa0971606384baf62a634376006c5b01e52a095795f88c730dc8e07104cb664  $HOME/swaydesk-archive-keyring_2026.11.20_all.deb" | sha256sum -c
{{< /step >}}
{{< step text="Instálalo. Pone la clave en `/usr/share/keyrings/` y el repositorio en `/etc/apt/sources.list.d/swaydesk.sources`, y desde entonces mantiene ambos al día." >}}
sudo dpkg -i ~/swaydesk-archive-keyring_2026.11.20_all.deb && rm ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Opcional, antes del paso 6: mira la huella digital de la clave instalada (requiere `gpg`: `sudo apt install gpg`)." fpr="installed" >}}
gpg --show-keys /usr/share/keyrings/swaydesk-archive-keyring.asc
{{< /step >}}
{{< step text="Actualiza la lista de paquetes e instala Swaydesk." >}}
sudo apt update && sudo apt install swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="Después del paso 1 (curl), los demás pasos encadenados: si el archivo descargado no es el esperado, no se instala nada." >}}
deb=swaydesk-archive-keyring_2026.11.20_all.deb
dir=$(mktemp -d) && curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Debian_Testing/all/$deb -o "$dir/$deb" &&
echo "0fa0971606384baf62a634376006c5b01e52a095795f88c730dc8e07104cb664  $dir/$deb" | sha256sum -c && sudo dpkg -i "$dir/$deb" && rm -r "$dir" &&
sudo apt update && sudo apt install swaydesk-desktop
{{< /oneline >}}
{{< /distro >}}
{{< distro id="ubuntu" name="Ubuntu 26.04 / Mint 27" >}}
{{< steps >}}
{{< step text="Instala `curl`, que descarga el paquete del repositorio." >}}
sudo apt install curl
{{< /step >}}
{{< step text="Descarga el paquete `swaydesk-archive-keyring`: agrega el repositorio y la clave del proyecto." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/xUbuntu_26.04/all/swaydesk-archive-keyring_2026.11.20_all.deb -o ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Verifica el archivo descargado. El comando debe mostrar `OK`; si no lo hace, detente aquí, borra el archivo y no sigas." >}}
echo "a34f455e495c69a2c5dd94ff8ce6dd0618ec569d6b010010c2360432f6029020  $HOME/swaydesk-archive-keyring_2026.11.20_all.deb" | sha256sum -c
{{< /step >}}
{{< step text="Instálalo. Pone la clave en `/usr/share/keyrings/` y el repositorio en `/etc/apt/sources.list.d/swaydesk.sources`, y desde entonces mantiene ambos al día." >}}
sudo dpkg -i ~/swaydesk-archive-keyring_2026.11.20_all.deb && rm ~/swaydesk-archive-keyring_2026.11.20_all.deb
{{< /step >}}
{{< step text="Opcional, antes del paso 6: mira la huella digital de la clave instalada (requiere `gpg`: `sudo apt install gpg`)." fpr="installed" >}}
gpg --show-keys /usr/share/keyrings/swaydesk-archive-keyring.asc
{{< /step >}}
{{< step text="Actualiza la lista de paquetes e instala Swaydesk." >}}
sudo apt update && sudo apt install swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="Después del paso 1 (curl), los demás pasos encadenados: si el archivo descargado no es el esperado, no se instala nada." >}}
deb=swaydesk-archive-keyring_2026.11.20_all.deb
dir=$(mktemp -d) && curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/xUbuntu_26.04/all/$deb -o "$dir/$deb" &&
echo "a34f455e495c69a2c5dd94ff8ce6dd0618ec569d6b010010c2360432f6029020  $dir/$deb" | sha256sum -c && sudo dpkg -i "$dir/$deb" && rm -r "$dir" &&
sudo apt update && sudo apt install swaydesk-desktop
{{< /oneline >}}
<p class="distro__note">En Ubuntu y Mint, las ventanas propias de GTK (como el selector de archivos) necesitan el paquete de idioma de GNOME de tu idioma. Swaydesk muestra un aviso, una sola vez, con el comando; también puedes instalarlo ahora, por ejemplo para el español: <code>sudo apt install language-pack-gnome-es</code>.</p>
{{< /distro >}}
{{< distro id="arch" name="Arch Linux" >}}
<p class="distro__note">Rolling release: Swaydesk se prueba en ella en cada versión, pero las actualizaciones de la propia distribución pueden requerir correcciones después.</p>
{{< steps >}}
{{< step text="Agrega el repositorio al final de `/etc/pacman.conf` (solo una vez)." >}}
sudo tee -a /etc/pacman.conf <<'EOF'

[home_nielsonrolim_Arch]
Server = https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/$arch
EOF
{{< /step >}}
{{< step text="Descarga la clave del repositorio." >}}
curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key -o ~/swaydesk.key
{{< /step >}}
{{< step text="Muestra la huella digital de la clave descargada." fpr="plain" >}}
gpg --show-keys ~/swaydesk.key
{{< /step >}}
{{< step text="Agrega la clave al llavero de pacman y fírmala localmente, para que pacman confíe en ella. El comando primero vuelve a verificar la clave y rechaza cualquier otra, como en el paso 3." >}}
[ "$(gpg --show-keys --with-colons ~/swaydesk.key | grep -E '^(pub|sub|fpr):' | cut -d: -f1,10 | tr '\n' ' ')" = 'pub: fpr:71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 ' ] &&
sudo pacman-key --add ~/swaydesk.key &&
sudo pacman-key --lsign-key 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 &&
rm ~/swaydesk.key
{{< /step >}}
{{< step text="Instala Swaydesk. Si ya tienes `jack2`, pacman pregunta si quieres reemplazarlo por `pipewire-jack`, el JACK de PipeWire, que es el que usa Swaydesk: responde y." >}}
sudo pacman -Syu swaydesk-desktop
{{< /step >}}
{{< /steps >}}
{{< oneline text="Los mismos pasos, encadenados: si la clave descargada no tiene la huella digital correcta, no se agrega ni se instala nada." >}}
key=$(mktemp) && curl -fsSL https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/x86_64/home_nielsonrolim_Arch.key -o "$key" &&
[ "$(gpg --show-keys --with-colons "$key" | grep -E '^(pub|sub|fpr):' | cut -d: -f1,10 | tr '\n' ' ')" = 'pub: fpr:71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 ' ] &&
sudo pacman-key --add "$key" && rm -f "$key" &&
sudo pacman-key --lsign-key 71A5E6CB39B9844E42CE42D35815F0B65BE1CFB9 &&
printf '\n[home_nielsonrolim_Arch]\nServer = https://download.opensuse.org/repositories/home:/nielsonrolim/Arch/$arch\n' | sudo tee -a /etc/pacman.conf >/dev/null &&
sudo pacman -Syu swaydesk-desktop
{{< /oneline >}}
<p class="distro__note">En Arch, el aviso de actualizaciones de Swaydesk se encarga de los repositorios, el AUR, las aplicaciones Flatpak y el firmware, por eso la parte de actualizaciones de la tienda viene desactivada. <a href="/es/guide/config/#actualizaciones-en-arch">Cómo cambiarlo</a>.</p>
{{< /distro >}}
{{< /distros >}}

## Después de instalar

Cierra la sesión y elige **Sway Desktop** en la pantalla de inicio de sesión que ya usas. Los [primeros pasos](/es/guide/first-steps/) explican el resto.

La pantalla de inicio de sesión propia de Swaydesk es opcional si ya tienes una (GDM, SDDM, LightDM). Sin un gestor de inicio de sesión, como en una instalación mínima o de servidor, el sistema arranca en una consola de texto, y es `swaydesk-greeter` el que te da un inicio de sesión gráfico: mira [cómo instalarlo y cómo volver atrás](/es/guide/first-steps/#la-pantalla-de-inicio-de-sesión-de-swaydesk).

## Los paquetes

| Paquete | Qué trae |
| --- | --- |
| `swaydesk-desktop` | La sesión completa, "Sway Desktop" en la pantalla de inicio de sesión, con todos los componentes |
| `swaydesk-greeter` | La pantalla de inicio de sesión de Swaydesk, sobre greetd: opcional con otro gestor de inicio de sesión, necesaria para un inicio de sesión gráfico sin uno |
| `swaydesk-archive-keyring` | Solo Debian, Ubuntu y Mint: la clave y el repositorio, siempre al día |

Los paquetes son de la versión 0.1.4, estable: mira las [notas de la versión](https://github.com/nielsonrolim/swaydesk/releases/tag/v0.1.4) y el [registro de cambios](https://github.com/nielsonrolim/swaydesk/blob/main/CHANGELOG.md). Las versiones nuevas llegan como actualizaciones.
