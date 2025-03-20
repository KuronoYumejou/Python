import os

def exercicio1():
    print("Python na escola de programaçao Alura")
    nome = "Chasseur"
    idade = 17
    print (f"Meu nome e {nome} e minha idade e {idade}")
    print(''' 
    A
    L
    U
    R
    A
    ''')
def exercicio2():
    numero = int(input("Digite um numero: "))
    
    if numero % 2 == 0 :
        print(f'O numero {numero} e par')
    else:
        print(f'O numero {numero} e impar')
def exercicio3():

    idade = int(input("Digite sua idade: "))
    if idade <= 12:
        print('criança')
    if idade <=18 and idade >=13  :
        print ('Adolescente')
    if idade > 18:
        print ('Adulto')
def exercicio4():
   Cx= int(input('Qual e a sua posiçao em X? '))
   Cy= int(input('Qual e a sua posiçao em Y? '))

   if Cx > 0 and Cy > 0:
       print('Voce esta no Quadrante 1')
   elif Cx < 0 and Cy >0:
       print('Voce esta no Quadrante 2')
   elif Cx < 0 and Cy <0:
       print('Voce esta no Quadrante 3')
   elif Cx > 0 and Cy <0:
       print('Voce esta no Quadrante 4')
   else:
       print('Voce esta na Origem')
def exercicio5():
    numero = [1,2,3,4,5,6,7,8,9,10]

 
       
    def impares():
        soma = 0

        for numeros in numero:
            if numeros%2 != 0:
             soma += numeros
        print(f"A soma dos numeros impares e : {soma} ")       
    def tabuada():
        for numeros in numero:
            
            for i in range(1,11):
                a = numeros

                a *= i

                soma = a

                print (f"A multiplicacao de {numeros} x {i} e: {soma}")

                soma = 0
    def somadelementos():
        soma = 0
        for numeros in numero:
            soma += numeros
    def ordemreversa():

        numero.reverse()

        for numeros in numero:

          print (f'{numeros}')

    print('''
            1 - Soma de Numero Impares
            2 - Tabuada
            3 - Soma dos Elementos

            ''')
                

    opcao = int(input("Selecione uma opçao : "))

    if opcao == 1:
                        impares()
    elif opcao == 2:
                        tabuada()
    elif opcao == 3:
                        somadelementos()
    elif opcao == 4:
                        ordemreversa()
def exercicio6():
 pessoas = [{'nome':'Vagabundol', 'idade': 48, 'cidade': 'Kenjivania'}, 
                 {'nome': 'Todney Rodney', 'idade': 26, 'cidade': 'Zeth'},
                 {'nome': 'Souless', 'idade': 32, 'cidade': 'Helman'}]
        
 def adicionarinfo ():
        
        nome_pessoa = input('Adicionar informaçao a qual pessoa? ')

        for pessoa in pessoas:
          if nome_pessoa == pessoa['nome']:
             pessoa.update({'profissao': 'coveiro'})
             idade_pessoa = pessoa['idade']
             cidade_pessoa = pessoa['cidade']
             profissao_pessoa = pessoa['profissao']

             print(f'{nome_pessoa}|{idade_pessoa}|{cidade_pessoa}|{profissao_pessoa}')
          else:
             print('Nao tem ninguem com esse nome aqui...')   
 def mudarinfo():
       nome_pessoa = input('mudar a idade de qual pessoa? ')   

       for pessoa in pessoas:
        
            if nome_pessoa == pessoa['nome']:
                pessoa.update({'idade': 12})
                idade_pessoa = pessoa['idade']
                print(f"{idade_pessoa}")     
            else:
                print('Nao tem ninguem com esse nome aqui...')   
 def checarchave():
      nome_chave = input("Qual a chave que voce esta procurando? ")  
      vezes = 0

      for pessoa in pessoas:
        if nome_chave in pessoa.keys():
            vezes += 1
           

      print(f'A chave aparece {vezes} vezes') 
      
      
   
      
      
 selecionar_opcao = int(input('Selecione um serviço: '))

 if selecionar_opcao == 1:
      adicionarinfo()
 elif selecionar_opcao == 2:
      mudarinfo()
 elif selecionar_opcao == 3:
      checarchave()
def exercicio7():
     dicionario = {}
     frase = input("Escreva sua frase favorita: ")
     palavras = frase.split()

     dicionario = palavras

     chave = input("Qual palavra voce quer procurar? ")

     if chave in dicionario:
        print('Essa chave existe!')
     else:
          print('Non Existe!')



        

                
            
       

                

        

def main():
    os.system('cls')
    exercicio7()

if __name__ == '__main__':
    main()

