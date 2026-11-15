---
title: Componentes
prompt: "ls /usr/bin/swaydesk-*"
crumb: components
aliases: ["/pt-br/apps/"]
description: As peças do Swaydesk, uma por uma.
---
O Swaydesk é feito de componentes próprios, quase todos escritos em Rust com GTK 4. Cada um tem o seu atalho e uma parte no [guia](/pt-br/guide/). Em breve, cada componente poderá ser desligado na configuração.


## Barra e popups

{{< component title="Rede" keys="Clique no ícone de rede" guide="guide/desktop/#a-barra" bin="swaydesk-network-popup" tech="rust" >}}Wi-Fi, cabo e VPN: liga e desliga, conecta, pede a senha e mostra os detalhes. Funciona com o NetworkManager e também com o iwd e o systemd-networkd.{{< /component >}}

{{< component title="Bluetooth" keys="Clique no ícone de Bluetooth" guide="guide/desktop/#a-barra" bin="swaydesk-bluetooth-popup" tech="rust" >}}Liga o Bluetooth, procura aparelhos, pareia, conecta, esquece e envia arquivos.{{< /component >}}

{{< component title="Áudio" shot="audio" keys="Clique no volume (clique do meio: pavucontrol)" guide="guide/desktop/#a-barra" bin="swaydesk-audio-popup" tech="rust" >}}Volume e mudo da saída e do microfone, e a escolha de cada dispositivo.{{< /component >}}

{{< component title="Bateria" keys="Clique na bateria" guide="guide/desktop/#a-barra" bin="swaydesk-battery-popup" tech="rust" >}}Carga, tempo restante, consumo, saúde, um gráfico das últimas 12 horas e o perfil de energia.{{< /component >}}

{{< component title="Brilho e luz noturna" keys="Clique no ícone de brilho; teclas de brilho" guide="guide/desktop/#a-barra" bin="swaydesk-brightness-popup" tech="rust" >}}O brilho da tela e a luz noturna: desligada, ligada ou no horário que você escolher.{{< /component >}}

{{< component title="Mídia" keys="Clique no ícone de mídia (só aparece com algo tocando)" guide="guide/desktop/#a-barra" bin="swaydesk-media-popup" tech="rust" >}}Capa, título, progresso e os controles do player que estiver tocando.{{< /component >}}

{{< component title="Clima" keys="Clique na temperatura" guide="guide/desktop/#a-barra" bin="swaydesk-weather-popup" tech="rust" >}}A previsão do dia e dos próximos, da cidade escolhida ou da que vem pelo seu IP.{{< /component >}}

{{< component title="Calendário" shot="calendar" keys="Clique na data" guide="guide/desktop/#a-barra" bin="swaydesk-calendar" tech="rust" >}}O mês, com os feriados do seu país.{{< /component >}}

{{< component title="Sistema" keys="Clique no ícone do sistema" guide="guide/desktop/#a-barra" bin="swaydesk-system-popup" tech="rust" >}}CPU, memória, disco, temperatura e os processos que mais consomem, com "Encerrar". O ícone fica laranja quando algo aperta.{{< /component >}}

{{< component title="Cafeína" keys="Clique na xícara" guide="guide/desktop/#a-barra" bin="swaydesk-caffeine-popup" tech="rust" >}}Impede o bloqueio e a suspensão por 1 hora, 2 horas ou sempre.{{< /component >}}

{{< component title="Central de notificações" shot="notifications" keys="`Super`+`C`; clique no sino" guide="guide/desktop/#notificações" bin="swaydesk-notifications-popup" tech="rust" >}}As notificações por app, com as ações de cada uma e o Não perturbe.{{< /component >}}

{{< component title="Área de transferência" shot="clipboard" keys="`Super`+`V`" guide="guide/desktop/#área-de-transferência" bin="swaydesk-clipboard-popup" tech="rust" >}}O histórico do que você copiou, com busca, miniaturas e itens fixados.{{< /component >}}


## Janelas e apps

{{< component title="Dock" shot="desktop" keys="Empurre o ponteiro para a borda de baixo" guide="guide/desktop/#a-dock" bin="swaydesk-dock" tech="rust" >}}Os apps fixados e os abertos, com menu no clique direito. Some quando uma janela precisa do espaço, ou fica sempre à vista.{{< /component >}}

{{< component title="Grade de apps" shot="drawer" keys="`Super`" guide="guide/desktop/#a-grade-de-apps" bin="swaydesk-drawer" tech="rust" >}}Todos os apps instalados, com busca, grupos e favoritos. A busca também faz contas, e com o `qalc` converte unidades.{{< /component >}}

{{< component title="Lançador" keys="`Alt`+`Espaço`" guide="guide/desktop/#o-lançador" bin="sway-launcher (rofi)" tech="script" >}}O rofi com quatro abas: apps, janelas abertas, área de transferência e busca na web (com prefixos como `w` para a Wikipédia).{{< /component >}}

{{< component title="Troca de janelas" shot="switcher" keys="`Alt`+`Tab`" guide="guide/desktop/#troca-de-janelas" bin="swaydesk-switcher" tech="rust" >}}As janelas na ordem de uso, de todos os workspaces, num cartão no meio da tela.{{< /component >}}


## Sessão

{{< component title="Notificações" guide="guide/desktop/#notificações" bin="swaydesk-notifd" tech="rust" >}}O serviço que recebe as notificações dos apps e mostra os avisos no canto da tela.{{< /component >}}

{{< component title="Indicador de volume e brilho" keys="Teclas de volume e de brilho" bin="swaydesk-osd-bar" tech="rust" >}}Ícone, barra e porcentagem no meio da tela por um segundo.{{< /component >}}

{{< component title="Menu de sessão" shot="session" keys="`Ctrl`+`Alt`+`Delete`; botão de energia da barra" guide="guide/desktop/#menu-de-sessão" bin="swaydesk-session-menu" tech="rust" >}}Bloquear, sair, suspender, reiniciar e desligar.{{< /component >}}

{{< component title="Bloqueio de tela" keys="`Ctrl`+`Alt`+`L`; sozinho depois de 10 minutos" guide="guide/desktop/#bloqueio-e-inatividade" bin="swaydesk-lock" tech="rust" >}}Hora, data e o campo de senha em todos os monitores, sobre o papel de parede desfocado. Precisa do gtk4-layer-shell 1.2; antes dele, como no Debian 13, quem bloqueia é o swaylock.{{< /component >}}

{{< component title="Tela de login (opcional)" shot="greeter" guide="guide/first-steps/#opcional-a-tela-de-login-do-swaydesk" bin="swaydesk-greeter" tech="rust" >}}Uma tela de login sobre o greetd, com o mesmo visual da tela de bloqueio. A que você já usa também serve.{{< /component >}}

{{< component title="Luz noturna" keys="No popup de brilho" guide="guide/desktop/#a-barra" bin="sway-nightlight (gammastep)" tech="script" >}}Deixa as cores mais quentes à noite, pelo gammastep, e volta ao último modo no login.{{< /component >}}

{{< component title="Papel de parede do dia" keys="No login" bin="bing-wallpaper" tech="script" >}}Baixa a imagem do dia do Bing e a usa como papel de parede.{{< /component >}}


## Apps próprios

{{< component title="Tema do Desktop" shot="theme" keys="Na grade de apps" guide="guide/config/" bin="swaydesk-theme-app" tech="rust" >}}Escolhe o tema GTK, os ícones e a cor de destaque, e aplica tudo de uma vez, também nos apps GTK e libadwaita.{{< /component >}}

{{< component title="Captura de tela" shot="capture" keys="`Super`+`Shift`+`E`; `Print`" guide="guide/desktop/#capturas-e-gravação" bin="swaydesk-capture" tech="rust" >}}Região, tela inteira ou janela, com atraso. Vai para a área de transferência e para `~/Imagens/Screenshots`; com o Gradia, abre para editar.{{< /component >}}

{{< component title="Gravação de tela" keys="`Super`+`Shift`+`R`" guide="guide/desktop/#capturas-e-gravação" bin="swaydesk-capture" tech="rust" >}}Região, tela inteira ou janela, com o som do sistema, o microfone ou sem áudio. O vídeo vai para `~/Vídeos/Screencasts`.{{< /component >}}

{{< component title="Telas" keys="Na grade de apps" bin="swaydesk-displays" tech="rust" soon="true" >}}A posição, a resolução, a escala e a rotação de cada monitor. Até ele chegar, o nwg-displays faz o mesmo.{{< /component >}}

{{< component title="Ajuda" keys="Na grade de apps" bin="swaydesk-help" tech="rust" soon="true" >}}Os atalhos de teclado da sessão, com busca, tirados da própria configuração do Sway.{{< /component >}}


## Apps que acompanham

| App | Para quê |
| --- | --- |
| kitty | Terminal (`Ctrl`+`Alt`+`T`) |
| Thunar | Gerenciador de arquivos (`Ctrl`+`Alt`+`E`) |
| rofi | O lançador (`Alt`+`Espaço`) |
| Blueman | Pareamento do Bluetooth (os pedidos de PIN e confirmação) |
| pavucontrol | Ajustes finos de áudio, além do popup da barra (clique do meio no volume) |
