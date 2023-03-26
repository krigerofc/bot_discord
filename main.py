import disnake
from disnake.ext import commands

# acessando o bot
# carregando a engrenagem(cog) de moderação 
bot = commands.Bot()
bot.load_extension("cogs.moderation.mod")
bot.load_extension('cogs.fast.menus')

# quando o bot estiver pronto ele vai aviasar
@bot.event
async def on_ready():
  print("O BOT KRIGER ESTÁ ON")

# iniciando o bot de chave ---
bot.run("")
