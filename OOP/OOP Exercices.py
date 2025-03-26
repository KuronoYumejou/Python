def class_musica():    
    class Musica:
            musicas = []

            def __init__(self, name, category, duration = int):
                self.name = name
                self.category = category
                self.duration = duration
                Musica.musicas.append(self)

            def __str__(self):
                return f'{self.name} | {self.category} | {self.duration}'
            
            def listar_musicas():
                for musica in Musica.musicas:
                    print(f'{musica.name} | {musica.category} | {musica.duration}')

    Musica.listar_musicas()
def class_carro():
     class Carro:
        def __init__(self, model, color, year):
            self.modelo = model
            self.cor = color
            self.ano = year
def class_restaurante():
    class Restaurante():
        restaurantes = []

        def __init__(self, nome, categoria):
            self.nome = nome
            self.categoria = categoria
            self.ativo = False
            Restaurante.restaurantes.append(self)
        
        def __str__(self):
            return f'{self.nome} | {self.categoria} | {self.ativo}'
        #prato_principal = ''
        #nota = int
    
    #Framboeza_louca = Restaurante() - Atribuindo Valores sem o __init__
    #Framboeza_louca.nome = 'Framboeza Louca'
    #Framboeza_louca.categoria = 'Deserts'
    #Framboeza_louca.prato_principal = "Bolo de Framboesa"
    #Framboeza_louca.nota = 9

    framboeza_louca = Restaurante('Framboeza Louca', 'Deserts')

    #print(vars(Framboeza_louca))
def cliente():
    class Cliente:
        def __init__(self, nome, pais, produto, registro = int):
            self.registro = registro
            self.nome = nome
            self.pais = pais
            self.produto = produto

    lang_shang = Cliente('Lang Shang', 'China', 'Ping-Pong Table', 1)
    iconico_margarette = Cliente ('Iconico Margarette', 'Cape Vert', 'Caldroun', 2)
    trash_ironmead = Cliente ('Trash Ironmead', 'England', 'Fart in a pot', 3)
    asuka_mikado = Cliente('Asuka Mikado', 'Japan', 'Frilly skirt', 4)
