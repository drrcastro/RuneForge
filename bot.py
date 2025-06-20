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
    'A': 'Λ', 'B': 'ᛒ', 'C': 'ᚲ', 'D': 'ᛞ', 'E': 'Σ',
    'F': 'Ϝ', 'G': 'ᚷ', 'H': 'ᚺ', 'I': 'Ι', 'J': 'ᛃ',
    'K': 'ᚲ', 'L': 'ᛚ', 'M': 'ᛗ', 'N': 'И', 'O': 'Ø',
    'P': 'ᛈ', 'Q': 'Ϙ', 'R': 'ᚱ', 'S': 'ᛋ', 'T': 'ᛏ',
    'U': 'ᚢ', 'V': 'Ѵ', 'W': 'ᚹ', 'X': '⚒', 'Y': 'ᛃ', 'Z': 'ᛉ'
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
async def converter(ctx, *, frase):
    convertido = converter_frase(frase)
    await ctx.send(f"🔤 **Convertido:** `{convertido}`")

# Rodar o bot
bot.run(TOKEN)
