from model import *
from dao import *
from utils import *
# No controller fazemos o tratamento dos dados. E, se tudo estiver como deveria, jogamos para o Dao.O Dao se encarrega
# de inserir o dados no banco de dados, remove-los ou retorna-los. 
# Aqui não deve ter nenhum "print", so para proposito de testes. Ele no máximo pode retornar uma string.


class ControllerHospital:

    def adicionarhospital(self, nome_hospital, bairro, rua, numero_rua, telefone, tipo_hospital, numero_med, lotacao_max):
        #O objetivo do controller e apenas ser o Guarda. Ele que permite que uma execução no view va direto para o
        #Dao. Mas, ele mesmo não faz nenhuma verificação se as variaveis são legitimas. Quem faz e seu auxiliar, utils.py.
        verificar_duplicata = UtilsVerificador.verificadorExistenciaHospital(nome_hospital)
        verificar_nome = UtilsVerificador.verificarComprimentoString(nome_hospital)
        verificar_bairro = UtilsVerificador.verificarComprimentoString(bairro)
        verificar_rua = UtilsVerificador.verificarComprimentoString(rua)
        verificar_integerRua = UtilsVerificador.converterParaNumero(numero_rua)
        verificar_comprimento_nrua = UtilsVerificador.verificarNumeroRua(numero_rua)
        verificar_tel = UtilsVerificador.verificarTelefone(telefone)
        verificar_tipo = UtilsVerificador.verificadorTipo(tipo_hospital)
        verificar_integer_nmed = UtilsVerificador.converterParaNumero(numero_med)
        verificar_integer_lotmax= UtilsVerificador.converterParaNumero(lotacao_max)
      
        
        erros = [verificar_duplicata,verificar_nome,verificar_bairro,verificar_rua,verificar_integerRua,verificar_comprimento_nrua,verificar_tel,verificar_tipo,verificar_integer_nmed, verificar_integer_lotmax ]
        #Como não existe a possibilidade de imprimir o erros onde eles aconteceram, todos os erros retornados pelo utils.py
        #são colocados em uma lista
        erros = [erro for erro in erros if erro is not None]
        #Isso gera um problema, porque todas as variáveis que nâo deram erro recebem o valor "None". None sozinho seria igual "False"
        #Porém, varios Nones não geram um valor Falso na variável "erros" por ser uma lista. 
        # Pior, eles são um valor impresso quando iteramos uma lista. Logo, temos remové-los com um list compreheension
        # Que utiliza uma variável para verificar a lista os valores na lista e reinserir na lista o valores diferentes de "None".

        if not erros:
            #Se todos os valores forem None, todos serão removidos. Logo, a variável erros == False por estar vazia.
            DaoHospital.salvar(nome_hospital,bairro,rua,numero_rua,telefone,tipo_hospital,numero_med,lotacao_max)    
        else:
            #Mas, se houver algum erro na lista, ele joga para o script views.py iterar a lista e mostrar para o usuário
            #todos os erros
            return erros
                
       
    def removerhospital(self, nome_hospital):
        verificar_existencia = UtilsVerificador.verificadorExistenciaHospital(nome_hospital)

        if verificar_existencia:
            DaoHospital.apagar(nome_hospital)
            return True
        
    def mostrarhospistais(self):
        lista_de_hospitais = DaoHospital.ler()

        return lista_de_hospitais
       

