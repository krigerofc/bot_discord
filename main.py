import disnake
from disnake.ext import commands

# acessando o bot
# carregando a engrenagem(cog) de moderação 
intents = disnake.Intents.all()
bot = commands.Bot(intents = disnake.Intents.all())
bot.load_extension("cogs.moderation.mod")
bot.load_extension('cogs.fast.menus')
bot.load_extension('cogs.fun.diver')

# quando o bot estiver pronto ele vai aviasar
@bot.event
async def on_ready():
  print("O BOT KRIGER ESTÁ ON")
  await bot.change_presence(activity=disnake.Activity(name='Use /comandos para ver os comandos', type=disnake.ActivityType.playing))
# iniciando o bot de chave ---

bot.run("NjExODE1MjM2NTkyMjA1ODI0.GbKorz.LOR-KDym4D5OaTRY6aC8y86g2bn9HyrkYKHYsA")
