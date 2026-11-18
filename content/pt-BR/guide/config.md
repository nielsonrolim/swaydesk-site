---
title: Configuração
prompt: "cat ~/.config/sway-desktop/config.toml"
crumb: guide/config
weight: 3
description: Os arquivos que você edita para ajustar o Swaydesk à sua máquina e ao seu gosto.
---
A configuração do Sway e da barra vem do pacote e é atualizada com ele. O que é seu fica em poucos arquivos na sua pasta pessoal, que o primeiro login cria e as atualizações nunca sobrescrevem.

| Arquivo | O que guarda |
| --- | --- |
| `~/.config/sway-desktop/config.toml` | Idioma, tema, ícones, cor de destaque, cidade do tempo, feriados, gerenciador de arquivos, perfil de atalhos e os componentes desligados |
| `~/.config/sway/config.d/50-local.conf` | Monitores, teclado, mouse, programas ao entrar e apps nos workspaces |
| `~/.config/sway-desktop/displays.json` | As telas de cada conjunto de monitores, gravadas pelo app **Telas** |
| `~/.config/sway-dock/config.toml` | O modo e o tamanho da dock |

## A configuração do desktop

O `~/.config/sway-desktop/config.toml` vale para todas as peças do Swaydesk. O jeito mais fácil de mudar o tema e a cor é o app **Tema do Desktop**, que grava este arquivo por você. Pelo terminal, o `swaydesk-theme` faz o mesmo:

```
swaydesk-theme families                  # as famílias de temas instaladas
swaydesk-theme pick Adwaita dark teal    # família, claro ou escuro, e a cor
swaydesk-theme current                   # o tema, os ícones e a cor em uso
```

As cores aceitas são as das pastas do Papirus; `swaydesk-theme colors` lista todas.

Um exemplo do arquivo, com as chaves que você pode mudar à mão:

```
# Idioma dos textos, da data e do tempo. Vazio: o idioma do sistema
locale = "pt_BR"

# Cidade da previsão do tempo. Vazio: a do seu IP
weather_location = "Recife"

# País dos feriados do calendário. Vazio: o do idioma. "none": nenhum
holidays = "BR"

# Tema GTK, ícones e cor de destaque
gtk_theme = "Adwaita-dark"
icon_theme = "Papirus-Dark"
accent = "#199ca8"

# Cor das pastas do Papirus, como "teal". Vazio: a mais perto do destaque
folder_color = ""

# Gerenciador de arquivos do Ctrl+Alt+E, da grade de apps e da dock. Vazio: o primeiro instalado
file_manager = "thunar"
```

Os programas leem o arquivo quando abrem. Depois de editar à mão:

- para a cor de destaque, rode `swaydesk-desktop-config apply`, que grava as cores e recarrega o Sway; os popups já abrem com a cor nova, e o resto muda no próximo login;
- para o gerenciador de arquivos, rode `swaydesk-desktop-config generate`, para as pastas abertas por outros apps também irem para ele;
- para o idioma, a cidade e os feriados, saia e entre de novo na sessão.

Um valor inválido não quebra nada: a peça usa o padrão daquela chave.

## Ligar e desligar componentes

Cada componente do Swaydesk vem ligado. Para desligar um, ponha a chave dele com `false` na seção `[enabled]` do `~/.config/sway-desktop/config.toml`; os módulos da barra ficam na `[enabled.bar]`:

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

As chaves do `[enabled.bar]` são os módulos da barra: `weather`, `clock`, `media`, `recording`, `notifications`, `clipboard`, `language`, `system`, `brightness`, `caffeine`, `bluetooth`, `network`, `volume`, `battery` e `power`. Os workspaces e a bandeja ficam sempre.

A mudança vale no próximo login. Uma chave ausente fica ligada, e um erro no arquivo nunca desliga nada. Na Ajuda (`Super`+`F1`), o cartão de um componente desligado diz "Desligado" e como religá-lo. A página [Componentes](/pt-br/components/) mostra a chave de cada um.

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

# Programas ao entrar na sessão (o Sway não lê o ~/.config/autostart)
exec nextcloud --background

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

## Buscas do lançador

As buscas da aba **Web** do lançador mudam no `~/.config/sway-desktop/launcher.conf`, uma linha `chave = valor` por ajuste (`#` comenta):

```
# um prefixo e o endereço da busca; %s é o texto digitado
search = gh https://github.com/search?q=%s
# a busca do texto sem prefixo (sem esta linha, o Google)
default = d
```

Uma linha `search` com um prefixo novo acrescenta uma busca, e uma com um prefixo que já existe (`g`, `d`, `w`, `yt`, `gt`, `cl`, `gpt`) troca a dele. O endereço precisa começar com `http://` ou `https://`, ter o `%s` e nenhum espaço; senão a linha é ignorada, e um `default` com um prefixo que não existe volta ao Google. A mudança vale na próxima vez que você abrir o lançador.

## Monitores

O jeito mais fácil de acertar as telas é o app **Telas**, na grade de apps. Arraste as telas no mapa, escolha a resolução, a taxa, a escala e a rotação de cada uma e clique em **Aplicar**. Sem um clique em **Manter** em 15 segundos, tudo volta ao que era.

Cada conjunto de monitores (o notebook sozinho, o notebook com o monitor do escritório…) guarda o seu layout em `~/.config/sway-desktop/displays.json`, aplicado sozinho quando você pluga ou despluga uma tela. Com a tampa fechada e um monitor ligado, a tela do notebook desliga. O último layout mantido também vai para `~/.config/sway/config.d/90-displays.conf`, lido depois do `50-local.conf`: ele vale mais que uma linha `output` de lá. Não edite esse arquivo à mão, porque o próximo **Manter** o regrava.

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

## SwayFX no Arch (opcional)

O [SwayFX](https://github.com/WillPower3309/swayfx) é o Sway com cantos arredondados, blur e sombras. No Arch, ele pode substituir o Sway, com a mesma configuração. Ele vem do AUR, por um AUR helper:

```
yay -S swayfx           # ou: paru -S swayfx; o pacman troca o sway por ele
sudo pacman -S sway     # para voltar ao Sway
```

O `swaydesk-desktop` continua instalado nos dois casos, porque o `swayfx` provê o `sway`.

**Aviso:** o SwayFX vem do AUR e é mantido por terceiros, fora do suporte do projeto. Ele pode atrasar em relação às versões do Sway, e um `pacman -Syu` que traga um wlroots novo pode quebrá-lo até o AUR acompanhar. Se a sessão não abrir depois de uma atualização, volte ao Sway com `sudo pacman -S sway`, num console de texto (Ctrl+Alt+F2).

O Swaydesk liga os efeitos sozinho, no próximo login. Ele percebe o SwayFX e grava o `~/.config/sway/config.d/10-effects.conf`; com o Sway comum, o arquivo fica só com um comentário. O arquivo é gravado de novo a cada login, quando o tema muda e com o `sway-desktop-config generate` (depois, rode `swaymsg reload`).

Os efeitos ficam na seção `[effects]` do `~/.config/sway-desktop/config.toml`. Uma chave ausente fica com o padrão:

```
[effects]
corner_radius = 10      # cantos das janelas e das camadas, em pixels, de 0 (retos) a 30
blur = true             # blur atrás das janelas transparentes
shadows = true          # uma sombra leve nas janelas
layer_blur = false      # blur atrás da barra, da dock, dos popups, das notificações e dos menus
dim_inactive = 0.0      # escurecer as janelas sem o foco, de 0.0 (nada) a 1.0
```

O blur atrás da barra, da dock e dos popups vem desligado por padrão, porque apareceu lixo visual numa máquina virtual (virgl). Ligue com `layer_blur = true`. Duas coisas nunca ficam com blur: a camada invisível que fecha os popups quando você clica fora, e a escolha da captura de tela, que precisa mostrar a tela nítida.

## A tela de login

Com o `swaydesk-greeter`, a tela de login tem os próprios ajustes, para a máquina toda:

- `/etc/swaydesk-greeter/config.toml` aceita a cor de destaque e o idioma, no mesmo formato da configuração do desktop (`accent = "#8e44ad"`, `locale = "pt_BR"`);
- os arquivos `/etc/swaydesk-greeter/sway.d/*.conf` recebem comandos do Sway para as telas da tela de login, como `output eDP-1 scale 1.25`.
