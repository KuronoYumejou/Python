class Restaurante:
    restaurantes = []
    #__Init__ 
    # 
    # Is a constructor method. When a Restaurant Object is instanced, the constructor is
    # Automatic called, expecting the variables that are inside the parenthesis.
    # 
    # self
    #  
    # Since a Class is associated with multiples instances, Self is used to differentiate that instances
    # But, "self" don't need to be added as a variable of any object (Since "Self" IS the object)

    def __init__(self, nome, categoria): 

        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

#__str__ is a special method that shows variables of the object in text format
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes :
          print (f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')
    
# Pizzaria_Pepino = Restaurante()
# Pizzaria_Pepino.nome = 'Pizzaria Pepino'
# Pizzaria_Pepino.categoria = 'Italiana'
# Sonic_Lanches = Restaurante()
Pizzaria_Pepino = Restaurante('Pizzaria Pepino', 'Italiana')
Sonic_Lanches = Restaurante('Sonic Lanches', 'Fast Food')
YugiYoyo_Chines = Restaurante ('Yugi Yoyo', 'Chinesa')

restaurantes = {Pizzaria_Pepino, Sonic_Lanches, YugiYoyo_Chines}

Restaurante.listar_restaurantes()

#print(restaurantes) / print(Pizzaria_Pepino)  
#
# This shows the place where the object and it's variables are stored in the computer memory.
# Unless we want a lot of ramdom symbols and numbers, it's not that useful...
# HOWEVER, if we are using __str__ print(Pizzaria_Pepino) will work as we REALLY want
#
#print(dir(Pizzaria_Pepino)) 
#
# Shows all attributes, methods and properties of this object
#
#print(var(Pizzaria_Pepino)) 
#
# Shows a dictionary of properties and methods of this object. But, don't shows variables that
# are received by the class of this object like "ativo" in this case. But, If the object comes from a 
# constructor, all variables will be printed on the screen.
#print(Pizzaria_Pepino.ativo)
#
# If we want to see an specific variable, that works well  