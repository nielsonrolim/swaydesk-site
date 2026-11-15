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
| `~/.config/sway-desktop/config.toml` | Idioma, tema, ícones, cor de destaque, cidade do tempo, feriados e gerenciador de arquivos |
| `~/.config/sway/config.d/50-local.conf` | Monitores, teclado, mouse, programas ao entrar e apps nos workspaces |
| `~/.config/sway/outputs` | As telas, gravadas pelo `nwg-displays` |
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

## Monitores

O jeito mais fácil de acertar a resolução, a posição e a escala das telas é o `nwg-displays`, na grade de apps. Ele grava a escolha em `~/.config/sway/outputs` e os workspaces de cada tela em `~/.config/sway/workspaces`. O Sway lê esses dois arquivos depois de todos os outros, então eles valem mais que uma linha `output` no `50-local.conf`.

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

## A tela de login

Com o `swaydesk-greeter`, a tela de login tem os próprios ajustes, para a máquina toda:

- `/etc/swaydesk-greeter/config.toml` aceita a cor de destaque e o idioma, no mesmo formato da configuração do desktop (`accent = "#8e44ad"`, `locale = "pt_BR"`);
- os arquivos `/etc/swaydesk-greeter/sway.d/*.conf` recebem comandos do Sway para as telas da tela de login, como `output eDP-1 scale 1.25`.
