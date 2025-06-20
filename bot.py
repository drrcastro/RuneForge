import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Carregar o token do arquivo .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents necessários
intents = discord.Intents.default()
intents.message_content = True

# Prefixo do bot (!converter)
bot = commands.Bot(command_prefix="!", intents=intents)

# Mapa de substituições A-Z (visual/runas)
substituicoes = {
    'A': 'Λ', 'B': 'ᛒ', 'C': 'C', 'D': 'D', 'E': 'Σ',
    'F': 'F', 'G': 'G', 'H': 'ᚺ', 'I': 'I', 'J': 'J',
    'K': 'ꓘ', 'L': 'L', 'M': 'ᛗ', 'N': 'Π', 'O': 'Ø',
    'P': 'P', 'Q': 'Ϙ', 'R': 'Я', 'S': 'S', 'T': 'ᛏ',
    'U': 'V', 'V': '∇', 'W': 'W', 'X': 'X', 'Y': 'Ψ', 'Z': 'Z'
}

# Função que converte a frase
def converter_frase(frase):
    return ''.join(substituicoes.get(c.upper(), c) for c in frase)

# Evento on_ready
@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# Comando !converter
@bot.command()
async def forge(ctx, *, frase):
    convertido = converter_frase(frase)
    await ctx.send(f"⚔️{convertido}⚔️")

# Rodar o bot
bot.run(TOKEN)
