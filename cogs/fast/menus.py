import disnake
from disnake.ext import commands

class Velo(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.slash_command(name='regras', description='Vou criar uma lista de regras para seu servidor')
    async def rules(self, inter:disnake.ApplicationCommandInteraction):
      if inter.author.guild_permissions.administrator:
        rules = disnake.Embed(title='📌 REGRAS DO SERVIDOR:',description=f'''Olá, bem-vindo!\nEsté canal é para regras,\nabaixo tem uma lista de coisas proibidas.''', colour=disnake.Colour.from_rgb(128, 0, 255))
        
        rules.set_author(name=inter.guild.name, icon_url=inter.guild.icon)   

        rules.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/9377/9377154.png')

        rules.add_field(name='TERMOS PROIBIDOS:',
          value='''É proibida a utilização de termos e assuntos\nque se destacam-se associados a:\npedofilia, toxidade e preconceito.''',inline=False)
        
        rules.add_field(name='COMUNIDADE:',
          value='''Qualquer violação das regras\nresultará em sua remoção do servidor.''',inline=False)
        
        rules.add_field(name='POLUIÇÃO VISUAL:',
          value='''É proibido o envio de mensagens em massa\nque sejá repetidas,longas ou desnecessárias.''',inline=False)
        
        rules.add_field(name='POLUIÇÃO SONORA:',
          value='''É proibido colocar músicas altas ou\nestourada, uso de voicemod, ou gritos.''',inline=False)

        rules.add_field(name='INFORMAÇÕES PESSOAIS:',
          value='''Proibido stalkear e/ou divulgar fotos,\ninformações pessoais,incluindo números,etc.''',inline=False)
        
        rules.add_field(name='RESPEITO:',
          value='''Proibido qualquer tipo de racismo ou\napologia a movimentos de odios, homofóbia e\nqualquer tipo de discriminação.''',inline=False)
        
        rules.set_image(url='https://th.bing.com/th/id/R.facb68ea2c536d612b90d48744639367?rik=e2soUsNOCeqrTA&pid=ImgRaw&r=0')
        rules.set_footer(text='Criador por:  ! │†「𝒌𝒓𝒊𝒈𝒆𝒓」† │#8700  | INSTA: @pedro.kriger',
          icon_url='https://cdn-icons-png.flaticon.com/512/1070/1070943.png')      
      
        await inter.send(embed=rules)
      elif inter.author.guild_permissions.administrator == False:
          erro = disnake.Embed(title='ALERTA!!', description='**Apenas para STAFFS**', colour=disnake.Colour.from_rgb(255, 0, 0))
          erro.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2780/2780146.png')
          erro.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
          await inter.send(embed=erro)


    @commands.slash_command(name="help", description="Menu sobre o bot")
    async def hello(self, inter:disnake.ApplicationCommandInteraction):
      menu = disnake.Embed(title='❓ Menu de ajuda',
        description=f'''Olá, **{inter.author.name}**\nAqui você receberá todo o apoio possível.\nBem-vind(a) a: **{inter.guild.name}**\n\nAlém do mais o servidor contém o **Kriger**\nQue é programado para ajudar.\n/help2 para comandos\n/doar para apoiar o bot.'''
        ,colour=disnake.Colour.from_rgb(128, 0, 255))
      
      menu.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/1660/1660114.png')

      menu.set_author(name=inter.guild.name,icon_url=inter.guild.icon)  

      menu.add_field(name='Servidor de Suporte:', value='https://discord.gg/uDUDuUGdDR', inline=True)

      menu.add_field(name='Sobre a moderação:',value='O Bot tem a proposta de acelerar e ajudar\nno gerencimento dos servidores.', inline=False)

      menu.add_field(name='Sobre a diversão:',value='Além de gerir o bot mantem contato com\nos membros usando comandos divertidos.', inline=False)

      menu.set_image(url='https://images.wallpapersden.com/image/download/new-york-buildings-night_ZmxmZm6UmZqaraWkpJRmbmdlrWZnZWU.jpg')

      menu.set_footer(text='Criador por:  ! │†「𝒌𝒓𝒊𝒈𝒆𝒓」† │#8700  | INSTA: @pedro.kriger', icon_url='https://cdn-icons-png.flaticon.com/512/1070/1070943.png')

      await inter.send(embed=menu)
            
    @commands.slash_command(name='comandos', description='Lista de comandos.')
    async def list_commands(self, inter:disnake.ApplicationCommandInteraction):
       ajuda = disnake.Embed(title='Lista de comandos',
        description=f'''A seguir uma lista de todos os comandos do bot.\n
**Administração:**
**/Kick** Para os staff expulsarem membros.
**/ban** Para os staff banir membros.
**/help** Uma introdução ao bot.
**/comandos** Lista de commandos.
**/regras** Defina regras prontas.
**/Anunciar** Anuncios pequenos e simples
**/clear ** apagar mensagens.
**/doar** doações para apoiar o bot
**Ticket** Crie um chat suporte

**Diversão:**
**/beijar**Para dar beijinhos
**/Tapa**Bata em alguém
**/Abraçar**Dê um abraço''',colour=disnake.Colour.from_rgb(128, 0, 255))

       
       ajuda.set_author(name=inter.guild.name, icon_url=inter.guild.icon)

       ajuda.set_footer(text='Criador por:  ! │†「𝒌𝒓𝒊𝒈𝒆𝒓」† │#8700  | INSTA: @pedro.kriger', icon_url='https://cdn-icons-png.flaticon.com/512/1070/1070943.png')

       ajuda.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4699/4699831.png")

       await inter.send(embed=ajuda)

    @commands.slash_command(name='doar', description='Faça doações e mantenha o bot on!!')
    async def doando(self, inter:disnake.ApplicationCommandInteraction):
       apoio_embed = disnake.Embed(title='Apoie o Bot', description='Está afim de ajudar o bot e deixar online?\naceitamos doações como forma de apoio.\nAbaixo algumas formas de doação:',
        colour=disnake.Colour.from_rgb(128, 0, 255))

       apoio_embed.set_author(name=inter.guild.name, icon_url=inter.guild.icon)

       apoio_embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/3367/3367537.png')

       apoio_embed.add_field(name='💰 Pix:', value='https://picpay.me/cristiane.emerick/15.0 \n**Agradecemos a todos os apoiadores!!**', inline=False)

       apoio_embed.set_image(url='https://i.pinimg.com/originals/90/02/80/900280da46a3f73dfab435d5ef282469.jpg')

       apoio_embed.set_footer(text='Criador por:  ! │†「𝒌𝒓𝒊𝒈𝒆𝒓」† │#8700  | INSTA: @pedro.kriger', icon_url='https://cdn-icons-png.flaticon.com/512/1070/1070943.png')

       await inter.send(embed=apoio_embed)

def setup(bot:commands.Bot):
    bot.add_cog(Velo(bot))