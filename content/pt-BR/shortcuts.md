---
title: Atalhos
prompt: "grep '^## ' keys/*.conf"
crumb: shortcuts
description: Todos os atalhos de teclado da sessão Swaydesk.
---
O Swaydesk vem com cinco perfis de atalhos: **Swaydesk** (o padrão, que segue o KDE Plasma com o Krohnkite), **i3**, **Hyprland**, **niri** e **dwm**. Cada um traz para o Swaydesk as teclas daquele gerenciador de janelas, e todos têm 9 workspaces. Os atalhos que não usam Super com uma letra (o menu da sessão, o terminal, as capturas, as teclas de mídia) são iguais em todos. `Super` é a tecla do logotipo.

**Escolher um perfil:** na **Ajuda** (`Super`+`F1`), a lista no alto, ao lado da busca, mostra o perfil em uso. Escolha outro e ele vale na hora, sem sair da sessão; a Ajuda passa a mostrar os atalhos novos. Escolher o dwm pede confirmação antes, porque o Mod dele é Alt. Pelo terminal, ponha `shortcuts = "i3"` (ou `swaydesk`, `hyprland`, `niri`, `dwm`) no `~/.config/sway-desktop/config.toml` e recarregue o Sway com `swaymsg reload`, ou com a tecla de recarregar do perfil.

As tabelas abaixo vêm dos mesmos arquivos e descrições que o app **Ajuda** (`Super`+`F1`) mostra.

{{< profiles >}}

## Personalizar atalhos

Os seus atalhos ficam em `~/.config/sway/config.d/50-local.conf`. O arquivo é criado no primeiro login, só com comentários e exemplos, e é seu: nem as atualizações nem a reinstalação o sobrescrevem. O Sway o lê depois dos atalhos do Swaydesk e do perfil de atalhos escolhido, então o que estiver nele vale mais.

**Trocar o que um atalho faz:** repita a tecla com `--no-warn`. Sem ele, o Sway avisa que a tecla já tinha um atalho.

```
## Open foot
bindsym --no-warn Ctrl+Alt+t exec foot
```

**Tirar um atalho:** use `unbindsym` com a tecla exatamente como o perfil em uso a define, inclusive opções como `--locked`. Tirar uma tecla que não tem atalho é um erro de config.

```
unbindsym Print
```

**Criar um atalho:** escolha uma tecla livre. `Super`+`F2` a `Super`+`F12` e `Super`+`Ctrl`+`Alt`+uma letra estão livres em todos os perfis.

```
## Open another terminal
bindsym Mod4+F12 exec kitty
```

O comentário `##` logo acima do atalho é a descrição que aparece na Ajuda.

**Aplicar:** salve o arquivo e rode `swaymsg reload` num terminal, ou entre de novo na sessão. Se algo estiver errado, o Sway mostra uma barra no topo da tela com a linha do problema.

**Conferir:** a Ajuda do Swaydesk (`Super`+`F1`) mostra os atalhos em uso, já com as suas mudanças. No fim da aba Atalhos dela, o botão **Abrir** abre o arquivo no editor.

O mesmo arquivo também guarda os ajustes desta máquina: tela, teclado, mouse, programas ao entrar e apps nos workspaces. Os exemplos estão nos comentários, e o [guia de configuração](/pt-br/guide/config/#os-ajustes-da-máquina) explica cada um.
