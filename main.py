import disnake
from disnake.ext import commands

# acessando o bot
# carregando a engrenagem(cog) de moderação 
intents = disnake.Intents.all()
bot = commands.Bot(intents = disnake.Intents.all())
bot.load_extension("cogs.moderation.mod")
bot.load_extension('cogs.fast.menus')
bot.load_extension('cogs.fun.diver')
bot.load_extension('cogs.fun.economia')

# quando o bot estiver pronto ele vai aviasar
@bot.event
async def on_ready():
  print("O BOT KRIGER ESTÁ ON")
  await bot.change_presence(activity=disnake.Activity(name='Use /comandos para ver os comandos', type=disnake.ActivityType.playing))
# iniciando o bot de chave ---

bot.run("NjExODE1MjM2NTkyMjA1ODI0.GiJRrB.2b5Xd4OOo9DyzqzDZwPshxT6As9rZaKlDK3EgU")
