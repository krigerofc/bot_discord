import disnake
from disnake.ext import commands

bot = commands.Bot()
bot.load_extension("cogs.mod")


@bot.event
async def on_ready():
  print("O BOT KRIGER ESTÁ ON")


bot.run(
  "")
