---
title: O desktop
prompt: "man swaydesk-dock"
crumb: guide/desktop
weight: 2
description: Um passeio pela barra, pelos popups, pela dock, pela grade de apps e pelo resto da sessão.
---
Cada peça do Swaydesk é um programa próprio, com o mesmo visual e a mesma cor de destaque. Os atalhos de todas elas estão em [atalhos](/pt-br/shortcuts/).

## A barra

A barra fica no topo de cada monitor. À esquerda estão os workspaces de 1 a 9: os vazios ficam apagados. No centro, o tempo e o relógio. À direita, os ícones do sistema.

Os ícones abrem popups logo abaixo da barra. Abrir um popup fecha o que estiver aberto, e clicar de novo no ícone, apertar `Esc`, clicar fora ou trocar de workspace fecha o popup. Passar o mouse num ícone mostra um resumo.

- **Rede:** liga e desliga o Wi-Fi, lista as redes Wi-Fi, as conexões cabeadas e as VPNs, conecta, desconecta e mostra os detalhes da conexão ativa (IP, gateway, DNS, sinal). Clique numa rede para conectar. Funciona com o NetworkManager e, sem ele, com o iwd para o Wi-Fi e o systemd-networkd para o cabo; nesse caso não há VPNs nem editor de conexões. O clique do meio abre o editor de conexões do NetworkManager.
- **Bluetooth:** liga o Bluetooth e a visibilidade, lista os aparelhos pareados, conecta, desconecta, procura e pareia aparelhos novos, esquece um aparelho e envia arquivos. A busca só roda quando você pede e para sozinha em 30 segundos. O código de pareamento aparece numa janela do blueman, e o popup fica aberto até o pareamento terminar. O clique do meio abre o gerenciador do blueman.
- **Áudio:** volume e mudo da saída e do microfone, e a escolha do dispositivo de saída e de entrada, com o atual na cor de destaque. Rolar sobre o ícone muda o volume, o clique direito liga o mudo e o clique do meio abre o `pavucontrol`.
- **Bateria:** carga, tempo restante, consumo, saúde da bateria, gráfico das últimas 12 horas, os perfis de energia e a bateria de outros aparelhos, como fone e mouse. O clique direito troca o perfil de energia, e o do meio mostra o estado numa notificação.
- **Brilho e luz noturna:** o controle de brilho e a luz noturna, que deixa a tela mais quente: desligada, ligada o tempo todo ou só no horário que você escolher. Rolar sobre o ícone muda o brilho.
- **Cafeína:** enquanto ela está ligada, a tela não bloqueia, não apaga e o computador não suspende por inatividade. Escolha 1 hora, 2 horas ou sempre. O clique direito liga e desliga. Fechar a tampa continua bloqueando.
- **Mídia:** o ícone só aparece com algo tocando ou pausado. O popup mostra a capa, a faixa, o progresso e os controles; com mais de um player, uma fileira de botões troca entre eles. O clique do meio toca ou pausa, e o direito passa para a próxima.
- **Sistema:** CPU, memória, disco, temperatura e os processos que mais consomem. Um processo seu pode ser encerrado: clique em **Encerrar** e confirme com um segundo clique. O clique direito abre o monitor do sistema.
- **Tempo:** a condição agora, as próximas horas e os próximos três dias, pelo wttr.in. A cidade vem do seu IP, ou da configuração (veja [Configuração](/pt-br/guide/config/)).
- **Calendário:** clique no relógio para ver o mês, com hoje na cor de destaque e os feriados do país. As setas e a rolagem do mouse trocam o mês, e **Hoje** volta.
- **Notificações e área de transferência:** o sino e o ícone da área de transferência abrem os popups descritos abaixo.
- **Teclado:** mostra o layout atual; um clique troca para o próximo.
- **Energia:** o botão no canto direito abre o menu de sessão.

Quando você muda o volume ou o brilho pelas teclas ou pela rolagem, um indicador aparece por um segundo na parte de baixo da tela, acima da dock.

## A dock

A dock fica embaixo, com os apps fixados, depois os abertos e, no fim, o botão da grade de apps. Um ponto embaixo do ícone indica uma janela aberta, e dois, várias. O ponto fica na cor de destaque com a janela em foco.

| Ação | O que acontece |
| --- | --- |
| Clique num app fechado | Abre o app |
| Clique num app com uma janela | Foca a janela, trocando de workspace se preciso |
| Clique num app com várias janelas | Mostra os títulos para você escolher |
| Clique direito | Fixar ou desafixar, nova janela, fechar ou fechar todas |
| Arrastar um fixado | Muda a ordem |

A dock tem três modos:

- **Sobreposição** (`overlap`, o padrão): fica visível e só se esconde quando uma janela ocupa o espaço dela. Na prática, aparece com o workspace vazio ou só com janelas flutuantes pequenas.
- **Esconder sozinha** (`auto-hide`): fica escondida e aparece quando você encosta o ponteiro no meio da borda de baixo.
- **Sempre** (`always`): sempre visível, com as janelas por cima dela.

O modo, o tamanho dos ícones e os monitores com dock ficam em `~/.config/sway-dock/config.toml` (veja [Configuração](/pt-br/guide/config/)). Com uma janela em tela cheia, a dock não aparece.

## A grade de apps

Aperte e solte `Super` para abrir a grade, ou clique no botão da dock. Ela mostra todos os apps instalados, inclusive os Flatpak e os Snap.

- **Busca:** comece a digitar. A busca olha o nome, a descrição e as palavras-chave dos apps, e também acha arquivos nas suas pastas, listados embaixo da grade. Uma conta, como `2*21`, mostra o resultado, e o `Enter` o copia. Com o `qalc` instalado, ela também converte unidades, como `5 km to mi`.
- **Grupos:** a barra de baixo tem a primeira aba, com todos os apps, e os grupos. Os primeiros são Escritório, Sistema e Utilitários. Crie um grupo com **Adicionar grupo** e, com o clique direito num app, ponha ou tire o app de cada grupo. `Ctrl`+`Page Up` e `Ctrl`+`Page Down` passam de um grupo para o outro.
- **Favoritos:** clique direito num app e **Favoritar**. Os favoritos ficam no topo da primeira aba.
- **Dock:** clique direito num app e **Fixar na dock**.

`Esc`, um clique fora dos ícones ou abrir um app fecha a grade.

## O lançador

`Alt`+`Espaço` abre o lançador, uma caixa de busca no centro da tela, com quatro abas: os apps, as janelas abertas, a área de transferência e a web. `Tab` passa de uma aba para a outra, e `Enter` abre o item escolhido. `Super`+`'` (a tecla à esquerda do 1) abre direto a lista de janelas. O mesmo atalho fecha o lançador.

Na aba **Web**, o que você digita vira uma busca. Um prefixo e um espaço escolhem o site: `g` Google, `d` DuckDuckGo, `w` Wikipédia, `yt` YouTube, `gt` Google Tradutor, `cl` Claude e `gpt` ChatGPT. O que parece um endereço, como `kde.org`, abre direto, e o texto sem prefixo vai para o Google. O texto só vai para um serviço de IA (Claude ou ChatGPT) quando você usa o prefixo `cl` ou `gpt`. Dá para acrescentar buscas suas e trocar a padrão nos [ajustes do lançador](/pt-br/guide/config/#buscas-do-lançador).

## Troca de janelas

`Alt`+`Tab` troca de janela na ordem de uso, como no KDE e no GNOME. Segurando o `Alt`, aparece um cartão no centro da tela com o ícone, o título e o workspace de cada janela. Cada `Tab` anda uma janela, e soltar o `Alt` foca a escolhida, trocando de workspace se preciso. `Esc` cancela.

Um toque rápido volta direto para a janela usada antes, sem mostrar o cartão. `Alt`+`Shift`+`Tab` começa pela mais antiga.

## Notificações

As notificações aparecem no canto superior direito e somem em 10 segundos (as urgentes ficam até você fechar). Clicar numa notificação executa a ação padrão do app.

O sino da barra ganha um ponto quando há notificações. Clique nele, ou aperte `Super`+`C`, para abrir a central: as notificações agrupadas por app, com **Limpar** por grupo e **Limpar tudo**.

O **Não perturbe** fica na central: desligado, por 1 hora, por 2 horas ou até você desligar. Com ele ligado, só as notificações urgentes aparecem na tela; as outras vão direto para a central. O clique direito no sino liga e desliga.

A lista só existe na memória: nada é gravado em disco, e ela se apaga quando você sai da sessão.

## Área de transferência

O Swaydesk guarda o histórico do que você copia: textos, imagens e outros conteúdos de até 5 MB. `Super`+`V`, ou o ícone na barra, abre o histórico.

- Digite para buscar em todo o texto dos itens. As setas escolhem um item, e `Enter` o copia, pronto para colar.
- Imagens aparecem com uma miniatura.
- Os botões de cada item fixam o item ou apagam do histórico. Os fixados ficam no topo e não somem quando o histórico é limpo.
- **Limpar histórico** pede um segundo clique para confirmar.

## Menu de sessão

`Ctrl`+`Alt`+`Delete`, ou o botão de energia da barra, abre o menu de sessão no centro da tela: **Bloquear**, **Sair**, **Suspender**, **Reiniciar** e **Desligar**. As teclas são as iniciais dos nomes em inglês: `L`, `E`, `S`, `R` e `P`. As setas e o `Tab` andam entre os botões, e `Esc` ou um clique fora fecha. Não há confirmação: o clique em **Desligar** desliga. Quando um app pede para reiniciar ou desligar, como o **Reiniciar e atualizar** da loja, o Swaydesk pergunta antes, com uma contagem de 60 segundos e um botão para cancelar; cancelar não instala nada e a atualização continua baixada.

## Bloqueio e inatividade

`Ctrl`+`Alt`+`L` bloqueia a tela. A tela de bloqueio mostra a hora e a data sobre o papel de parede desfocado e o campo de senha em todos os monitores. No monitor principal, mostra também a bateria, a rede, o layout do teclado (um clique troca) e a mídia que está tocando.

Essa tela precisa do gtk4-layer-shell 1.2 ou mais novo. Num sistema com uma versão mais antiga, como o Debian 13, quem bloqueia é o swaylock, mais simples. Nos dois casos, se a tela de bloqueio falhar, o swaylock assume, e a tela nunca fica desbloqueada.

Sem uso, o computador:

- bloqueia a tela depois de 10 minutos;
- apaga a tela depois de 15 minutos;
- suspende depois de 30 minutos, só na bateria e sem som tocando.

Ele também bloqueia antes de suspender. A cafeína, na barra, suspende tudo isso enquanto estiver ligada. Se a tela não voltar depois de apagar, `Super`+`Shift`+`O` a liga de novo, mesmo bloqueada.

## Capturas e gravação

`Print` captura uma região, e há atalhos para a tela inteira e para uma janela. As capturas vão para `~/Imagens/Screenshots` (a pasta de imagens do seu idioma), para a área de transferência e aparecem numa notificação. Com o Gradia instalado, dá para abrir a captura nele para editar.

`Super`+`Shift`+`E` abre o painel de captura e `Super`+`Shift`+`R` o de gravação, com as opções de atraso e de som. Durante a gravação, a barra mostra o tempo em vermelho; clique nele, ou repita o atalho, para parar. Os vídeos vão para `~/Vídeos/Screencasts`. As teclas dos painéis estão em [atalhos](/pt-br/shortcuts/).

## Compartilhar a tela

O compartilhamento de tela funciona pelo portal, como nos outros desktops. Quando um app, como o navegador numa chamada, pede para compartilhar a tela, o cursor vira uma mira: clique no monitor que você quer mostrar.

Os navegadores baseados no Chromium abrem uma barra "… está compartilhando sua tela" cujos botões não respondem no Sway. O Swaydesk a guarda de lado; para parar, use o botão da própria página. `Super`+`Z` traz a barra de volta, se precisar.

## Senhas e chaveiro

- **Chaveiro:** o gnome-keyring guarda as senhas do navegador, do Git e de outros apps, e abre junto com o login. Se, no primeiro login, ele tiver sido criado sem abrir, o Swaydesk pede a sua senha uma vez, e os próximos logins o abrem sozinhos.
- **Ações de administrador:** quando um app pede permissão, como para montar um disco, uma janela pede a sua senha. Ela vem do agente de polkit; sem nenhum instalado, uma notificação avisa.
- **Senhas de Wi-Fi:** com o NetworkManager, a janela de senha é a do `nm-applet`. Com o iwd, a senha de uma rede nova é digitada no próprio popup de rede.
