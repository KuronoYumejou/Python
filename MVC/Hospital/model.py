#No models so construimos nossas entidades, nenhuma operação e feita diretamente aqui. Assim como no banco de dados, o POO faz
#a modelagem de entidades. 
#Com alguns extras como coisas que essas entidades podem fazer como organizar, remover, inserir ou fazer
#ate coisas mais complexas como atacar, correr, perder vida, vender, comprar e etc.
#O que não faltam são exemplos. Já que, todos os tipos de variáveis são Classes com sua proprias funções (chamadas de metodos):
#Lista, Tupla, Dicionario, String são exemplos de classe. E esses são seus exemplos de metodos: .append(), .split(), .keys()
#.title()

class TipoHospital:
    #Podemos imaginar que todos nós somos uma instância da classe "Humano" e o self representa cada humano individualmente.
    #erick = Humano("Erick Luiz")
    #francisco = Humano("Francisco Sales")
    #erick.nome é igual a "Erick Luiz"
    #francisco.nome é igual a "Franscisco Sales". 
    #Nesses dois casos o self seria "erick" no primeiro caso e no segundo caso "francisco".
    #Ou seja, o self "representa" o nome da variável que se tornou uma instância de um objeto da classe "Humano".
    #Sem esse self, a classe não sabe de qual humano se trata e não temos como manipular suas caracteristicas se for
    #necessário.
    #Ele não precisa ser preenchido. Já que ele é a variável que se tornou a instância de uma classe.
    #
    #
    #O __init__ é iniciado automaticamente sempre que criamos um objeto de uma classe. Então, sempre que criamos um tipo
    #de hospital ele automaticamente recebe o tipo.
    def __init__(self,tipo):
        self.tipo = tipo
   
class Hospital:
    #é muito imporatante marcarmos os tipo de objeto que uma variável recebe para não esquecermos depois
    def __init__(self,nome_hospital, bairro, rua, numero_rua,telefone, tipo_hospital : TipoHospital, numero_med, lotacao_max):
        self.nome_hospital = nome_hospital
        self.bairro = bairro
        self.rua = rua
        self.numero_rua = numero_rua
        self.telefone = telefone
        self.tipo_hospital = tipo_hospital
        self.numero_med = numero_med
        self.lotacao_max = lotacao_max
