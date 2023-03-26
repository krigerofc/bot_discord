import disnake
from disnake.ext import commands

class Velo(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.slash_command(name='regras', description='Vou criar uma lista de regras para seu servidor')
    async def rules(self, inter:disnake.ApplicationCommandInteraction):
      if inter.author.guild_permissions.administrator:
        rules = disnake.Embed(title='REGRAS DO SERVIDOR:',description=f'''Olá, bem-vindo!
          Neste canal você vai conseguir ver as regras,
          abaixo tem uma lista de coisas proibidas.''', colour=disnake.Colour.from_rgb(128, 0, 255))
        
        rules.set_author(name=inter.guild.name, icon_url=inter.guild.icon)   

        rules.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/9377/9377154.png')

        rules.add_field(name='TERMOS PROIBIDOS:',
          value='''É proibida a utilização de termos que remetem a
          assuntos que se destacam-se associados a:
          pedofilia, toxidade e preconceito.''',inline=False)
        
        rules.add_field(name='COMUNIDADE:',
          value='''Qualquer violação das regras
          resultará em sua remoção do servidor.''',inline=False)
        
        rules.add_field(name='POLUIÇÃO VISUAL:',
          value='''É proibido o envio de mensagens em massa
          que sejá repetidas,longas ou desnecessárias.''',inline=False)
        
        rules.add_field(name='POLUIÇÃO SONORA:',
          value='''É proibido colocar músicas altas ou
          estourada, uso de voicemod, ou gritos em call.''',inline=False)

        rules.add_field(name='INFORMAÇÕES PESSOAIS:',
          value='''Proibido stalkear e/ou divulgar fotos,
          informações pessoais,incluindo números e etc.''',inline=False)
        
        rules.add_field(name='RESPEITO:',
          value='''Proibido qualquer tipo de racismo ou
          apologia a movimentos de odios, homofóbia e
          qualquer tipo de discriminação.''',inline=False)
        
        rules.set_image(url='https://th.bing.com/th/id/R.facb68ea2c536d612b90d48744639367?rik=e2soUsNOCeqrTA&pid=ImgRaw&r=0')
        rules.set_footer(text='Criador por:  ! │†「𝒌𝒓𝒊𝒈𝒆𝒓」† │#8700  | INSTA: @pedro.kriger',
          icon_url='https://cdn-icons-png.flaticon.com/512/1070/1070943.png')      
      
        await inter.send(embed=rules)
      elif inter.author.guild_permissions.administrator == False:
          erro = disnake.Embed(title='ALERTA!!', description='**Apenas para STAFFS**', colour=disnake.Colour.from_rgb(255, 0, 0))
          erro.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2780/2780146.png')
          erro.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
          await inter.send(embed=erro)

    # comando usando /, nome do comando e descrição
    # função hello self(acessando bot), inter para acesar o contexto
    @commands.slash_command(name="help", description="Menu sobre o bot")
    async def hello(self, inter:disnake.ApplicationCommandInteraction):
      #criação do embed
      menu = disnake.Embed(title='Menu de ajuda',
        description=f'''Olá, **{inter.author.name}**
        Aqui você receberá todo o apoio possível.
        Bem-vind(a) a: **{inter.guild.name}**
        
        Além do mais o servidor contém o **Kriger BOT**
        Que é programado para administrar e divertir.
        /help2 para ver os comandos.''',colour=disnake.Colour.from_rgb(128, 0, 255))
      #foto ao lado
      menu.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/1660/1660114.png')
      #author é o que aparece em primeiro
      menu.set_author(name=inter.guild.name,
        icon_url=inter.guild.icon)  
      menu.add_field(name='Servidor de Suporte', value='https://discord.gg/uDUDuUGdDR', inline=True)
      menu.add_field(name='Comandos administrativos',
       value='O Bot tem a proposta de acelerar e ajudar\nno gerencimento dos servidores.', inline=False)
      #mensagem separadas como se fosse categorias
      menu.add_field(name='Comandos de diversão',
        value='Além de gerir o bot mantem contato com\nos membros usando comandos divertidos', inline=False)
      #foto do servidor no final
      menu.set_image(url='https://images.wallpapersden.com/image/download/new-york-buildings-night_ZmxmZm6UmZqaraWkpJRmbmdlrWZnZWU.jpg')
      # ultimas letrinhas em baixo do embed
      menu.set_footer(text='Criador por:  ! │†「𝒌𝒓𝒊𝒈𝒆𝒓」† │#8700  | INSTA: @pedro.kriger',
        icon_url='https://cdn-icons-png.flaticon.com/512/1070/1070943.png')
      #publicação do embed
      await inter.send(embed=menu)
            
    @commands.slash_command(name='comandos', description='Lista de comandos.')
    async def list_commands(self, inter:disnake.ApplicationCommandInteraction):
       ajuda = disnake.Embed(title='Lista de comandos',
        description=f'''A seguir uma lista de todos os comandos do bot.

        **Administração:**
        **/Kick** Para os staff expulsarem membros.
        **/ban** Para os staff banir membros.
        **/help** Uma introdução ao bot.
        **/comandos** Lista de commandos.
        **/regras** Defina regras prontas a seu servidor.
        **/Anunciar** Anuncios pequenos e simples
        **/clear ** quantidade de mensagens para apagar.

        **Diversão:**''',colour=disnake.Colour.from_rgb(128, 0, 255))
       
       ajuda.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
       ajuda.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4699/4699831.png")
       await inter.send(embed=ajuda)

def setup(bot:commands.Bot):
    bot.add_cog(Velo(bot))