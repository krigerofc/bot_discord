import disnake
from disnake.ext import commands

class Diversao(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.slash_command(name='dado', description='Role um dado de 1-20')
    async def dado(self, inter:disnake.ApplicationCommandInteraction):
        from random import randint
        dado = randint(1,20)
        embed_dado = disnake.Embed(title='🎲 Dado rolando!!', description=f'rolando...O dado caiu em: **{dado}**', colour=disnake.Colour.from_rgb(128, 0, 255))
        embed_dado.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
        embed_dado.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/6729/6729805.png')
        await inter.send(embed=embed_dado)



    @commands.slash_command(name='say', description='Irei falar algo que você mandar')
    async def say(self, inter:disnake.ApplicationCommandInteraction, texto):
        txt = f'{texto}'
        await inter.send(content=txt, allowed_mentions=disnake.AllowedMentions(users=True))



    @commands.slash_command(name='userinfo', description='Descrição de um membro')
    async def info(self, inter:disnake.ApplicationCommandInteraction, membro:disnake.Member):
        info = disnake.Embed(title='User info', description='Comando para ver informações sobre alguém', colour=disnake.Colour.from_rgb(128, 0, 255))

        data = {'dia':str(membro.created_at.day),
                'mes':str(membro.created_at.month),
                'ano':str(membro.created_at.year)}
        
        info.add_field(name='👤 User:', value=f'{membro}', inline=False)

        if len(data['dia']) == 1 and len(data['mes']) == 1:
            info.add_field(name='🔧 Criação:',value=f'0{data["dia"]}/0{data["mes"]}/{data["ano"]}',inline=False)
        else:
            info.add_field(name='🔧 Criação:',value=f'{data["dia"]}/{data["mes"]}/{data["ano"]}',inline=False)

        info.add_field(name='🎫 Id:', value=f'{membro.id}', inline=False)
        info.set_thumbnail(url=membro.avatar)
        info.set_author(name=inter.guild.name, icon_url=inter.guild.icon)

        view = disnake.ui.View()
        botao = disnake.ui.Button(label='Avatar', custom_id='Avatar', style=disnake.ButtonStyle.blurple, emoji='🖼')
        view.add_item(botao)


        async def press(inter:disnake.MessageInteraction):
            avatar = disnake.Embed(title=membro.name, description=f'Avatar de {membro.name}', colour=disnake.Colour.from_rgb(128, 0, 255))
            avatar.set_image(url=membro.avatar)
            await inter.send(embed=avatar)


        botao.callback = press
        await inter.send(embed=info, view=view)



    @commands.slash_command(name='abraçar', description='de um abraço em alguém')
    async def abracar(self, inter:disnake.ApplicationCommandInteraction, membro:disnake.Member):
        from random import randint
        gifs = ['https://media0.giphy.com/media/PHZ7v9tfQu0o0/giphy.gif?cid=ecf05e478tirtncbbkk6j160hi603fzfhu2ltwmwm6f8nn1x&rid=giphy.gif&ct=g',
                'https://media2.giphy.com/media/Y8wCpaKI9PUBO/giphy.gif?cid=ecf05e47m9m1nmm4740zcvi0pp1l99crvd7yroek3foj4dkg&rid=giphy.gif&ct=g',
                'https://media3.giphy.com/media/143v0Z4767T15e/giphy.gif?cid=ecf05e478tirtncbbkk6j160hi603fzfhu2ltwmwm6f8nn1x&rid=giphy.gif&ct=g',
                'https://media1.giphy.com/media/5eyhBKLvYhafu/giphy.gif?cid=ecf05e47jyeie0o5gq4jsd8g12zonv0x0cxksjiulhs75xuu&rid=giphy.gif&ct=g',
                'https://media1.giphy.com/media/lrr9rHuoJOE0w/giphy.gif?cid=ecf05e47hsb3ouy954fin75vy0az49elhwbfb1i9o6ck7pre&rid=giphy.gif&ct=g',
                'https://media1.giphy.com/media/ythHeq4Qgx2De/giphy.gif?cid=ecf05e47jyeie0o5gq4jsd8g12zonv0x0cxksjiulhs75xuu&rid=giphy.gif&ct=g']
        sorteio = randint(0, len(gifs))

        hug = disnake.Embed(title='💗!', description=f'{inter.author.mention} **deu um abraço em** {membro.mention}', colour=disnake.Colour.from_rgb(128, 0, 255))
        hug.set_image(url=gifs[sorteio])

        await inter.send(embed=hug, allowed_mentions=disnake.AllowedMentions(users=True), content=f'||{inter.author.mention} {membro.mention}||')



    @commands.slash_command(name='beijar', description='de um beijo em alguém')
    async def kiss(self, inter:disnake.ApplicationCommandInteraction, membro:disnake.Member):
        from random import randint

        gifs = ['https://media2.giphy.com/media/wOtkVwroA6yzK/giphy.gif?cid=ecf05e478cs2c10ogv744jjx4la3x8a1lipv9e0zwvcwo0rn&rid=giphy.gif&ct=g',
                'https://media4.giphy.com/media/FqBTvSNjNzeZG/giphy.gif?cid=ecf05e478cs2c10ogv744jjx4la3x8a1lipv9e0zwvcwo0rn&rid=giphy.gif&ct=g',
                'https://media4.giphy.com/media/QGc8RgRvMonFm/giphy.gif?cid=ecf05e478cs2c10ogv744jjx4la3x8a1lipv9e0zwvcwo0rn&rid=giphy.gif&ct=g',
                'https://media3.giphy.com/media/11rWoZNpAKw8w/giphy.gif?cid=ecf05e478cs2c10ogv744jjx4la3x8a1lipv9e0zwvcwo0rn&rid=giphy.gif&ct=g',
                'https://media0.giphy.com/media/EVODaJHSXZGta/giphy.gif?cid=ecf05e47lry0kafea5bw41atharic9wrdrb9mtgj8e6pq0al&rid=giphy.gif&ct=g']
        sorteio = randint(0, len(gifs))

        bj = disnake.Embed(title='💕!', description=f'{inter.author.mention} **deu um beijo em** {membro.mention}', colour=disnake.Colour.from_rgb(128, 0, 255))
        bj.set_image(url=gifs[sorteio])

        await inter.send(embed=bj, allowed_mentions=disnake.AllowedMentions(users=True), content=f'||{inter.author.mention} {membro.mention}||')



    @commands.slash_command(name='tapa', description='você pode da um tapa em alguém')
    async def tapa(self, inter:disnake.ApplicationCommandInteraction, membro:disnake.Member):
        from random import randint

        gifs = ['https://media3.giphy.com/media/Zau0yrl17uzdK/giphy.gif?cid=ecf05e47qzu1f69ucu63j8d2mvh31ivz5rfyl7nzqb4347ej&rid=giphy.gif&ct=g',
                'https://media3.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif?cid=ecf05e47qzu1f69ucu63j8d2mvh31ivz5rfyl7nzqb4347ej&rid=giphy.gif&ct=g',
                'https://media1.giphy.com/media/k1uYB5LvlBZqU/giphy.gif?cid=ecf05e47qzu1f69ucu63j8d2mvh31ivz5rfyl7nzqb4347ej&rid=giphy.gif&ct=g',
                'https://media3.giphy.com/media/xUNd9HZq1itMkiK652/giphy.gif?cid=ecf05e47qzu1f69ucu63j8d2mvh31ivz5rfyl7nzqb4347ej&rid=giphy.gif&ct=g']
        sorteio = randint(0, len(gifs))

        tapa = disnake.Embed(title='🚨 Treta!', description=f'{inter.author.mention} **deu um tapa em** {membro.mention}', colour=disnake.Colour.from_rgb(128, 0, 255))
        tapa.set_image(url=gifs[sorteio])

        await inter.send(embed=tapa, allowed_mentions=disnake.AllowedMentions(users=True), content=f'||{inter.author.mention} {membro.mention}||')



    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        from random import randint

        tupla_de_frases = ("Sim", "Não", "Você é estranho...", "Olá esquisitinho", "você acha?",
                           "Será ?", "Me explique melhor", "Talvez o silêncio seja a melhor opção",
                           'Eu prefiro não comentar.', 'SIM, SIM!!', 'Como não pensei nisso antes?',
                           'Quanta burrice', 'Ave maria', 'Vish, começou a delirar', 'você tem certeza?'
                           'Dessa vez vou ficar de fora', 'QUEM ESTÁ TIRANDO MEU SONO😡', 'Inocente',
                           'Sua cara não queima?', 'Discordo totalmente', 'Sou um anjo', 'Prefiro um sorvete',
                           'Chora', 'rapaz...')

        palavra = tupla_de_frases[randint(0, len(tupla_de_frases)-1)]
        
        if 'kriger' in message.content:
            await message.channel.send(content=f'{palavra}')




def setup(bot:commands.Bot):
    bot.add_cog(Diversao(bot))