#Cuida da parte Visual do Programa
from controller import *
import os
#O View só tem acesso ao controller e ele retorna para o view se as operações do backend deram certo ou não.



#Sempre importante criarmos TODOS os nossos bancos de dados na VIEW. Já que esse script é o contato do usuario com o programa
def criarbancodedados():
    conexao = sqlite3.connect(bancodedados)
    cursor = conexao.cursor() 
    cursor.execute('''CREATE TABLE IF NOT EXISTS Tipo_Hospital(tipo VARCHAR(50) NOT NULL PRIMARY KEY)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS hospital(nome_hospital VARCHAR(50) NOT NULL PRIMARY KEY, bairro VARCHAR(50) NOT NULL, rua VACHAR(50) NOT NULL,
                       numero_rua VARCHAR(4) NOT NULL, telefone VARCHAR(15) NOT NULL, tipo_hospital VARCHAR(30) NOT NULL, numero_med INT NOT NULL, lotacao_max INT NOT NULL,
                       FOREIGN KEY (tipo_hospital) REFERENCES Tipo_Hospital(tipo))
                       ''')
    
    conexao.commit()
    conexao.close()

#Esse script não pode ser chamado por nenhum outros script.Já que ele é nossa tela inicial.
#Para garantir isso, podemos usar if __name__ == '__main__'. Sempre que executamos um script, ele recebe o nome de __main___
#pelo Python. Se ele for importado por outro script, logo o nome dele não será '__main__', tornando a condição falsa e impedindo
#a execução.
if __name__ == '__main__':
    criarbancodedados()
    hosp = ControllerHospital()
    while True:
        os.system('cls')
        resposta = input('''
▒█▀▄▀█ ▒█▀▀▀ ▒█▀▀▄ ▀█▀ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀▀█ 　 ▒█▀▀▀█ ▒█▀▀▀ ▒█▀▄▀█ 　 ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█▀▀▀ ▀█▀ ▒█▀▀█ ░█▀▀█ ▒█▀▀▀█ 
▒█▒█▒█ ▒█▀▀▀ ▒█░▒█ ▒█░ ▒█░░░ ▒█░░▒█ ░▀▀▀▄▄ 　 ░▀▀▀▄▄ ▒█▀▀▀ ▒█▒█▒█ 　 ▒█▀▀▄ ▒█▄▄█ ▒█▄▄▀ ▒█▄▄▀ ▒█▀▀▀ ▒█░ ▒█▄▄▀ ▒█▄▄█ ░▀▀▀▄▄ 
▒█░░▒█ ▒█▄▄▄ ▒█▄▄▀ ▄█▄ ▒█▄▄█ ▒█▄▄▄█ ▒█▄▄▄█ 　 ▒█▄▄▄█ ▒█▄▄▄ ▒█░░▒█ 　 ▒█▄▄█ ▒█░▒█ ▒█░▒█ ▒█░▒█ ▒█▄▄▄ ▄█▄ ▒█░▒█ ▒█░▒█ ▒█▄▄▄█
                         

                         
                         Bem vindo ao Médicos Sem Barreiras! O que você deseja? 
                         

                         1 - Adicionar um Hospital
                         2 - Remover um Hospital
                         3 - Ver Hospitais Parceiros\n''')
        if resposta == '1':
            os.system('cls')
            print('Obrigado por contribuir com nosso programa! Por favor, preencha os dados do hospital:\n ')
            nome = input('Nome do hospital: ')
            bairro = input('Bairro em que esta localizado: ')
            rua = input('Rua do Hospital: ')
            numero = input('Número da rua do hospital: ')
            telefone = input('Telefone do Hospital: ')
            tipo = input('Tipo do Hospital: ')
            numero_medicos = input('Número de médicos: ')
            lotacao_maxima = input('Lotação Máxima: ')
            resultado = hosp.adicionarhospital(nome,bairro,rua,numero,telefone,tipo,numero_medicos,lotacao_maxima)
            if resultado:
                print('Não foi possivel adicionar o hospital pelas seguintes razões: ')
                for i in resultado:
                    input(f'-{i}')
            else:
                input(f'Hospital {nome} criado com sucesso!')
            
        if resposta == '2':
            os.system('cls')
            print('Que pena...')
            nome = input('Qual Hospital você deseja desassociar do programa? ')
            resultado = hosp.removerhospital(nome)
            if resultado:
                input('Hospistal removido do nosso programa!')
            else:
                input('Nenhum hospital com esse nome foi encontrado!')
        if resposta == '3':
            os.system('cls')
            print('Esses são os nossos hospitais parceiros: ')
            lista_de_hospitais = hosp.mostrarhospistais()
            for i in lista_de_hospitais:
            #Aqui nós recebemos varios objetos do tipo hospital. Se apenas dermos print,o programa nós entregara apenas o endereço
            #de memória dos objetos. Precisamos chamar o objeto com suas variaveis definitas no __init__. 
            #Uma coisa muito importante: Se um objeto recebe outro objeto, precisamos da variável onde o objeto foi armazenado
            #na classe principal e a variável do objeto recebido que queremos que ele mostre. 
            #Ou ele tambem sera retornado como um endereço de memória.
            #Podemos definir como os objetos são impressos na model usando o def __str___ na classe. Não sei se isso normalmente é usado.
            #Mas, aqui está o metodo "normal" para chamar algo legivel do objeto.
                print(f'\nNome do hospital:{i.nome_hospital}\nEndereço:{i.rua},{i.bairro},{i.numero_rua}\nTelefone:{i.telefone}\nTipo:{i.tipo_hospital.tipo}\nNumero de Medicos:{i.numero_med}\nLotaçao Maxima:{i.lotacao_max}\n')
            input('')
