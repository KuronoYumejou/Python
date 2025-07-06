#Todos os tratamento de erros são feitos aqui.
import sqlite3, re
bancodedados = 'db_hospitais.db'

class UtilsVerificador:
    @classmethod
    def verificarTelefone(cls,telefone):
        if len(telefone) >= 9 and len(telefone) <= 15: 
            padrao_telefone = re.compile(r'^\d{4}\-\d{4}$')
            padrao_telefone2 = re.compile(r'^\(\d{2}\)\d{4}\-\d{4}$')
            #Criamos os dois padrões de números possiveis
            verificador = bool(padrao_telefone.match(telefone))
            verificador2 = bool(padrao_telefone2.match(telefone))
            #Verificamos se o telefone recebido é igual a um dos padrões e tranformamos essa resposta em booleano
            if verificador == False and verificador2 == False:
                return 'Telefône no padrão incorreto!'
        else:
            return 'O telefône esta faltando números!'
    @classmethod
    def verificarComprimentoString(cls,alfanumerico):
       if len(alfanumerico) >= 50:
            return f'O valor inserido em nome, rua ou bairro é longo demais! Digite Nome, rua ou bairro com até 50 caracteres!'
    @classmethod
    def converterParaNumero(cls,alfanumerico):
        try: #Tenta converter o alfanumerico recebido em um int
            conversor = int(alfanumerico)
        except: #Se der errado, retorna um erro
            return f'O valor inserido em número de medicos ou lotação máxima não é um número!'
    @classmethod
    def verificarNumeroRua(cls,NumeroRua):
        if len(NumeroRua) >=5:
            return 'O Número da rua só pode ter no máximo 4 digitos!'          
    @classmethod
    def verificadorTipo(cls, tipo_hospital):
        conexao = sqlite3.connect(bancodedados)
        cursor = conexao.cursor() 
        cursor.execute('SELECT * FROM tipo_hospital WHERE tipo = (?)',(tipo_hospital,))
        lista_tipo = cursor.fetchall()
        conexao.close()
        if len(lista_tipo) == 0:
            return 'Esse tipo de hospital não existe!'  
    @classmethod
    def verificadorExistenciaHospital(cls,nome_hospital ):
        conexao = sqlite3.connect(bancodedados)
        cursor = conexao.cursor() 
        cursor.execute('SELECT * FROM hospital WHERE nome_hospital = (?)',(nome_hospital,))
        lista_hospitais = cursor.fetchall()
        conexao.close()
        if len(lista_hospitais) > 0:
            return 'Esse hospital já está registrado no sistema!'
 
        