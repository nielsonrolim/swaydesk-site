---
title: Atalhos
prompt: "grep bindsym ~/.config/sway/config"
crumb: shortcuts
description: Todos os atalhos de teclado da sessão Swaydesk.
---
Os atalhos seguem os do KDE Plasma com o Krohnkite. `Super` é a tecla do logotipo.

> Esta tabela foi escrita a partir da configuração do Sway. Em breve ela será gerada das mesmas descrições que o app **Ajuda** mostra.

## Sessão e apps

| Atalho | O que faz |
| --- | --- |
| `Super` (sozinho) | Mostra ou esconde a grade de apps |
| `Alt`+`Espaço` | Lançador: apps, janelas abertas, área de transferência e busca na web |
| `Super`+`'` (à esquerda do 1) | Lista das janelas abertas, para buscar |
| `Ctrl`+`Alt`+`T` | Terminal |
| `Ctrl`+`Alt`+`E` | Gerenciador de arquivos |
| `Super`+`C` | Central de notificações |
| `Super`+`V` | Histórico da área de transferência |
| `Super`+`Espaço` | Troca o layout do teclado |
| `Ctrl`+`Alt`+`L` | Bloqueia a tela |
| `Ctrl`+`Alt`+`Delete` | Menu de sessão: bloquear, sair, suspender, reiniciar, desligar |
| `Super`+`R` | Recarrega a configuração do Sway |
| `Super`+`Shift`+`O` | Liga a tela de novo, se ela não voltar (vale com a tela bloqueada) |

## Janelas

| Atalho | O que faz |
| --- | --- |
| `Alt`+`Tab` / `Alt`+`Shift`+`Tab` | Troca de janela na ordem de uso, com o seletor na tela |
| `Super`+`Tab` / `Super`+`Shift`+`Tab` | Próxima ou anterior na ordem da tela |
| `Super`+`H` `J` `K` `L` ou `Super`+`Alt`+setas | Foca a janela à esquerda, abaixo, acima ou à direita |
| `Super`+`Shift`+`H` `J` `K` `L` | Move a janela |
| `Super`+`Ctrl`+`H` `J` `K` `L` | Redimensiona a janela |
| `Super`+`Enter` | Troca a janela com a primeira do workspace (a "principal") |
| `Super`+`Q` ou `Super`+`Ctrl`+`Esc` | Fecha a janela |
| `Super`+`F` | Solta ou prende a janela (flutuante) |
| `Super`+`Shift`+`F` | Solta ou prende todas as janelas do workspace |
| `Super`+`M`, `Super`+`Page Up` ou `Super`+`Ctrl`+`F` | Tela cheia |
| `Super`+`Page Down` | Guarda a janela de lado (o "minimizar" do Sway) |
| `Super`+`Backspace` ou `Super`+`Z` | Traz de volta a janela guardada |
| `Super`+`Shift`+`G` | Fixa a janela flutuante em todos os workspaces |

## Layout

| Atalho | O que faz |
| --- | --- |
| `Super`+`]` | Alterna entre lado a lado, um sobre o outro, empilhado e em abas |
| `Super`+`Ctrl`+`T` | Volta ao lado a lado |
| `Super`+`Ctrl`+`Enter` | Alterna a próxima divisão entre horizontal e vertical |
| `Super`+`Ctrl`+`X` / `Z` | Aumenta ou diminui o espaço entre as janelas |
| `Super`+`Ctrl`+`R` | Liga ou desliga o espaço entre as janelas |

## Workspaces e monitores

| Atalho | O que faz |
| --- | --- |
| `Super`+`1`…`9` | Vai ao workspace |
| `Super`+`Ctrl`+`1`…`9` | Leva a janela ao workspace, e vai junto |
| `Super`+`←` / `→` | Workspace anterior ou seguinte, mesmo vazio |
| `Super`+`Ctrl`+`←` / `→` | Leva a janela ao workspace anterior ou seguinte |
| `Super`+rolagem do mouse | Workspace anterior ou seguinte |
| `Super`+`W` / `E` | Foca o monitor da esquerda ou da direita |
| `Super`+`Ctrl`+`W` / `E` ou `Super`+`Shift`+`←` / `→` | Leva a janela ao outro monitor |

## Captura e gravação

| Atalho | O que faz |
| --- | --- |
| `Print` | Captura uma região |
| `Shift`+`Print` | Captura a tela inteira |
| `Super`+`Print` | Captura a janela |
| `Ctrl` + qualquer um dos três | O mesmo, e abre a captura no Gradia para editar |
| `Super`+`Shift`+`E` | Painel de captura |
| `Super`+`Shift`+`R` | Painel de gravação; durante a gravação, para |

Nos painéis, as teclas são as iniciais em inglês: `R` região, `S` tela, `W` janela, `Esc` fecha. Na captura, `G` liga ou desliga o Gradia e `D` muda o atraso. Na gravação, `Shift`+tecla grava com o som do sistema, `Ctrl`+tecla com o microfone, e `A` muda o áudio.

## Mídia e brilho

Funcionam também com a tela bloqueada.

| Tecla | O que faz |
| --- | --- |
| Volume +, −, mudo | Volume, com o indicador na tela |
| Microfone mudo | Liga ou desliga o microfone |
| Tocar, próxima, anterior | Controla o player que estiver tocando |
| Brilho +, − | Brilho, com o indicador na tela |

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

**Conferir:** a Ajuda do Swaydesk (`Super`+`F1`) mostra os atalhos em uso, já com as suas mudanças.

O mesmo arquivo também guarda os ajustes desta máquina: tela, teclado, mouse, programas ao entrar e apps nos workspaces. Os exemplos estão nos comentários, e o [guia de configuração](/pt-br/guide/config/#os-ajustes-da-máquina) explica cada um.
