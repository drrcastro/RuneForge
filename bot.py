import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Necessário para ler mensagens com comandos normais

bot = commands.Bot(command_prefix="!", intents=intents)

# Dicionário personalizado de substituições
substituicoes = {
   'A': 'Λ', 
   'B': 'ᛒ', 
   'C': 'C', 
   'D': 'ᛞ', 
   'E': 'Σ',
   'F': 'Ϝ', 
   'G': 'ᚷ', 
   'H': 'ᚺ', 
   'I': 'Ι', 
   'J': 'J',
   'K': 'K', 
   'L': 'ᛚ', 
   'M': 'ᛗ', 
   'N': 'И', 
   'O': 'Ø',
   'P': 'P', 
   'Q': 'Ϙ', 
   'R': 'ᚱ', 
   'S': 'S', 
   'T': 'T',
   'U': 'ᚢ', 
   'V': 'Ѵ', 
   'W': 'ᚹ', 
   'X': 'X', 
   'Y': 'Y', 
   'Z': 'Z'
}

def converter_frase(frase):
    return ''.join(substituicoes.get(c.upper(), c) for c in frase)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

@bot.command()
async def rune(ctx, *, frase):
    resultado = converter_frase(frase)
    await ctx.send(f'🔤 **Forged:** `{resultado}`')

# Coloque o token do bot aqui
bot.run("TOKEN")
