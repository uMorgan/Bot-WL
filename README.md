# 🤖 Bot de Whitelist para Discord - REALIDADE RP

Este bot foi desenvolvido para gerenciar o processo de whitelist no servidor **REALIDADE RP**, um servidor de roleplay no FiveM. Ele permite que membros enviem suas informações por meio de um formulário (modal), e que a equipe possa aprovar ou reprovar os pedidos de forma prática, com botões interativos.

## ✨ Funcionalidades

- Envia automaticamente um embed com botão ao iniciar o bot.
- Abre um **modal** com perguntas de whitelist ao clicar no botão.
- Cria um canal privado com as respostas para análise da equipe.
- Possui botões de **Aprovar** ou **Reprovar**.
- Envia resultados para um canal específico e também via DM.
- Deleta automaticamente o canal de whitelist após um tempo.

## 🧱 Estrutura de Permissões Necessária

O bot precisa de permissões suficientes para:

- Criar canais de texto.
- Gerenciar permissões de canal.
- Enviar mensagens e embeds.
- Gerenciar cargos (para adicionar cargo aprovado).
- Enviar mensagens privadas (opcional, mas recomendado).

## ⚙️ Configurações

No início do script, você encontrará constantes com os IDs dos canais e cargo:

```python
CANAL_WL = 1364997491568808047         # Canal onde o botão de whitelist será enviado
CATEGORIA_WL = 1364997526712881223     # Categoria onde os canais de whitelist serão criados
CANAL_RESULTADO = 1364998988171841548  # Canal onde os resultados são postados
CARGO_APROVADO = 1364997695361515600   # Cargo que será atribuído ao usuário aprovado
```

Certifique-se de substituir esses valores pelos IDs corretos do seu servidor.

## 🚀 Como Usar

1. Instale o pacote necessário:

```bash
pip install -U discord.py
```

2. Salve o código em um arquivo, por exemplo, `bot.py`.

3. Substitua o token do bot no final do código:

```python
bot.run("SEU_TOKEN_AQUI")
```

4. Inicie o bot com o seguinte comando no terminal:

```bash
python bot.py
```

5. O bot enviará um embed no canal `CANAL_WL` com o botão **"Fazer WL"** automaticamente ao iniciar.

---

## 🧪 Modal de Whitelist

As perguntas incluídas no formulário (modal) são:

1. **Qual seu nome?**
2. **Idade**
3. **Conte-nos a história do seu personagem**
4. **Qual rumo você irá seguir na cidade?** (Ex: Bandido, Polícia, Mecânico etc.)
5. **Como você nos conheceu?**

---

## ✅ Aprovando ou ❌ Reprovando

Após o envio das respostas, o bot:

- Cria automaticamente um **canal privado** para a equipe visualizar.
- Exibe dois botões: **✅ Aprovar** e **❌ Reprovar**.
- Envia o resultado da análise para:
  - O canal `CANAL_RESULTADO`, com menção ao jogador.
  - Mensagem privada (DM), se permitido pelo usuário.

Além disso:

- Se aprovado, o canal será deletado **após 60 segundos**.
- Se reprovado, o canal será deletado **após 15 segundos**.

---

## 📌 Observações

- O bot é ideal para servidores RP do FiveM, mas pode ser adaptado para outros usos com whitelist.
- Evite reiniciar o bot várias vezes sem apagar mensagens anteriores no canal `CANAL_WL`, pois ele enviará novos botões a cada inicialização.

---

## 🛡️ Segurança

**⚠️ Nunca compartilhe o token do seu bot publicamente!**

O token presente no exemplo deve ser substituído por um token válido do seu bot e mantido **em segredo absoluto**.

Para maior segurança, você pode utilizar variáveis de ambiente ou arquivos `.env` para armazenar o token, como neste exemplo:

```python
import os

bot.run(os.getenv("DISCORD_BOT_TOKEN"))
```

E salvar seu token em um arquivo `.env`:

```
DISCORD_BOT_TOKEN=seu_token_aqui
```

---

🔗 **Feito para ajudar na gestão de Whitelist com facilidade e automação.**
