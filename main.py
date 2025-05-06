import discord
from discord.colour import Color
from discord.ext import commands
from discord.ui import Button, View, Modal, TextInput
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# IDs fixos
CANAL_WL = 1364997491568808047
CATEGORIA_WL = 1364997526712881223
CANAL_RESULTADO = 1364998988171841548
CARGO_APROVADO = 1364997695361515600


# Envia o embed com botão ao iniciar
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    canal = bot.get_channel(CANAL_WL)
    if canal:
        embed = discord.Embed(
            title=":fire:Você está pronto para viver a Realidade?",
            description=
            "Você está a um passo de pedir um registro em São Paulo para viver uma nova Realidade! Antes de continuarmos, pedimos que verifique o canal ⁠(#ALLOW LIST).",
            color=discord.Color.blurple())
        view = View()
        view.add_item(WLButton())
        await canal.send(embed=embed, view=view)


# Botão que abre o modal
class WLButton(Button):

    def __init__(self):
        super().__init__(label="Fazer WL", style=discord.ButtonStyle.primary)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_modal(WLModal())


# Modal com perguntas
class WLModal(Modal, title="Whitelist - Responda abaixo"):
    q1 = TextInput(label="Qual seu nome?", placeholder="Digite seu nome")
    q2 = TextInput(label="Idade", placeholder="Digite sua idade")
    q3 = TextInput(label="Conte-nos a história do seu personagem:",
                   placeholder="Crie uma história para seu personagem")
    q4 = TextInput(
        label="Qual rumo você irá seguir na cidade?",
        placeholder="Bandido,Polícia,Empresarial,Mecânica,Hospital...")
    q5 = TextInput(label="Como você nos conheceu?",
                   placeholder="Lista FiveM,Amigos,Instagram,YouTuber,Etc.")

    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        user = interaction.user
        category = guild.get_channel(CATEGORIA_WL)

        overwrites = {
            guild.default_role:
            discord.PermissionOverwrite(view_channel=False),
            user:
            discord.PermissionOverwrite(view_channel=True,
                                        send_messages=False),
        }

        try:
            canal_wl = await guild.create_text_channel(name=f"wl-{user.name}",
                                                       category=category,
                                                       overwrites=overwrites)
        except discord.Forbidden:
            await interaction.response.send_message(
                "❌ Erro ao criar o canal. Verifique as permissões do bot.",
                ephemeral=True)
            return

        embed = discord.Embed(title=f"📄 Whitelist de {user}",
                              color=discord.Color.yellow())
        embed.add_field(name="Nome", value=self.q1.value, inline=False)
        embed.add_field(name="Idade", value=self.q2.value, inline=False)
        embed.add_field(name="História", value=self.q3.value, inline=False)
        embed.add_field(name="Rumo", value=self.q4.value, inline=False)
        embed.add_field(name="Como nos conheceu",
                        value=self.q5.value,
                        inline=False)

        view = View()
        view.add_item(AprovarButton(user.id))
        view.add_item(ReprovarButton(user.id))

        await canal_wl.send(embed=embed, view=view)
        await interaction.response.send_message(
            "✅ Sua whitelist foi enviada para análise.", ephemeral=True)


# Botão Aprovar
class AprovarButton(Button):

    def __init__(self, user_id):
        super().__init__(label="✅ Aprovar", style=discord.ButtonStyle.success)
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        member = interaction.guild.get_member(self.user_id)
        role = interaction.guild.get_role(CARGO_APROVADO)
        await member.add_roles(role)

        # Embed bonito
        embed_resultado = discord.Embed(
            title="✅ Whitelist Aprovada!",
            description="Parabéns! Sua whitelist foi aprovada com sucesso.",
            color=discord.Color.green())
        embed_resultado.set_footer(text="Bem-vindo ao REALIDADE RP!")

        canal_resultado = interaction.guild.get_channel(CANAL_RESULTADO)

        # Mencionar o usuário e mandar embed
        await canal_resultado.send(content=f"{member.mention}",
                                   embed=embed_resultado)

        # Tentar mandar DM
        try:
            await member.send(embed=discord.Embed(
                title="✅ Aprovado(a)!",
                description=
                "Parabéns! Você foi aprovado(a) na whitelist e já pode jogar no <#1306059695013756928>",
                color=discord.Color.green()))
        except discord.Forbidden:
            pass  # O usuário pode ter DMs fechadas

        await interaction.response.send_message(
            "✅ Canal será deletado em 60 segundos.", ephemeral=False)
        await asyncio.sleep(60)
        await interaction.channel.delete()


# Botão Reprovar
class ReprovarButton(Button):

    def __init__(self, user_id):
        super().__init__(label="❌ Reprovar", style=discord.ButtonStyle.danger)
        self.user_id = user_id

    async def callback(self, interaction: discord.Interaction):
        member = interaction.guild.get_member(self.user_id)

        embed_resultado = discord.Embed(
            title="❌ Whitelist Reprovada",
            description="Infelizmente, sua whitelist não foi aprovada.",
            color=discord.Color.red())
        embed_resultado.set_footer(text="Tente novamente.")

        canal_resultado = interaction.guild.get_channel(CANAL_RESULTADO)

        # Mencionar o usuário e mandar embed
        await canal_resultado.send(content=f"{member.mention}",
                                   embed=embed_resultado)

        # Tentar mandar DM
        try:
            await member.send(embed=discord.Embed(
                title="❌ Reprovado(a)",
                description=
                "Sua whitelist foi reprovada. Leia atentamente as regras e tente novamente se possível.",
                color=discord.Color.red()))
        except discord.Forbidden:
            pass  # DMs fechadas

        await interaction.response.send_message(
            "❌ Canal será deletado em 15 segundos.", ephemeral=False)
        await asyncio.sleep(15)
        await interaction.channel.delete()


# Rodar bot
bot.run(
    "COLOCAR O TOKEN PESSOAL")
