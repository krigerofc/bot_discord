import disnake
from disnake.ext import commands

#classe menu é filha da engrenagem(cog) que é filha dos comandos botando tudo no bot
class Menu(commands.Cog):
    def __init__(self, bot: commands.Bot):
        #definimos que o bot deve ser do tipo commands.Bot ou seja o parametro só aceita esse tipo 
        self.bot = bot
      

    @commands.slash_command(name="rr", description="reini")
    async def rr(self,inter:disnake.ApplicationCommandInteraction):
      await inter.send('Bot desligado')
      await self.bot.close()
    
    
    #comando e kick
    @commands.slash_command(naame='kick', description='de kick a um membro que não está nos conformes')
    async def kick(self, inter:disnake.ApplicationCommandInteraction, member:disnake.Member, razao):
      try:
        if inter.author.guild_permissions.kick_members: # verificar se tem permissão de admin
          await inter.guild.kick(user=member, reason=razao) # da kick no membro selecionado

          embed = disnake.Embed(title='Punição', description='Registro de punição',colour=disnake.Colour.from_rgb(239, 255, 0)) 
          embed.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
          
          embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/1792/1792870.png')

          embed.add_field(name='Staff', value=inter.author.name, inline=False)

          embed.add_field(name='Usuário Punido', value=member.name, inline=False)

          embed.add_field(name='Motivo',value=razao, inline=False)

          embed.add_field(name='Tipo de punição', value='kick', inline=False)
          await inter.send(embed=embed) #criação do embed e executalo no final 
        elif inter.author.guild_permissions.administrator == False:
          erro = disnake.Embed(title='ALERTA!!', description='**Apenas para STAFFS**', colour=disnake.Colour.from_rgb(255, 0, 0))
          erro.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2780/2780146.png')
          erro.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
          await inter.send(embed=erro)
      except:
        await inter.send('O bot não tem permissão para isso.')# caso tente se auto expulsar, expulsar superioes e etc


    @commands.slash_command(name='ban', description='Dê ban aos membros que não estão seguindo as regras')
    async def ban(self, inter:disnake.ApplicationCommandInteraction, membro:disnake.Member, razao):
      try:
        if inter.author.guild_permissions.ban_members:
          await inter.guild.ban(user=membro, reason=razao)

          embed = disnake.Embed(title='Punição', description='Registro de punição', colour=disnake.Colour.from_rgb(255, 0, 0))

          embed.set_author(name=inter.guild.name, icon_url=inter.guild.icon)

          embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/1792/1792870.png')

          embed.add_field(name='Staff', value=inter.author.name, inline=False)

          embed.add_field(name='Usuário Punido', value=membro.name, inline=False)

          embed.add_field(name='Motivo',value=razao, inline=False)

          embed.add_field(name='Tipo de punição', value='BAN', inline=False)
          await inter.send(embed=embed)
        elif inter.author.guild_permissions.administrator == False:
          erro = disnake.Embed(title='ALERTA!!', description='**Apenas para STAFFS**', colour=disnake.Colour.from_rgb(255, 0, 0))
          erro.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2780/2780146.png')
          erro.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
          await inter.send(embed=erro)
      except:
          await inter.send('O bot não pode fazer isso.')

    @commands.slash_command(name='anunciar',description='Use o bot para anunciar algo')
    async def anuncio(self,inter:disnake.ApplicationCommandInteraction, anuncio, link_associado='', imagem_link='', categoria='', texto_cate='', categoria2='', texto_cate2=''):
        if inter.author.guild_permissions.administrator:
          anuncio2 = disnake.Embed(title='Anuncio!!',description=anuncio,colour=disnake.Colour.from_rgb(128, 0, 255))

          anuncio2.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/1759/1759283.png')

          anuncio2.set_author(name=inter.guild.name, icon_url=inter.guild.icon)

          anuncio2.add_field(name=categoria, value=texto_cate, inline=False)

          anuncio2.add_field(name=categoria2, value=texto_cate2, inline=False)

          anuncio2.set_image(url=f'{imagem_link}')
          if link_associado != '':
            anuncio2.add_field(name='link Associado', value=f'{link_associado}', inline=False)
          await inter.send(embed=anuncio2,allowed_mentions=disnake.AllowedMentions(users=True), content='||@everyone||')
        else:
            erro = disnake.Embed(title='ALERTA!!', description='**Apenas para STAFFS**', colour=disnake.Colour.from_rgb(255, 0, 0))
            erro.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2780/2780146.png')
            erro.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
            await inter.send(embed=erro)

    @commands.slash_command(name='clear', description='quantidade de mensagens')
    async def apagar(self, inter:disnake.ApplicationCommandInteraction, quantidade:int):
      if inter.author.guild_permissions.manage_messages:
        await inter.channel.purge(limit=quantidade)
        limpo = disnake.Embed(title='Limpeza!', description='**Mensagens apagadas**', colour=disnake.Colour.from_rgb(128, 0, 255))

        limpo.set_author(name=inter.guild.name, icon_url=inter.guild.icon)

        limpo.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/5508/5508841.png')

        limpo.add_field(name='Staff:', value=inter.author.name, inline=True)

        limpo.add_field(name='Quantidade:', value=f'{quantidade} mensagens apagadas.', inline=False)
        await inter.send(embed=limpo)
      else:
        erro = disnake.Embed(title='ALERTA!!', description='**Apenas para STAFFS**', colour=disnake.Colour.from_rgb(255, 0, 0))
        erro.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2780/2780146.png')
        erro.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
        await inter.send(embed=erro)

# parametro bot definido como tipo commandos.Bot() para aceitar apenas bot
# adicionando a engranagem(cog) menu e mandando de parametro para a classe o bot
# onde a classe vai acessar a engrenagem do bot
def setup(bot:commands.Bot):
  bot.add_cog(Menu(bot))