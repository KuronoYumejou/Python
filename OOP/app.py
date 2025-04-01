from OOP.Restaurante import Restaurante

Pizzaria_Pepino = Restaurante('Pizzaria Pepino', 'Italian')
Sonic_Lanches = Restaurante('Sonic Lanches', 'Fast Food')
YugiYoyo_Chines = Restaurante ('Yugi Yoyo', 'Chinese')

restaurantes = {Pizzaria_Pepino, Sonic_Lanches, YugiYoyo_Chines}

Restaurante.change_status(Sonic_Lanches)
Restaurante.receive_rating('Rocketman', 8.0)
Restaurante.receive_rating('Pizza Guy', 5.5)



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()