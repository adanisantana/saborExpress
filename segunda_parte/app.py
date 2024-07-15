from modelos.restaurante import Restaurante


restaurante_mexicano = Restaurante('Si señhora', 'Mexicana')
restaurante_comida_boa = Restaurante ('Comida Boa', 'Caseira')
restaurante_lanche_fast = Restaurante('Lanche Fast', 'Lanches')
restaurante_comida_boa = Restaurante('Comida Boa', 'Caseira')
restaurante_muy_delicia = Restaurante('Muy Delicia', 'Pizzaria')

restaurante_comida_boa.alternar_estado()
restaurante_mexicano.alternar_estado()

restaurante_comida_boa.receber_avaliacao('Lurdes', 10)
restaurante_comida_boa.receber_avaliacao("Juju", 5)
restaurante_muy_delicia.receber_avaliacao('Pri', 9)
restaurante_lanche_fast.receber_avaliacao('Emily', 3)

def main():
   Restaurante.listar_restaurante()

if __name__ == '__main__':
    main()