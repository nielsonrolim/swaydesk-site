---
title: Primeiros passos
prompt: "swaydesk-desktop-config setup"
crumb: guide/first-steps
weight: 1
description: Como entrar na sessão do Swaydesk e o que fazer no primeiro login.
---
Com os pacotes instalados, o Swaydesk aparece como uma sessão a mais na tela de login. O desktop que você já tinha continua lá, e as configurações dos dois não se misturam.

## Entrar na sessão

Se você já usa uma tela de login, como a do GNOME (GDM), a do KDE (SDDM) ou a do Mint e do Xfce (LightDM), **não precisa fazer nada além de escolher a sessão**. O Swaydesk entra nela como mais uma opção, e o desktop que você já tinha continua lá:

- **GDM:** clique no seu nome e, antes de digitar a senha, no ícone de engrenagem no canto de baixo à direita;
- **SDDM:** use o menu de sessão, no canto de baixo à esquerda;
- **LightDM:** use o ícone ou o menu de sessão (no Mint, ao lado do nome; em outros temas, no painel de cima).

Escolha **Sway Desktop** e entre com a sua senha. A tela de login lembra a escolha para a próxima vez. Se aparecer também uma sessão chamada só **Sway**, ela é a do pacote do Sway, sem o Swaydesk: use a **Sway Desktop**.

### A tela de login do Swaydesk

O Swaydesk também tem uma tela de login própria, o pacote `swaydesk-greeter`, com o mesmo visual da tela de bloqueio. Com o GDM, o SDDM ou o LightDM, ela é opcional. Sem um gerenciador de login, como numa instalação mínima ou de servidor, o sistema abre num console de texto, e é ela que dá o login gráfico. O que ela faz:

- mostra as contas da máquina com a foto de cada uma, e **Outro usuário…** para digitar o nome;
- lembra a última conta e a sessão que cada pessoa usou, com a **Sway Desktop** primeiro na lista;
- depois da senha, pergunta o que mais o sistema pedir, como um código ou a troca de uma senha vencida;
- usa o teclado e o idioma do sistema e tem os botões de suspender, reiniciar e desligar.

Ela roda sobre o greetd. No Debian e no Ubuntu, o greetd se liga sozinho só quando a máquina não tem outra tela de login; com o GDM, o SDDM ou o LightDM, nada muda até você trocar:

```
sudo apt install swaydesk-greeter
sudo systemctl disable gdm      # ou sddm, ou lightdm
sudo systemctl enable greetd
```

No Arch, o pacman não liga serviços: depois de instalar, rode `sudo systemctl enable greetd`. Em todas as distros, as sessões abertas por esta tela de login usam o serviço PAM do próprio pacote, o `/etc/pam.d/swaydesk-greeter`, que também abre o chaveiro junto com o login. Se você personalizou o `/etc/pam.d/greetd` (um leitor de digital, uma chave de segurança), faça essa mudança no `/etc/pam.d/swaydesk-greeter`.

Para voltar à tela de login de antes, desligue o greetd e ligue a outra (`sudo systemctl disable greetd` e `sudo systemctl enable gdm`, por exemplo). Veja também as [perguntas frequentes](/pt-br/guide/faq/#como-volto-para-a-tela-de-login-que-eu-usava-antes).

## O que você vê

- **A barra no topo:** os workspaces de 1 a 9 à esquerda, o tempo e o relógio no centro e, à direita, os ícones da bandeja, da área de transferência, do teclado, do sistema, do brilho, da cafeína, do Bluetooth, da rede, do volume, da bateria e o botão de energia. Cada ícone abre um popup com um clique.
- **A dock embaixo:** os apps fixados, os abertos e o botão da grade de apps. Ela some quando uma janela ocupa o espaço dela e volta quando você encosta o ponteiro no meio da borda de baixo.
- **A grade de apps:** aperte e solte `Super` (a tecla do logotipo) para mostrar ou esconder todos os apps instalados, com busca.

Os atalhos seguem o esquema Swaydesk, inspirado no KDE Plasma com o Krohnkite, e dá para trocá-los pelos do i3, do Hyprland, do niri ou do dwm. A lista completa, perfil por perfil, está em [atalhos](/pt-br/shortcuts/), e o passeio por cada peça, em [O desktop](/pt-br/guide/desktop/).

## O que o primeiro login prepara

No primeiro login, a sessão copia para a sua pasta pessoal os arquivos que ainda não existem. Nada que você já tenha é sobrescrito, e o que ela copia passa a ser seu:

- `~/.config/swaydesk/config.toml`, a configuração do desktop: idioma, tema, ícones e cor de destaque. Se o tema padrão não estiver instalado, ela já começa com o `Adwaita-dark`;
- `~/.config/sway/config.d/50-local.conf`, o arquivo com os ajustes desta máquina, com exemplos comentados e o layout de teclado do sistema;
- a lista inicial de apps fixados na dock: o gerenciador de arquivos e o terminal.

Ela também aplica o tema e a cor de destaque aos apps GTK, à barra, à dock e aos popups. Os detalhes estão em [Configuração](/pt-br/guide/config/).

**O chaveiro no Debian 13:** no primeiro login de cada usuário aparece um aviso ("Primeiro login: digite sua senha uma vez para ativar o chaveiro. Nos próximos logins ele abre sozinho.") e, logo depois, o pedido de senha do chaveiro (**Unlock Login Keyring**). Digite a mesma senha do login. Isso acontece uma vez só: nos logins seguintes, o chaveiro abre sozinho. É uma limitação do gnome-keyring 48 do Debian; o Ubuntu 26.04 e o Arch não têm.

## Primeiras coisas a fazer

- **Tema e cor de destaque:** abra o app **Tema do Desktop** pela grade de apps. Escolha a família do tema, claro ou escuro, e a cor; **Aplicar** muda tudo de uma vez, e a janela continua aberta para você testar outra combinação.
- **Monitores:** abra o app **Telas** pela grade de apps para acertar a posição, a resolução e a escala das telas. Cada conjunto de monitores guarda a sua escolha, que volta sozinha quando você pluga as mesmas telas.
- **Teclado:** o Swaydesk começa com o layout do sistema. Para usar dois layouts, como o `br` ABNT2 e o `us` internacional, edite o `50-local.conf` (veja [Configuração](/pt-br/guide/config/)). `Super`+`Espaço` troca o layout, e o ícone do teclado na barra mostra o atual.
- **Wi-Fi:** clique no ícone de rede na barra, escolha a rede e digite a senha.
- **Bluetooth:** clique no ícone de Bluetooth, ligue-o e use a busca para parear um aparelho novo.
- **Som:** clique no ícone de volume para escolher a saída e o microfone.
