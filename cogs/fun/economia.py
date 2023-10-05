import disnake
from disnake.ext import commands
import cogs.dados as dados

msql = dados.Msql_dados()

class Economia(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.slash_command(name='daily', description='Pegue suas moedas do dia!')
    async def daily(self, inter:disnake.ApplicationCommandInteraction):
        
        id = inter.user.id
        msql.criar_user(id)

        #dar dinheiro do daily
        dinheiro = msql.dar_dinheiro_daily(id)

        if isinstance(dinheiro, int):
            dinheiro_embed = disnake.Embed(title='💸 **Daily** 💸', description=f'Você acabou de sacar seu prêmio do dia!!', colour=disnake.Colour.from_rgb(128, 0, 255))
            dinheiro_embed.set_author(name=inter.guild.name, icon_url=inter.guild.icon)

            dinheiro_embed.set_image(url='https://media3.giphy.com/media/xTiTnqUxyWbsAXq7Ju/giphy.gif?cid=ecf05e47l0dsckxng09714y8e9w9zokp37rsoc1qiixy32cr&ep=v1_gifs_search&rid=giphy.gif&ct=g')
            dinheiro_embed.add_field(name='💰 Moedas:', value=f'Você acabou de ganhar **2000** moedas!!\n\n**Saldo atual: {int(dinheiro)}**', inline=True)

            await inter.send(embed=dinheiro_embed)
        elif isinstance(dinheiro, str):
            dinheiro_embed = disnake.Embed(title='👮 **PARADO**!', description=f'\n\nVocê já pegou seu prêmio do dia.\nAguarde o prazo de 24 horas acabar.', colour=disnake.Colour.from_rgb(255, 0, 0))
            dinheiro_embed.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
            dinheiro_embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/522/522554.png')

            await inter.send(embed=dinheiro_embed)
        

        
    @commands.slash_command(name='apostar', description='aposte para ganhar 2x mais moedas')
    async def apostar(self, inter:disnake.ApplicationCommandInteraction, valor:int):
        from random import randint

        msql.criar_user(inter.user.id)
        moeda = msql.dinheiro_quantidade(inter.user.id)
        numero_sorteado = randint(1, 10)


        cass_embed = disnake.Embed(title='🎲 **MAQUINA DE APOSTA** 💵', description=f'Você apostou **{valor}** moedas por 2x', colour=disnake.Colour.from_rgb(128, 0, 255))
        cass_embed.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
        cass_embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/445/445076.png')

        if moeda > 0 and valor <= moeda:
            if numero_sorteado % 2 == 0:
                
                msql.dar_dinheiro(inter.user.id, valor)
                moeda = msql.dinheiro_quantidade(inter.user.id)

                cass_embed.colour = disnake.Colour.from_rgb(0, 190, 0)
                cass_embed.add_field(name='💵 Resultado:', value=f'VOCÊ GANHOU!!!\nVocê acaba de ganhar: **{valor*2}**\n\nVocê tem um total de: **{moeda + valor}**', inline=True)
                cass_embed.set_image(url='https://media2.giphy.com/media/qH1jQOvi4WVEvCRvOg/giphy.gif?cid=ecf05e474taefc7iywp2yonqlloe4o6qdj8p1mm5p5q3ubey&ep=v1_gifs_related&rid=giphy.gif&ct=g')
                
                await inter.send(embed=cass_embed)
                
            else:
                msql.remover_moedas(inter.user.id, valor)
                moeda = msql.dinheiro_quantidade(inter.user.id)

                cass_embed.colour = disnake.Colour.from_rgb(190, 0, 0)
                cass_embed.add_field(name='🎲 Resultado:', value=f'VOCÊ PERDEU!!\nVocê acaba de perder: **{valor}**\n\nVocê tem um total de: **{moeda}**', inline=True)
                cass_embed.set_image(url='https://media0.giphy.com/media/xT9DPi61MmrDLzVFzq/giphy.gif?cid=ecf05e47wkh55t0vix4956tkobg18jiq6mtioculabac9094&ep=v1_gifs_related&rid=giphy.gif&ct=g')

                await inter.send(embed=cass_embed)
        else:
            await inter.send('Você não tem essa quantidade de moedas')
    

    @commands.slash_command(name='trabalhar', description='Trabalhe para conseguir moedinhas')
    async def trabalhar(self, inter:disnake.ApplicationCommandInteraction):
        from random import randint

        msql.criar_user(inter.user.id)

        sorte = randint(1, 100)

        resultado = msql.dar_dinheiro_trabalho(id_discord=inter.user.id, sorte=sorte)

        if resultado[0] == 'Você foi roubado':
            embed_roubo = disnake.Embed(title='🗣️ **MÃOS AO ALTO**!', description=f'\n\nHA HA HA! \nME PASSE TODO SEU DINHEIRO!\nAGORA!!', colour=disnake.Colour.from_rgb(190, 0, 0))
            embed_roubo.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
            
            embed_roubo.add_field(name='\n\n💸 Azar:', value=f'Você acabou de ser assaltado \ne acabou perdendo **{resultado[1]}** moedas', inline=True)
            embed_roubo.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/7792/7792678.png')
            embed_roubo.set_image(url='https://media0.giphy.com/media/HxgTc2NvIO6jowsknb/giphy.gif?cid=ecf05e47auktzk83nt6nxue9va4xz4bwxnpbtmtmten4hilr&ep=v1_gifs_related&rid=giphy.gif&ct=g')

            await inter.send(embed=embed_roubo)


        elif resultado[0] == 'Você achou um presente':
            embed_presente = disnake.Embed(title='📦 **UM PRESENTE MISTERIOSO**!', description=f'\n\nUAU!! Isso é incrível.\n Eu amei!', colour=disnake.Colour.from_rgb(128, 190, 255))
            embed_presente .set_author(name=inter.guild.name, icon_url=inter.guild.icon)
            
            embed_presente .add_field(name='\n\n⭐ Sorte em dobro:', value=f'Você ganhou um presente com\nUma carta e **{resultado[1]}** moedas!', inline=True)
            embed_presente .set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/3850/3850991.png')
            embed_presente .set_image(url='https://media1.giphy.com/media/xTiTnhCc4SeRW74zBK/giphy.gif?cid=ecf05e47kuxpnu27v16k9umwc951wx6zekywxb7gp8l543km&ep=v1_gifs_search&rid=giphy.gif&ct=g')

            await inter.send(embed=embed_presente)


        else:
            gifs = ['https://media3.giphy.com/media/ThrM4jEi2lBxd7X2yz/giphy.gif?cid=ecf05e47pgspx162ohxy0etpjly9ckefyrb05v6g25cwq1mu&ep=v1_gifs_search&rid=giphy.gif&ct=g',
                    'https://media4.giphy.com/media/5Zesu5VPNGJlm/giphy.gif?cid=ecf05e47pgspx162ohxy0etpjly9ckefyrb05v6g25cwq1mu&ep=v1_gifs_search&rid=giphy.gif&ct=g',
                    'https://media3.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif?cid=ecf05e47pgspx162ohxy0etpjly9ckefyrb05v6g25cwq1mu&ep=v1_gifs_search&rid=giphy.gif&ct=g',
                    'https://media4.giphy.com/media/RH1IFq2GT0Oau8NRWX/giphy.gif?cid=ecf05e47f8axbmu4mlwjlau8lkd7cf55wwq5qxxaoqhuim8j&ep=v1_gifs_search&rid=giphy.gif&ct=g']
            
            embed_trabalho = disnake.Embed(title='🛠️ **Ao trabalho**!', description=f'\n\nVocê trabalhou muito e \nAgora é hora de receber!', colour=disnake.Colour.from_rgb(128, 0, 255))
            embed_trabalho.set_author(name=inter.guild.name, icon_url=inter.guild.icon)
            
            embed_trabalho.add_field(name='\n\n💷 Dia de pagamento:', value=f'Você recebeu **{resultado[1]}** moedas', inline=True)
            embed_trabalho.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/1716/1716764.png')
            embed_trabalho.set_image(url=gifs[randint(0,len(gifs)-1)])

            await inter.send(embed=embed_trabalho)




def setup(bot:commands.Bot):
    bot.add_cog(Economia(bot))