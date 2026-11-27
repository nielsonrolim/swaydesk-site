---
title: Configuração
prompt: "cat ~/.config/swaydesk/config.toml"
crumb: guide/config
weight: 3
description: Os arquivos que você edita para ajustar o Swaydesk à sua máquina e ao seu gosto.
---
A configuração do Sway e da barra vem do pacote e é atualizada com ele. O que é seu fica em poucos arquivos na sua pasta pessoal, que o primeiro login cria e as atualizações nunca sobrescrevem.

| Arquivo | O que guarda |
| --- | --- |
| `~/.config/swaydesk/config.toml` | Idioma, tema, ícones, cor de destaque, cidade do tempo, feriados, gerenciador de arquivos, perfil de atalhos e os componentes desligados |
| `~/.config/sway/config.d/50-local.conf` | Monitores, teclado, mouse, programas ao entrar e apps nos workspaces |
| `~/.config/swaydesk/displays.json` | As telas de cada conjunto de monitores, gravadas pelo app **Telas** |
| `~/.config/sway-dock/config.toml` | O modo e o tamanho da dock |

Antes da 0.1.4, as pastas `swaydesk` se chamavam `sway-desktop`: `~/.config/sway-desktop`, e o mesmo em `~/.local/share` e `~/.local/state`. O primeiro login na 0.1.4 as move para `swaydesk` e deixa os nomes antigos como links para as pastas novas, então os caminhos antigos continuam valendo. Se um arquivo estiver na pasta velha e na nova, nada é movido, a pasta velha continua valendo, e o log da sessão avisa (`grep kept: ~/.local/state/sway/sway.log`); junte as duas pastas à mão para trocar.

## A configuração do desktop

O `~/.config/swaydesk/config.toml` vale para todas as peças do Swaydesk. O jeito mais fácil de mudar o tema e a cor é o app **Tema do Desktop**, que grava este arquivo por você. Pelo terminal, o `swaydesk-theme` faz o mesmo:

```
swaydesk-theme families                  # as famílias de temas instaladas
swaydesk-theme pick Adwaita dark teal    # família, claro ou escuro, e a cor
swaydesk-theme current                   # o tema, os ícones e a cor em uso
swaydesk-theme cursor 32                 # o tamanho do cursor; sem número, os tamanhos que o tema do cursor tem
```

As cores aceitas são as das pastas do Papirus; `swaydesk-theme colors` lista todas.

O tamanho do cursor também está no app, na lista **Tamanho do cursor** abaixo dos ícones, que só mostra os tamanhos que o tema do cursor tem. A escolha vale na hora, sem **Aplicar**: os apps GTK 4 e Qt 6 mudam na mesma hora, e os mais antigos (GTK 3, Qt 5, Electron e os apps X11) quando você os abre de novo. Uma linha `seat` sua no `~/.config/sway/config.d/50-local.conf` vale mais e volta no próximo reload ou login.

Um exemplo do arquivo, com as chaves que você pode mudar à mão:

```
# Idioma dos textos, da data e do tempo. Vazio: o idioma do sistema
locale = "pt_BR"

# Cidade da previsão do tempo. Vazio: a do seu IP
weather_location = "Lisbon"

# País dos feriados do calendário. Vazio: o do idioma. "none": nenhum
holidays = "BR"

# Tema GTK, ícones e cor de destaque
gtk_theme = "Adwaita-dark"
icon_theme = "Papirus-Dark"
accent = "#199ca8"

# true: a cor de destaque vem do papel de parede e muda com ele. Sem esta chave, fica ligado enquanto o
# destaque é o padrão e há papel de parede, e desligado nos outros casos
accent_auto = true

# Cor das pastas do Papirus, como "teal". Vazio: a mais perto do destaque
folder_color = ""

# Gerenciador de arquivos do Ctrl+Alt+E, da grade de apps e da dock. Vazio: o primeiro instalado
file_manager = "thunar"

# Perfis de energia no popup Sistema: "auto" (o padrão) só sem bateria, "always" ou "never"
power_profiles_in_system = "auto"

# Tamanho do cursor em pixels, de 16 a 96 (24 por padrão)
cursor_size = 24

# Tema do cursor: qualquer um instalado (uma pasta com cursors/). Vazio: o automático (Bibata no Debian e no
# Ubuntu, Capitaine no Arch)
cursor_theme = ""
```

Os programas leem o arquivo quando abrem. Depois de editar à mão:

- para a cor de destaque, ponha antes `accent_auto = false`, senão o próximo papel de parede traz a cor dele de volta; depois rode `swaydesk-desktop-config apply`, que grava as cores e recarrega o Sway; os popups já abrem com a cor nova, e o resto muda no próximo login;
- para o gerenciador de arquivos, rode `swaydesk-desktop-config generate`, para as pastas abertas por outros apps também irem para ele;
- para o idioma, a cidade e os feriados, saia e entre de novo na sessão;
- para o `power_profiles_in_system`, nada: vale na próxima vez que o popup Sistema abrir;
- para o `cursor_theme`, o `swaydesk-desktop-config apply` (ou o app Tema) o aplica na hora: o cursor do Sway, as configurações do GTK e o `gsettings`; um tema que não está instalado só gera um aviso, e uma linha `seat … xcursor_theme` sua em `~/.config/sway/config.d` continua valendo;
- para o `cursor_size`, `swaydesk-theme cursor <tamanho>` o aplica em tudo na hora; `swaydesk-desktop-config apply` o aplica no Sway, e o resto no próximo login.

Um valor inválido não quebra nada: a peça usa o padrão daquela chave.

Num computador sem bateria, o ícone da bateria sai da barra e, com ele, os botões de perfil do popup dela. Por isso o popup Sistema ganha a linha **Perfil de energia**, com os perfis que o `power-profiles-daemon` oferece (Economia, Equilibrado e, onde o hardware permite, Desempenho): um clique troca o perfil sem fechar o popup. Sem o daemon, a linha não aparece. Com `"always"`, ela aparece também nos notebooks; o popup da bateria continua com os botões de qualquer jeito.

## Ligar e desligar componentes

Cada componente do Swaydesk vem ligado, menos o método de entrada ([abaixo](#metodo-de-entrada)). Para desligar um, ponha a chave dele com `false` na seção `[enabled]` do `~/.config/swaydesk/config.toml`; os módulos da barra ficam na `[enabled.bar]`:

```
[enabled]
dock = false            # a dock
bing_wallpaper = false  # o papel de parede do dia

[enabled.bar]
weather = false         # o clima na barra
```

| Chave do `[enabled]` | O que desliga |
| --- | --- |
| `dock` | A dock |
| `app_grid` | A grade de apps (o toque no `Super`) |
| `switcher` | O cartão do `Alt`+`Tab` |
| `notifications` | O serviço de notificações |
| `osd` | O indicador de volume e brilho |
| `clipboard_history` | O histórico da área de transferência |
| `nightlight` | A luz noturna |
| `bing_wallpaper` | O papel de parede do dia |
| `polkit_agent` | O agente de polkit (a senha de administrador) |
| `update_notifier` | O aviso de atualizações |
| `displays` | Os perfis automáticos das telas; o app **Telas** continua |
| `autostart` | Os apps de `~/.config/autostart` e `/etc/xdg/autostart` (veja abaixo) |
| `input_method` | Desligada a menos que seja `true`: aí a sessão sobe o método de entrada fcitx5 (veja abaixo) |

As chaves do `[enabled.bar]` são os módulos da barra: `weather`, `clock`, `media`, `recording`, `notifications`, `clipboard`, `language`, `system`, `brightness`, `caffeine`, `bluetooth`, `network`, `volume`, `battery`, `power` e, no Arch, `updates`. Os workspaces e a bandeja ficam sempre.

A mudança vale no próximo login. Uma chave ausente fica ligada (menos a `input_method`), e um erro no arquivo nunca desliga nada. Na Ajuda (`Super`+`F1`), o cartão de um componente desligado diz "Desligado" e como religá-lo. A página [Componentes](/pt-br/components/) mostra a chave de cada um.

### Apps que abrem no login

A sessão abre os apps das pastas de início automático do XDG, `~/.config/autostart` e `/etc/xdg/autostart`, como o GNOME e o KDE fazem, e os fecha quando você sai. As entradas do que o Swaydesk já cobre (blueman, nm-applet, os agentes de polkit do mate e do lxpolkit, xapp-sn-watcher) ficam de fora, só na sessão do Swaydesk: o GNOME ou o KDE na mesma conta continuam abrindo essas entradas. A entrada do próprio PulseAudio também fica de fora ali, mas só quando o PipeWire é o servidor de som, caso em que ela só falharia.

Para um app não abrir, ponha uma cópia do `.desktop` dele em `~/.config/autostart` com `Hidden=true`, ou com `NotShowIn=sway;` para pular só nas sessões do Sway, e o GNOME ou o KDE continuam abrindo. Para desligar todos, ponha `autostart = false` em `[enabled]`. Um `config.toml` de uma versão anterior não tem essa chave: acrescente a linha dentro de `[enabled]`, antes da parte `[enabled.bar]`, porque uma linha abaixo de `[enabled.bar]` vale para a barra.

### Método de entrada (fcitx5) {#metodo-de-entrada}

No Wayland, o Chromium, o Chrome, o Vivaldi, o Brave e os apps Electron (VS Code, Slack, Discord) ignoram o `~/.XCompose` e compõem os acentos com uma tabela própria, a do en_US, em que `'` + `c` dá `ć`. O método de entrada fcitx5 faz o `ç` sair neles. Com `input_method = true` no `[enabled]` e o pacote `fcitx5` instalado, o login sobe o fcitx5 com os atalhos, o ícone na bandeja e os avisos dele desligados, no teclado da sessão (o primeiro layout). Ele acompanha o teclado quando você o muda no `50-local.conf`, até você mesmo trocar os métodos do fcitx5 (no `fcitx5-configtool`, por exemplo). Quem troca o layout continua sendo o Sway, com `Super`+`Espaço`, e os apps GTK continuam compondo sozinhos.

A chave vem desligada num sistema que instalou os pacotes, e ligada nas imagens de instalação do Debian 13 e do Arch, pelo `/etc/swaydesk/config.toml`, que só traz os padrões do sistema para o `[enabled]`. Uma linha no seu `config.toml` vence.

Os navegadores precisam também de duas opções, `--enable-wayland-ime --wayland-text-input-version=3`:

- **No Arch**, o login cria os arquivos de opções que os lançadores leem, em `~/.config`: `chromium-flags.conf`, `chrome-flags.conf`, `vivaldi-stable.conf`, `brave-flags.conf`, `electron-flags.conf` e `code-flags.conf`, só para o que estiver instalado e só quando o arquivo não existe. Num arquivo seu, acrescente as duas opções. Um navegador instalado no meio da sessão só ganha o arquivo no próximo login: saia e entre de novo (ou crie o arquivo) antes de abri-lo.
- **No Debian**, o Chromium não lê esses arquivos e chega ao fcitx5 pelo `GTK_IM_MODULE=fcitx` que o im-config, que vem com o fcitx5, exporta. O Chrome e o Vivaldi dos `.deb` dos fabricantes, e os apps Electron, precisam das opções no atalho: copie o `.desktop` para `~/.local/share/applications` e acrescente-as à linha `Exec`.

Nada sobe se outro método de entrada estiver configurado (`GTK_IM_MODULE`, `QT_IM_MODULE` ou `XMODIFIERS` apontando para outro, como o ibus que o im-config do Linux Mint exporta) ou se o `ibus-daemon` já estiver rodando. Se você sobe o ibus no `50-local.conf`, desligue o `input_method`. No Linux Mint, para usar o fcitx5, escolha-o com `im-config -n fcitx5` (com os pacotes `fcitx5-frontend-gtk3` e `fcitx5-frontend-gtk4`) e ligue a chave.

Para desligar, ponha `input_method = false`: vale no próximo login, e os arquivos criados ficam. No Arch, o autostart do próprio pacote fcitx5 continua subindo o fcitx5, como em qualquer sessão: remova o pacote, ou ponha uma cópia do `/etc/xdg/autostart/org.fcitx.Fcitx5.desktop` em `~/.config/autostart` com `NotShowIn=sway;` (só no Swaydesk) ou `Hidden=true` (em todos os desktops da conta). No Debian, o im-config exporta `GTK_IM_MODULE=fcitx` em toda sessão Wayland enquanto o fcitx5 estiver instalado, em qualquer desktop; `im-config -n none` (ou remover o fcitx5) volta ao padrão.

## Os ajustes da máquina

O Sway lê, por último, os arquivos de `~/.config/sway/config.d/`, então o que estiver ali vale mais que a configuração do pacote. O primeiro login cria o `50-local.conf` com exemplos comentados e o layout de teclado do sistema. Edite e aplique com `Super`+`R` (ou `swaymsg reload`).

Um exemplo preenchido:

```
# Tela: o nome da saída vem de `swaymsg -t get_outputs`
output eDP-1 mode 1920x1080@60Hz scale 1

# Teclado: br ABNT2 e us internacional, trocados com Super+Espaço
input type:keyboard {
    xkb_layout  br,us
    xkb_variant abnt2,intl
}

# Mouse: canhoto e rolagem invertida
input type:pointer {
    left_handed    enabled
    natural_scroll enabled
}

# Programas ao entrar na sessão que não têm entrada de autostart (os do ~/.config/autostart já abrem)
exec foot --server

# Apps nos workspaces: o app abre lá, e você continua onde está
assign [app_id="^org.mozilla.firefox$"] workspace number 2
assign [app_id="^thunderbird$"]         workspace number 9

# Para trocar um atalho que já existe, use --no-warn
bindsym --no-warn Ctrl+Alt+t exec foot
```

Algumas dicas:

- Com dois layouts no `xkb_layout`, a sessão sempre começa no primeiro.
- O `app_id` de uma janela aberta aparece com `swaymsg -t get_tree | grep app_id`. Os apps que rodam pelo XWayland usam `class=` no lugar de `app_id=`.
- Os arquivos `00-accent.conf` e `00-font.conf` da mesma pasta são gerados pelo Swaydesk: não os edite, porque eles são regravados.
- A documentação completa dos comandos está em `man 5 sway` e `man 5 sway-input`.

### Teclado e acentos

- **O teclado do sistema.** O bloco do teclado que o primeiro login grava no fim do `50-local.conf` segue o teclado do sistema a cada login, enquanto ninguém o mexer. Uma troca com `localectl set-x11-keymap` ou `sudo dpkg-reconfigure keyboard-configuration` chega às contas que já existem no login seguinte, e a tela de login e as contas novas também seguem. Um bloco editado à mão fica como está, e um bloco seu mais abaixo no arquivo vale mais que o nosso.
- **Debian e Ubuntu.** Neles, o `localectl` muda só o `/etc/vconsole.conf`, que o boot reescreve a partir do `/etc/default/keyboard`: a troca que fica depois de um reboot é a do `sudo dpkg-reconfigure keyboard-configuration`. No Arch, o `localectl` fica.
- **`ç` no US internacional.** Com a sessão no US internacional (`intl` ou `altgr-intl`), `'` + `c` dá `ç` (e `'` + `C` dá `Ç`) nos apps GTK e Qt, nos terminais e na tela de login. Para isso, o login cria este `~/.XCompose`, se não houver nada nesse caminho:

  ```
  include "%L"
  <dead_acute> <c> : "ç" ccedilla
  <dead_acute> <C> : "Ç" Ccedilla
  ```

  Um arquivo seu nunca é mexido. Se a sessão deixar de usar o US internacional, o arquivo sai no login seguinte, enquanto estiver igual ao original. Ao escrever um à mão, deixe a linha do `include` em primeiro: sem ela, o arquivo troca a tabela inteira e os outros acentos (`'` + `e`, `~` + `a`) deixam de sair.
- **Acentos e método de entrada.** Sem método de entrada (ibus, fcitx) configurado, a sessão usa `GTK_IM_MODULE=simple`, e o GTK compõe as teclas mortas sozinho, também nos apps GTK 4. Quem usa um método de entrada define `GTK_IM_MODULE`, `QT_IM_MODULE` ou `XMODIFIERS` no `~/.profile` (por exemplo, `export GTK_IM_MODULE=wayland` para o fcitx5), e a sessão não muda nada. Para o `ç` no Chromium e nos apps Electron, veja [Método de entrada (fcitx5)](#metodo-de-entrada). O mesmo vale para um teclado na tela que digita pelo método de entrada, como o squeekboard: ele precisa do `export GTK_IM_MODULE=wayland` no `~/.profile`.

## Buscas do lançador

As buscas da aba **Web** do lançador mudam no `~/.config/swaydesk/launcher.conf`, uma linha `chave = valor` por ajuste (`#` comenta):

```
# um prefixo e o endereço da busca; %s é o texto digitado
search = gh https://github.com/search?q=%s
# a busca do texto sem prefixo (sem esta linha, o Google)
default = d
```

Uma linha `search` com um prefixo novo acrescenta uma busca, e uma com um prefixo que já existe (`g`, `d`, `w`, `yt`, `gt`, `cl`, `gpt`) troca a dele. O endereço precisa começar com `http://` ou `https://`, ter o `%s` e nenhum espaço; senão a linha é ignorada, e um `default` com um prefixo que não existe volta ao Google. A mudança vale na próxima vez que você abrir o lançador.

## Monitores

O jeito mais fácil de acertar as telas é o app **Telas**, na grade de apps. Arraste as telas no mapa, escolha a resolução, a taxa, a escala e a rotação de cada uma e clique em **Aplicar**. Sem um clique em **Manter** em 15 segundos, tudo volta ao que era.

Cada conjunto de monitores (o notebook sozinho, o notebook com o monitor do escritório…) guarda o seu layout em `~/.config/swaydesk/displays.json`, aplicado sozinho quando você pluga ou despluga uma tela. Com a tampa fechada e um monitor ligado, a tela do notebook desliga. O último layout mantido também vai para `~/.config/sway/config.d/90-displays.conf`, lido depois do `50-local.conf`: ele vale mais que uma linha `output` de lá. Não edite esse arquivo à mão, porque o próximo **Manter** o regrava.

## A dock

A dock lê `~/.config/sway-dock/config.toml`, que não existe no começo: crie o arquivo com só o que quiser mudar. Depois de editar, rode `swaydesk-dock reload`.

```
# overlap: some quando uma janela ocupa o espaço dela
# auto-hide: escondida até você encostar o ponteiro na borda
# always: sempre visível
mode = "auto-hide"

icon_size = 40          # de 16 a 128
hide_delay_ms = 400     # tempo até esconder, em milissegundos
animation_ms = 200      # duração do deslizar; 0 desliga

ignore = []             # app_ids que não aparecem na dock
outputs = ["eDP-1"]     # monitores com dock; vazio: todos
```

Os apps fixados ficam em `~/.local/share/sway-dock/pinned`, mas é mais simples fixar pelo clique direito na dock ou na grade de apps. Os grupos e os favoritos da grade ficam em `~/.local/share/sway-drawer/`.

## Atualizações no Arch

No Arch, a parte de atualizações da loja (GNOME Software) vem desativada, porque o aviso do Swaydesk cuida de tudo: os repositórios oficiais, o AUR (pelo paru ou yay, se você já tiver um instalado), os apps Flatpak e o firmware (fwupd). Ele confere em segundo plano, mostra um ícone na barra com a quantidade e avisa por notificação quando há algo novo; nada é atualizado sozinho. O clique (ou o botão **Atualizar** da notificação) abre um terminal com a atualização.

- **Para desligar o aviso do Swaydesk** (quem prefere atualizar à mão ou por outra ferramenta): ponha `update_notifier = false` na seção `[enabled]` de `~/.config/swaydesk/config.toml` e entre de novo na sessão. A verificação, a notificação e o ícone param, e a loja volta a cuidar das atualizações sozinha.
- **Para reativar a parte de atualizações da loja à mão**, mantendo o aviso do Swaydesk: `gsettings set org.gnome.software allow-updates true` (para voltar: `gsettings reset org.gnome.software allow-updates`). Com os dois ligados, as atualizações do Flatpak aparecem duas vezes.
- **Só o ícone:** `updates = false` na seção `[enabled.bar]` esconde o ícone e mantém a verificação e a notificação.

## SwayFX no Arch (opcional)

O [SwayFX](https://github.com/WillPower3309/swayfx) é o Sway com cantos arredondados, blur e sombras. No Arch, ele pode substituir o Sway, com a mesma configuração. Ele vem do AUR, por um AUR helper:

```
yay -S swayfx           # ou: paru -S swayfx; o pacman troca o sway por ele
sudo pacman -S sway     # para voltar ao Sway
```

O `swaydesk-desktop` continua instalado nos dois casos, porque o `swayfx` provê o `sway`.

**Aviso:** o SwayFX vem do AUR e é mantido por terceiros, fora do suporte do projeto. Ele pode atrasar em relação às versões do Sway, e um `pacman -Syu` que traga um wlroots novo pode quebrá-lo até o AUR acompanhar. Se a sessão não abrir depois de uma atualização, volte ao Sway com `sudo pacman -S sway`, num console de texto (Ctrl+Alt+F2).

O Swaydesk liga os efeitos sozinho, no próximo login. Ele percebe o SwayFX e grava o `~/.config/sway/config.d/10-effects.conf`; com o Sway comum, o arquivo fica só com um comentário. O arquivo é gravado de novo a cada login, quando o tema muda e com o `swaydesk-desktop-config generate` (depois, rode `swaymsg reload`).

Os efeitos ficam na seção `[effects]` do `~/.config/swaydesk/config.toml`. Uma chave ausente fica com o padrão:

```
[effects]
corner_radius = 10      # cantos das janelas e das camadas, em pixels, de 0 (retos) a 30
blur = true             # blur atrás das janelas transparentes
shadows = true          # uma sombra leve nas janelas
layer_blur = false      # blur atrás da barra, da dock, dos popups, das notificações e dos menus
dim_inactive = 0.0      # escurecer as janelas sem o foco, de 0.0 (nada) a 1.0
```

O blur atrás da barra, da dock e dos popups vem desligado por padrão, porque apareceu lixo visual numa máquina virtual (virgl). Ligue com `layer_blur = true`. Duas coisas nunca ficam com blur: a camada invisível que fecha os popups quando você clica fora, e a escolha do screenshot, que precisa mostrar a tela nítida.

## A tela de login

Com o `swaydesk-greeter`, a tela de login tem os próprios ajustes, para a máquina toda:

- `/etc/swaydesk-greeter/config.toml` aceita a cor de destaque e o idioma, no mesmo formato da configuração do desktop (`accent = "#8e44ad"`, `locale = "pt_BR"`);
- os arquivos `/etc/swaydesk-greeter/sway.d/*.conf` recebem comandos do Sway para as telas da tela de login, como `output eDP-1 scale 1.25`.
