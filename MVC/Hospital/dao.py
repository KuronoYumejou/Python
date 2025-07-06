#O Dao só faz operações no banco de dados, nada mais. Todo o processo de tratamento e recebimento desses dados 
#fica nas mãos do utils.py e controller.py.

from model import *

import sqlite3
bancodedados = 'db_hospitais.db'

class DaoHospital():
    #O classmethod e quando uma classe não precisa de nenhuma instância para ser chamado. O "cls" e igual ao "self", mas
    #ele recebe a própria classe ao inves de uma instância do objeto. Ele também não precisa ser preenchido.
    @classmethod
    def salvar(cls, nome_hospital, bairro, rua, numero_rua, telefone, tipo_hospital, numero_med, lotacao_max):
        conexao = sqlite3.connect(bancodedados)
        #Para acessar um banco de dados, precisamos primeiro definir qual banco de de dados nos queremos nos conectar
        cursor = conexao.cursor() 
        # O cursor seria como um bibliotecário que faz operações no nosso banco de dados. Desde a adição de novos "livros"
        #até entregar esses "livros" ao usuário. 
        cursor.execute('''INSERT INTO hospital (nome_hospital,bairro, rua, numero_rua, telefone, tipo_hospital, numero_med,
                       lotacao_max) VALUES (?,?,?,?,?,?,?,?)''',(nome_hospital, bairro, rua, numero_rua, telefone, tipo_hospital, numero_med, lotacao_max,) )
        #Esses "?" são o dados que virão da nossa linguagem de programação para o nosso banco de dados. Que serão 
        #preenchidos com todas as variaveis dentro da tupla.
        #
        #A virgula no final precisa existir. Já que estamos usando uma tupla, não um metodo.

        conexao.commit() 
        #Todas as nossas operações no bando de dados vão direto para o "buffer" do banco de dados e, enquanto estiverem lá, podem
        #ser defeitas com um rollback(). Muito util para impedir que transações errôneas sejam defeitas.
        #Para lançar nossas alterações nos dados permanentes, precisamos usar o comando commit()
        conexao.close()
        #Se não fecharmos a conexão o usuário ficará conectado ao banco de dados enquanto não fechar o app. O que pode deixar as 
        #operações muito mais lentas.  Com close() garantimos que que se o banco de dados não estiver sendo usado, os usuários
        #não terão conexão alguma com ele enquanto usarem o aplicativo/site.
    @classmethod
    def apagar(cls, nome_hospital):
        conexao = sqlite3.connect(bancodedados)
        cursor = conexao.cursor() 
        cursor.execute('DELETE FROM hospital WHERE nome_hospital = (?)',(nome_hospital,))
        conexao.commit() 
        conexao.close()
    @classmethod
    def ler(cls):
        conexao = sqlite3.connect(bancodedados)
        cursor = conexao.cursor() 

        cursor.execute('SELECT * FROM hospital')
        cls.hospital = cursor.fetchall() 
        #O cursor pega todos os "livros" da sessao hospital e entrega um a um em forma de tupla
        conexao.close()
        hospit = [] #Criamos uma lista para guardar todos os nossos objetos do tipo "Hospital dentro dela"
        for i in cls.hospital:
            hospit.append(Hospital(i[0],i[1],i[2],i[3],i[4],TipoHospital(i[5]),i[6],i[7])) 
            #Pegamos os dados recebidos e usamos eles para criar um ou mais objetos do tipo "Hospital" que
            #requer 8 dados.
            #Não esquecendo que a criação de uma instância de Hospital tambem requer um "TipoHospital"
            #que precisamos de instanciar dento da nossa lista. 
        return hospit
class DaoTipoHospital():
    @classmethod
    def salvar(cls, tipo):
        conexao = sqlite3.connect(bancodedados)
        cursor = conexao.cursor() 
        cursor.execute('''CREATE TABLE IF NOT EXISTS Tipo_Hospital(tipo VARCHAR(50))''')
        cursor.execute('''INSERT INTO Tipo_Hospital(tipo) VALUES (?)''',(tipo,) )

        conexao.commit() 
        conexao.close()
    @classmethod
    def ler(cls):
        conexao = sqlite3.connect(bancodedados)
        cursor = conexao.cursor() 

        cursor.execute('SELECT * FROM Tipo_Hospital')
        cls.tipo = cursor.fetchall() 
        conexao.close()
        tipo_h = [] 
        for i in cls.tipo:
            tipo_h.append(TipoHospital(i)) 
        return tipo_h
    @classmethod
    def apagar(cls, tipo):
        conexao = sqlite3.connect(bancodedados)
        cursor = conexao.cursor() 
        cursor.execute('DELETE FROM Tipo_Hospital WHERE tipo = (?)',(tipo,))
        conexao.commit() 
        conexao.close()



