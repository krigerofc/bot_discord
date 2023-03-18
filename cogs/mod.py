import disnake
from disnake.ext import commands

#classe menu é filha da engrenagem(cog) que é filha dos comandos botando tudo no bot
class Menu(commands.Cog):
    def __init__(self, bot: commands.Bot):
        #definimos que o bot deve ser do tipo commands.Bot ou seja o parametro só aceita esse tipo 
        self.bot = bot
      
    @commands.slash_command(name="lypos", description="lypos ficaria feliz ao te ouvir")
    async def hello(self, inter:disnake.ApplicationCommandInteraction):
        f ='Lypos'
        for c in range(1,11):
          await inter.send(f)


#função de setup para carregar a engrenagem quando o main tiver rodando
# parametro bot definido como tipo commandos.Bot() para aceitar apenas bot
def setup(bot:commands.Bot):
  bot.add_cog(Menu(bot))