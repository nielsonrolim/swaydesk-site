---
title: Componentes
prompt: "ls /usr/bin/swaydesk-*"
crumb: components
aliases: ["/pt-br/apps/"]
description: As peças do Swaydesk, uma por uma.
---
O Swaydesk é feito de componentes próprios, quase todos escritos em Rust com GTK 4. Cada um tem o seu atalho e uma parte no [guia](/pt-br/guide/).

Os atalhos desta página são os do perfil **Swaydesk**, o padrão. Os outros perfis (i3, Hyprland, niri e dwm) mudam boa parte deles: veja todos em [Atalhos](/pt-br/shortcuts/).

Quase todo componente pode ser desligado. A última linha de cada um mostra a chave, que vai no `~/.config/sway-desktop/config.toml`; veja [Ligar e desligar componentes](/pt-br/guide/config/#ligar-e-desligar-componentes).


## Barra e popups

{{< component title="Rede" shot="network" keys="Clique no ícone de rede" guide="guide/desktop/#a-barra" bin="swaydesk-network-popup" src="rust/network-popup" tech="rust" off="bar.network" >}}Wi-Fi, cabo e VPN: liga e desliga, conecta, pede a senha e mostra os detalhes. Funciona com o NetworkManager e também com o iwd e o systemd-networkd (a VPN, só com o NetworkManager).{{< /component >}}

{{< component title="Bluetooth" shot="bluetooth" keys="Clique no ícone de Bluetooth" guide="guide/desktop/#a-barra" bin="swaydesk-bluetooth-popup" src="rust/bluetooth-popup" tech="rust" off="bar.bluetooth" >}}Liga o Bluetooth, procura aparelhos, pareia, conecta, esquece e envia arquivos.{{< /component >}}

{{< component title="Áudio" shot="audio" keys="Clique no volume (clique do meio: pavucontrol)" guide="guide/desktop/#a-barra" bin="swaydesk-audio-popup" src="rust/audio-popup" tech="rust" off="bar.volume" >}}Volume e mudo da saída e do microfone, e a escolha de cada dispositivo.{{< /component >}}

{{< component title="Bateria" shot="battery" keys="Clique na bateria" guide="guide/desktop/#a-barra" bin="swaydesk-battery-popup" src="rust/battery-popup" tech="rust" off="bar.battery" >}}Carga, tempo restante, consumo, saúde, um gráfico das últimas 12 horas e o perfil de energia.{{< /component >}}

{{< component title="Brilho e luz noturna" shot="brightness" keys="Clique no ícone de brilho; teclas de brilho" guide="guide/desktop/#a-barra" bin="swaydesk-brightness-popup" src="rust/brightness-popup" tech="rust" off="bar.brightness" >}}O brilho da tela e a luz noturna: desligada, ligada ou no horário que você escolher.{{< /component >}}

{{< component title="Mídia" shot="media" keys="Clique no ícone de mídia (só aparece com algo tocando)" guide="guide/desktop/#a-barra" bin="swaydesk-media-popup" src="rust/media-popup" tech="rust" off="bar.media" >}}Capa, título, progresso e os controles do player que estiver tocando.{{< /component >}}

{{< component title="Clima" shot="weather" keys="Clique na temperatura" guide="guide/desktop/#a-barra" bin="swaydesk-weather-popup" src="rust/weather-popup" tech="rust" off="bar.weather" >}}A previsão do dia e dos próximos, da cidade escolhida ou da que vem pelo seu IP.{{< /component >}}

{{< component title="Calendário" shot="calendar" keys="Clique na data" guide="guide/desktop/#a-barra" bin="swaydesk-calendar" src="rust/calendar" tech="rust" off="bar.clock" >}}O mês, com os feriados do seu país.{{< /component >}}

{{< component title="Sistema" shot="system" keys="Clique no ícone do sistema" guide="guide/desktop/#a-barra" bin="swaydesk-system-popup" src="rust/system-popup" tech="rust" off="bar.system" >}}CPU, memória, disco, temperatura e os processos que mais consomem, com "Encerrar". O ícone fica laranja quando algo aperta.{{< /component >}}

{{< component title="Cafeína" shot="caffeine" keys="Clique na xícara" guide="guide/desktop/#a-barra" bin="swaydesk-caffeine-popup" src="rust/caffeine-popup" tech="rust" off="bar.caffeine" >}}Impede o bloqueio e a suspensão por 1 hora, 2 horas ou sempre.{{< /component >}}

{{< component title="Central de notificações" shot="notifications" keys="`Super`+`C`; clique no sino" guide="guide/desktop/#notificações" bin="swaydesk-notifications-popup" src="rust/notifications-popup" tech="rust" off="bar.notifications" >}}As notificações por app, com as ações de cada uma e o Não perturbe.{{< /component >}}

{{< component title="Área de transferência" shot="clipboard" keys="`Super`+`V`" guide="guide/desktop/#área-de-transferência" bin="swaydesk-clipboard-popup" src="rust/clipboard-popup" tech="rust" off="clipboard_history" >}}O histórico do que você copiou, com busca, miniaturas e itens fixados. Desligado, nada mais é gravado no histórico.{{< /component >}}

A barra também mostra o layout do teclado, quando há dois ou mais; um clique troca o layout. Para tirá-lo da barra: `[enabled.bar] language = false`.


## Janelas e apps

{{< component title="Dock" shot="desktop" keys="Empurre o ponteiro para a borda de baixo" guide="guide/desktop/#a-dock" bin="swaydesk-dock" src="rust/dock" tech="rust" off="dock" >}}Os apps fixados e os abertos, com menu no clique direito. Some quando uma janela precisa do espaço, ou fica sempre à vista.{{< /component >}}

{{< component title="Grade de apps" shot="drawer" keys="`Super`" guide="guide/desktop/#a-grade-de-apps" bin="swaydesk-drawer" src="rust/drawer" tech="rust" off="app_grid" >}}Todos os apps instalados, com busca, grupos e favoritos. A busca também acha arquivos, faz contas e converte unidades.{{< /component >}}

{{< component title="Lançador" shot="launcher-apps" keys="`Alt`+`Espaço`" guide="guide/desktop/#o-lançador" bin="sway-launcher (rofi)" src="home/.local/bin/sway-launcher" tech="script" >}}O rofi com quatro abas: apps, janelas abertas, área de transferência e busca na web (com prefixos como `w` para a Wikipédia). Um clique abre o item, e um clique fora fecha.{{< /component >}}

{{< component title="Troca de janelas" shot="switcher" keys="`Alt`+`Tab`" guide="guide/desktop/#troca-de-janelas" bin="swaydesk-switcher" src="rust/switcher" tech="rust" off="switcher" >}}As janelas na ordem de uso, de todos os workspaces, num cartão no meio da tela.{{< /component >}}


## Sessão

{{< component title="Notificações" guide="guide/desktop/#notificações" bin="swaydesk-notifd" src="rust/notifd" tech="rust" off="notifications" >}}O serviço que recebe as notificações dos apps e mostra os avisos no canto da tela.{{< /component >}}

{{< component title="Indicador de volume e brilho" shot="osd" keys="Teclas de volume e de brilho" bin="swaydesk-osd-bar" src="rust/osd-bar" tech="rust" off="osd" >}}Ícone, barra e porcentagem no meio da tela por um segundo.{{< /component >}}

{{< component title="Menu de sessão" shot="session" keys="`Ctrl`+`Alt`+`Delete`; botão de energia da barra" guide="guide/desktop/#menu-de-sessão" bin="swaydesk-session-menu" src="rust/session-menu" tech="rust" >}}Bloquear, sair, suspender, reiniciar e desligar.{{< /component >}}

{{< component title="Bloqueio de tela" shot="lock" keys="`Ctrl`+`Alt`+`L`; sozinho depois de 10 minutos" guide="guide/desktop/#bloqueio-e-inatividade" bin="swaydesk-lock" src="rust/lock" tech="rust" >}}Hora, data e o campo de senha em todos os monitores, sobre o papel de parede desfocado. Precisa do gtk4-layer-shell 1.2; antes dele, como no Debian 13, quem bloqueia é o swaylock.{{< /component >}}

{{< component title="Tela de login" shot="greeter" guide="guide/first-steps/#a-tela-de-login-do-swaydesk" bin="swaydesk-greeter" src="rust/greeter" tech="rust" >}}Uma tela de login sobre o greetd, com o mesmo visual da tela de bloqueio, em todas as distros suportadas, o Arch inclusive. Ela abre o chaveiro com a senha do login. A tela de login que você já usa também serve; sem uma, como numa instalação mínima ou de servidor, é ela que dá o login gráfico.{{< /component >}}

{{< component title="Chaveiro" guide="guide/desktop/#senhas-e-chaveiro" bin="swaydesk-keyring" src="rust/keyring" tech="rust" >}}O gnome-keyring guarda as senhas dos apps e abre junto com o login. No Debian 13, o primeiro login de cada usuário mostra um aviso e pede a senha uma vez; nos seguintes, o chaveiro abre sozinho. No Ubuntu e no Arch, não pede nada.{{< /component >}}

{{< component title="Senha de administrador" keys="Quando um app pede permissão" guide="guide/desktop/#senhas-e-chaveiro" bin="sway-polkit-agent (mate-polkit)" src="home/.local/bin/sway-polkit-agent" tech="script" off="polkit_agent" >}}Inicia o agente de polkit: a janela que pede a sua senha nas ações de administrador, como montar um disco. Sem nenhum agente instalado, uma notificação avisa.{{< /component >}}

{{< component title="Aviso de atualizações" keys="No login" bin="sway-update-notifier" src="home/.local/bin/sway-update-notifier" tech="script" off="update_notifier" >}}Inicia o aviso de atualizações da distro, que no Sway não abre sozinho: o do GNOME Software, o Atualizador de Programas do Ubuntu ou o do Discover. Sem nenhum deles, não faz nada.{{< /component >}}

{{< component title="Luz noturna" keys="No popup de brilho" guide="guide/desktop/#a-barra" bin="sway-nightlight (gammastep)" src="home/.local/bin/sway-nightlight" tech="script" off="nightlight" >}}Deixa as cores mais quentes à noite, pelo gammastep, e volta ao último modo no login.{{< /component >}}

{{< component title="Papel de parede do dia" keys="No login" bin="bing-wallpaper" src="home/.local/bin/bing-wallpaper" tech="script" off="bing_wallpaper" >}}Baixa a imagem do dia do Bing e a usa como papel de parede.{{< /component >}}


## Apps próprios

{{< component title="Tema do Desktop" shot="theme" keys="Na grade de apps" guide="guide/config/" bin="swaydesk-theme-app" src="rust/theme-app" tech="rust" >}}Escolhe o tema GTK, os ícones e a cor de destaque, e aplica tudo de uma vez, também nos apps GTK e libadwaita.{{< /component >}}

{{< component title="Telas" shot="displays" keys="Na grade de apps" guide="guide/config/#monitores" bin="swaydesk-displays" src="rust/displays" tech="rust" off="displays" >}}As telas num mapa, para arrastar, com a resolução, a taxa, a escala e a rotação de cada uma, e se ela fica ligada. Uma mudança se desfaz sozinha em 15 segundos, se você não a mantiver. Cada conjunto de monitores guarda o seu layout, aplicado quando você pluga ou despluga uma tela, e a tela do notebook desliga com a tampa fechada e um monitor ligado. A chave desliga só esses perfis automáticos; o app continua.{{< /component >}}

{{< component title="Ajuda" shot="help" keys="`Super`+`F1`; `Super`+`/`" guide="shortcuts/" bin="swaydesk-help" src="rust/help" tech="rust" >}}Os atalhos do perfil em uso, com busca, lidos da própria configuração do Sway, e um cartão para cada parte do desktop, com o atalho e um botão que a abre. Nela você também troca o perfil de atalhos e abre o seu `50-local.conf` para editar.{{< /component >}}

{{< component title="Perfis de atalhos" keys="Na Ajuda; ou `shortcuts` no `config.toml`" guide="shortcuts/" src="home/.config/sway/keys/" tech="Sway" >}}Os atalhos do Swaydesk, do i3, do Hyprland, do niri ou do dwm (que usa o `Alt` como modificador), todos com 9 workspaces. A troca vale na hora, sem sair da sessão, e o seu `50-local.conf` vale por cima de qualquer perfil.{{< /component >}}

{{< component title="Captura de tela" shot="capture" keys="`Super`+`Shift`+`E`; `Print`" guide="guide/desktop/#capturas-e-gravação" bin="swaydesk-capture" src="rust/capture" tech="rust" >}}Região, tela inteira ou janela, com atraso. Vai para a área de transferência e para `~/Imagens/Screenshots`; com o Gradia, abre para editar.{{< /component >}}

{{< component title="Gravação de tela" shot="recording" keys="`Super`+`Shift`+`R`" guide="guide/desktop/#capturas-e-gravação" bin="swaydesk-capture" src="rust/capture" tech="rust" >}}Região, tela inteira ou janela, com o som do sistema, o microfone ou sem áudio. O vídeo vai para `~/Vídeos/Screencasts`.{{< /component >}}

{{< component title="Configuração do desktop" keys="No terminal" guide="guide/config/" bin="swaydesk-desktop-config" src="rust/desktop-config" tech="rust" >}}Lê o `~/.config/sway-desktop/config.toml` e gera os arquivos que o Sway, a barra e os apps usam. Depois de editar o arquivo à mão, `swaydesk-desktop-config apply` grava tudo e recarrega o Sway; `swaydesk-desktop-config generate` só grava os arquivos.{{< /component >}}


## Apps que acompanham

| App | Para quê |
| --- | --- |
| kitty | Terminal (`Ctrl`+`Alt`+`T`) |
| Thunar | Gerenciador de arquivos (`Ctrl`+`Alt`+`E`) |
| rofi | O lançador (`Alt`+`Espaço`) |
| qalc | As contas e as conversões de unidades na busca da grade de apps |
| Blueman | Pareamento do Bluetooth (os pedidos de PIN e confirmação) |
| pavucontrol | Ajustes finos de áudio, além do popup da barra (clique do meio no volume) |
| gammastep | A luz noturna |
| mate-polkit | A janela da senha de administrador (no Debian e no Ubuntu, o lxpolkit também serve) |
| gnome-text-editor | O botão **Abrir** da Ajuda, que edita o `50-local.conf`; sem ele, a Ajuda abre um editor no terminal. Recomendado no Debian e no Ubuntu; opcional no Arch |
| grim, slurp e wf-recorder | A captura e a gravação de tela |
| swaylock | O bloqueio de reserva; no Debian 13, o bloqueio de sempre |
