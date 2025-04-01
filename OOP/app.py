from OOP.Restaurante import Restaurante

Pizzaria_Pepino = Restaurante('Pizzaria Pepino', 'Italian')
Sonic_Lanches = Restaurante('Sonic Lanches', 'Fast Food')
YugiYoyo_Chines = Restaurante ('Yugi Yoyo', 'Chinese')

restaurantes = {Pizzaria_Pepino, Sonic_Lanches, YugiYoyo_Chines}

Restaurante.change_status(Sonic_Lanches)
Restaurante.listar_restaurantes()


def main():
    pass

if __name__ == '__main__':
    main()