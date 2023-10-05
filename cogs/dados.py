import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='krigerpher22--',
    database='detroit'
)
cursor = conexao.cursor()


class Msql_dados():
    def __init__(self):
        pass
        
    def criar_user(self, id_discord):
        # Verificar se o id_discord já existe na tabela
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM users WHERE id_discord = '{id_discord}')")
        existe = cursor.fetchone()[0]

        cursor.execute("SELECT MAX(id) FROM users")
        ultimo_id = cursor.fetchone()[0]
        if ultimo_id is None:
            ultimo_id = 1
        else:
            ultimo_id = int(ultimo_id)
            ultimo_id += 1

        # Se não existir, inserir na tabela
        if not existe:
            bio = 'Olá, amigos(a) é um prazer está com vocês'
            cursor.execute(f"INSERT INTO detroit.users (id, id_discord, status, moedas, conjuge, bio, wallpaper, delay, gemas) VALUES ('{ultimo_id}', '{id_discord}', 'player', 0, 'solteiro(a)', '{bio}', 'sem', 0, 0)")
            conexao.commit()  # Não se esqueça de fazer commit das alterações
        elif existe:
            pass


    def dinheiro_quantidade(self, id_discord):
        cursor.execute(f"SELECT moedas FROM detroit.users WHERE id_discord = '{id_discord}'")
        moeda = cursor.fetchone()[0]

        return int(moeda)
    

    def dar_dinheiro(self, id_discord, valor):
        moeda = self.dinheiro_quantidade(id_discord)
        cursor.execute(f"UPDATE detroit.users SET moedas = '{moeda + valor}' WHERE id_discord = '{id_discord}'")
        conexao.commit()


    def remover_moedas(self, id_discord, valor):
        moeda = self.dinheiro_quantidade(id_discord)
        cursor.execute(f"UPDATE detroit.users SET moedas = '{moeda - valor}' WHERE id_discord = '{id_discord}'")
        conexao.commit()

    def setar_valor_dinheiro(self, id_discord, valor):
        cursor.execute(f"UPDATE detroit.users SET moedas = {valor} WHERE id_discord = '{id_discord}'")
        conexao.commit()


    def dar_dinheiro_daily(self, id_discord):

        cursor.execute(f"SELECT delay FROM detroit.users WHERE id_discord = '{id_discord}'")
        delay= cursor.fetchone()[0]
        
        if int(delay) == 0:
            moeda = self.dinheiro_quantidade(id_discord)

            valor_daily = moeda + 2000

            self.setar_valor_dinheiro(id_discord, valor_daily)

            cursor.execute(f"UPDATE detroit.users SET delay = 24 WHERE id_discord = '{id_discord}'")
            conexao.commit()

            return valor_daily
        else:
            return 'negado'
        


    def dar_dinheiro_trabalho(self, id_discord, sorte):
        from random import randint

        moeda = self.dinheiro_quantidade(id_discord)

        valor = randint(200, 1500)
        presente = randint(1500, 2500)
        trab = randint(10, 200)
        
        if sorte <= 3:
            self.setar_valor_dinheiro(id_discord, moeda - valor)
            
            return ('Você foi roubado', valor)
        elif sorte >= 98:
            self.setar_valor_dinheiro(id_discord, moeda + presente)

            return ('Você achou um presente', presente)
        else:
            self.setar_valor_dinheiro(id_discord, moeda + trab)

            return ('você trabalhou', trab)
        
