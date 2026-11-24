---
title: Perguntas frequentes
prompt: "less ~/.local/state/sway/sway.log"
crumb: guide/faq
weight: 4
description: Problemas conhecidos e o que fazer em cada um.
---
## Sessão e login

### O login volta para a tela inicial, ou a tela fica preta

Entre na sua outra sessão (GNOME, KDE ou a que você tiver) e veja o erro em `~/.local/state/sway/sway.log`. O log da tentativa anterior fica em `sway.log.old`, ao lado.

### Na tela de login aparecem "Sway" e "Sway Desktop". Qual escolher?

**Sway Desktop**. A sessão **Sway** vem do pacote do Sway e abre o Sway puro, sem o ambiente que o Swaydesk prepara.

### Como volto para a tela de login que eu usava antes?

Sem remover o pacote `swaydesk-greeter`:

```
sudo mkdir -p /etc/systemd/system/greetd.service.d
sudo ln -s /dev/null /etc/systemd/system/greetd.service.d/swaydesk-greeter.conf
sudo systemctl daemon-reload
```

O greetd volta a usar o `/etc/greetd/config.toml` no próximo boot. Se você usava o GDM ou o SDDM, desligue o greetd e ligue o outro de novo com o `systemctl`.

### A sessão pediu a senha do chaveiro no primeiro login. Isso é normal?

Sim, uma vez, no Debian 13. O gnome-keyring 48 dele cria o chaveiro no primeiro login, mas não o deixa disponível para os apps; o Swaydesk o reabre e, para isso, mostra um aviso e pede a senha do login uma vez. Nos logins seguintes, o chaveiro abre sozinho. O Ubuntu 26.04 e o Arch não pedem. Veja [os primeiros passos](/pt-br/guide/first-steps/#o-que-o-primeiro-login-prepara).

## Tela e energia

### A tela continua preta depois de apagar por inatividade

Aperte `Super`+`Shift`+`O`: o atalho liga as telas de novo, mesmo com a tela bloqueada.

### As teclas de brilho não fazem nada

Coloque o seu usuário no grupo `video` e entre de novo na sessão:

```
sudo usermod -aG video $USER
```

### Depois de algumas senhas erradas, diz que a conta está bloqueada {#conta-bloqueada}

É uma regra do próprio Arch (pam_faillock): depois de três logins com falha, a conta fica bloqueada por 10 minutos, inclusive no sudo, e a tela de bloqueio mostra a mensagem do sistema com o tempo que falta. O seu próprio sudo também fica bloqueado; então espere os 10 minutos, ou rode `sudo faillock --user <seu-usuário> --reset` de outra conta de administrador, ou `faillock --user <seu-usuário> --reset` como root num console de texto. O Debian e o Ubuntu não têm essa regra.

### A dock não aparece

No modo padrão, ela se esconde quando uma janela ocupa o espaço dela. Encoste o ponteiro no meio da borda de baixo para ela aparecer. Com uma janela em tela cheia, ela não aparece. Para deixá-la sempre visível, use `mode = "always"` na [configuração da dock](/pt-br/guide/config/).

## Rede, Bluetooth e senhas

### Uma rede com senha não conecta, e nenhuma janela pede a senha

Com o NetworkManager, quem pede a senha é o `nm-applet`. Instale o pacote `network-manager-applet` e entre de novo na sessão.

Com o iwd, a senha de uma rede nova é digitada no popup de rede, que precisa ficar aberto até conectar.

### Parear um aparelho Bluetooth falha, ou nenhuma janela aparece

O código de pareamento é mostrado pelo blueman. Instale o pacote `blueman` e entre de novo na sessão.

### Um app pediu senha de administrador e nada apareceu

Falta um agente de polkit, e a sessão avisa com uma notificação. Instale o `mate-polkit` e entre de novo na sessão.

### O VS Code diz "An OS keyring couldn't be identified"

O VS Code não reconhece o Sway e não acha o chaveiro sozinho. Não aceite a criptografia mais fraca que ele oferece. Em vez disso, acrescente esta linha ao `~/.vscode/argv.json` e reinicie o VS Code:

```
"password-store": "gnome-libsecret"
```

## Apps e aparência

### Compartilhar a tela não mostra nada para escolher

Reinicie o portal, ou saia e entre de novo na sessão:

```
systemctl --user restart xdg-desktop-portal
```

Quando o app pede a tela, o cursor vira uma mira: clique no monitor que você quer compartilhar.

### O aviso "… está compartilhando sua tela" do navegador não responde ao clique

Os botões desse aviso dos navegadores baseados no Chromium não funcionam no Sway, por isso o Swaydesk o guarda de lado. Pare o compartilhamento pelo botão da própria página. `Super`+`Z` traz o aviso de volta.

### Um app Flatpak aparece borrado

Ele está rodando pelo XWayland. Com o Flatseal, dê a ele a permissão de Wayland (`--socket=wayland`).

### Os apps Qt não seguem o tema

Instale o `qt5ct` e o `qt6ct`. O Swaydesk gera a configuração dos dois com as cores do tema GTK e a cor de destaque.

### O app Tema do Desktop avisa que o tema da configuração não está instalado

Enquanto isso, a sessão usa o `Adwaita-dark`. Escolha e aplique um tema no app, e o aviso some.

### Troquei o gerenciador de arquivos, mas a dock continua com o antigo

A dock não troca os fixados sozinha. Desafixe o antigo pelo clique direito na dock e fixe o novo pelo clique direito na grade de apps.

### O calendário não mostra feriados

Os feriados vêm do pacote `python3-holidays`, pelo país da chave `holidays` ou, sem ela, pelo do idioma. Confira se o pacote está instalado e se o país está certo na [configuração](/pt-br/guide/config/).

### Os textos ou o relógio estão no idioma errado

Defina o `locale` na [configuração do desktop](/pt-br/guide/config/) e entre de novo na sessão. O idioma precisa estar gerado no sistema: `locale -a` lista os que estão.

### A previsão do tempo é de outra cidade

Sem configuração, a cidade vem do seu IP. Defina `weather_location` na [configuração do desktop](/pt-br/guide/config/) e entre de novo na sessão. A previsão antiga pode continuar por até 15 minutos.

### O sino das notificações ficou vermelho

O serviço de notificações não está respondendo, e as notificações se perdem. Em geral ele volta sozinho em um segundo. Se continuar, veja se outro serviço de notificações, como o mako ou o dunst, está rodando na sessão: só um pode funcionar por vez.

### Escolhi uma impressora da rede e o diálogo ficou em "Obtendo informações da impressora…"

É normal na primeira vez: o CUPS está criando a fila da impressora e perguntando a ela o que ela sabe fazer, o que leva até uns 30 segundos. Depois a impressão sai normalmente. O CUPS apaga essa fila temporária depois de um tempo sem uso, então a espera pode voltar; para evitar, adicione a impressora de vez em **Configurações da impressão** (no Ubuntu, **Impressoras**), que vem nas ISOs.
