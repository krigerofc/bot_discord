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

          embed = disnake.Embed(title='Punição', description='EITA! alguém foi punido',colour=disnake.Colour.from_rgb(255, 0, 0)) 
          embed.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
          
          embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/1792/1792870.png')

          embed.add_field(name='Staff:', value=inter.author.name, inline=True)

          embed.add_field(name='Usuário Punido:', value=member.name,inline=True)

          embed.add_field(name='Motivo:',value=razao, inline=False)

          embed.add_field(name='Tipo de punição:', value='**kick**', inline=False)

          embed.set_image(url='https://media1.giphy.com/media/KmqxlCZgIUWe3z4yRD/giphy.gif?cid=ecf05e47pwckiq0u9x2i1ltvlncf19ou3xrtno2qdaqeftas&rid=giphy.gif&ct=g')
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

          embed = disnake.Embed(title='Punição', description='EITA! alguém foi punido', colour=disnake.Colour.from_rgb(255, 0, 0))

          embed.set_author(name=inter.guild.name, icon_url=inter.guild.icon)

          embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/1792/1792870.png')

          embed.add_field(name='Staff:', value=inter.author.name, inline=True)

          embed.add_field(name='Usuário Punido:', value=membro.name,inline=True)

          embed.add_field(name='Motivo:',value=razao, inline=False)

          embed.add_field(name='Tipo de punição:', value='**ban**', inline=False)

          embed.set_image(url='https://media4.giphy.com/media/3ohzdOOXqGR7sFyMoM/giphy.gif?cid=ecf05e47hpzoxlx4h1zxxtte1sl2mdjrw7v96ih2ynzmvb1t&rid=giphy.gif&ct=g')
          await inter.send(embed=embed)
          
        elif inter.author.guild_permissions.administrator == False:
          erro = disnake.Embed(title='ALERTA!!', description='**Apenas para STAFFS**', colour=disnake.Colour.from_rgb(255, 0, 0))
          erro.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2780/2780146.png')
          erro.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
          await inter.send(embed=erro)
      except:
          await inter.send('O bot não pode fazer isso.')

    @commands.slash_command(name='anunciar',description='Use o bot para anunciar algo')
    async def anuncio(self,inter:disnake.ApplicationCommandInteraction, anuncio, anuncio_desc, link_associado='', imagem_link='', categoria='', texto_cate='', categoria2='', texto_cate2=''):
        if inter.author.guild_permissions.manage_messages:
          anuncio2 = disnake.Embed(title=anuncio, description=anuncio_desc, colour=disnake.Colour.from_rgb(128, 0, 255))

          anuncio2.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/1759/1759283.png')

          anuncio2.set_author(name=inter.guild.name, icon_url=inter.guild.icon)

          anuncio2.add_field(name=categoria, value=texto_cate, inline=False)

          anuncio2.add_field(name=categoria2, value=texto_cate2, inline=False)

          anuncio2.set_image(url=f'{imagem_link}')
          if link_associado != '':
            anuncio2.add_field(name='link Associado', value=f'{link_associado}', inline=False)
          await inter.send(embed=anuncio2, allowed_mentions=disnake.AllowedMentions(users=True), content='||@everyone||')
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

        limpo.add_field(name='Quantidade:', value=f'{quantidade} mensagens apagadas.', inline=True)
        await inter.send(embed=limpo)
      else:
        erro = disnake.Embed(title='ALERTA!!', description='**Apenas para STAFFS**', colour=disnake.Colour.from_rgb(255, 0, 0))
        erro.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2780/2780146.png')
        erro.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
        await inter.send(embed=erro)


    @commands.slash_command(name='ticket', description='Abra ticket de suporte para os staff te ajudarem')
    async def criar(self, inter:disnake.ApplicationCommandInteraction, id_cargo_staff):
      if inter.author.guild_permissions.administrator:
        ticket  = disnake.Embed(title='🔔 Suporte 24h', description='Olá, este é o chat de suporte.\nCaso tenha alguma dúvida ou problema basta apertar o botão abaixo e um ticket será criado, assim um staff irá te ajudar!', colour=disnake.Colour.from_rgb(128, 0, 255))
        ticket.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/5821/5821865.png')
        ticket.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
        visual = disnake.ui.View(timeout=None)
        menu = disnake.ui.Button(label='Abrir ticket', custom_id='ticket1', style=disnake.ButtonStyle.blurple, emoji='📢')
        menu.is_persistent()

        async def criar_ticker(inter:disnake.MessageInteraction):
          staff = disnake.utils.get(inter.guild.roles, id=int(id_cargo_staff))
          verificar = inter.channel.threads
          if disnake.utils.get(verificar, name=inter.author.name):
            alerta = disnake.Embed(title='Opa, opa...', description='Você já tem um ticket em aberto!!\nAguarde ou feche o anterior.', colour=disnake.Colour.from_rgb(128, 0, 255))
            alerta.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/3472/3472621.png')
            alerta.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
            dm = await inter.author.create_dm()
            await dm.send(embed=alerta)
            await inter.send('Ops, verifique seu privado...', delete_after=5, ephemeral=True)

          else:
            thread = await inter.channel.create_thread(name=inter.author.name, type=disnake.ChannelType.private_thread, reason='Pedido de Suporte')

            new_chat = disnake.Embed(title='🎫Ticket Aberto', description=f'Olá, {inter.author.name}\nVocê acabou de abrir um ticket!\nEscreva abaixo qual seu problema e\nAguarde um staff para atende-lo.', colour=disnake.Colour.from_rgb(128, 0, 255))
            new_chat.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/10135/10135912.png')
            new_chat.set_author(name=inter.guild.name, icon_url=inter.guild.icon)

            visual2 = disnake.ui.View(timeout=None)
            fechar_ticket = disnake.ui.Button(label='Fechar ticket', emoji='❌', style=disnake.ButtonStyle.blurple, custom_id='fechar')
            async def fechar(inter:disnake.MessageInteraction):
              await thread.delete(reason='Ticket encerrado')

            visual2.add_item(fechar_ticket) 
            fechar_ticket.callback = fechar
            await thread.send(embed=new_chat , content=f'||{inter.author.mention} {staff.mention}||', view=visual2)
            await inter.send('Ticket criado com sucesso', delete_after=5, ephemeral=True )
            
        # conintinuação do embed do menu de suporte
        visual.add_item(menu)
        menu.callback = criar_ticker
        await inter.send(embed=ticket, view=visual)
      else:
        erro = disnake.Embed(title='ALERTA!!', description='**Apenas para STAFFS**', colour=disnake.Colour.from_rgb(255, 0, 0))
        erro.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/2780/2780146.png')
        erro.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
        await inter.send(embed=erro)

    #@commands.slash_command(name='mute', description='Mute um')
# parametro bot definido como tipo commandos.Bot() para aceitar apenas bot
# adicionando a engranagem(cog) menu e mandando de parametro para a classe o bot
# onde a classe vai acessar a engrenagem do bot
def setup(bot:commands.Bot):
  bot.add_cog(Menu(bot))