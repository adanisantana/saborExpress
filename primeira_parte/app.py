import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo': False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana', 'ativo': True},
                {'nome':'O melhor da Índia', 'categoria':'Indiano', 'ativo':False},
                {'nome':'Mexidinho', 'categoria': 'Mineiro', 'ativo': True}]


def exibir_programa():

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulos_menu("Finalizar app")

def voltar_ao_menu():
    input("\nDigite uma tecla para voltar ao menu principal  ")
    main()

def opcao_invalida():
    print("Opção inválida! \n")
    voltar_ao_menu()

def exibir_subtitulos_menu(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print()
    print(linha)

def cadastrar_restaurante():
      '''Essa função é responsável por cadastrar um novo restaurante
      
      Inputs:
      - Nome do Restaurante 
      - Categoria

      Outputs:
      -Adiciona um restaurante na lista de restaurantes
      '''
      exibir_subtitulos_menu("Cadastro de Restaurantes")
      nome_restaurante = input("Digite o nome do restaurante: ")
      categoria = input(f"Digite a categoria do restaurante {nome_restaurante}:")
      dado_restaurante = {'nome':nome_restaurante, 'categoria': categoria, 'ativo': False}
      restaurantes.append(dado_restaurante)
      print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso\n")
      voltar_ao_menu()

def listar_restaurantes():
        ''' Essa função lista todos os restaurantes cadastrados
        Retorna:
        - Nome do Restaurante
        - Categoria
        - E o status do Restaurante (ativo/desativado)
        '''
        exibir_subtitulos_menu('Lista de Restaurantes')

        print(f"{'Nome do Restaurante'.ljust(22)}|  {'Categoria'.ljust(20)} |Status")

        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f' {nome_restaurante.ljust(20)} | {categoria.ljust(20)}  | {ativo}' )

        voltar_ao_menu()

def alterar_status_restaurante():
     '''Essa função altera o status do restaurante

     Retorno:
     - se o restaurante está ativo passa para o status desativado
     - se o restaurante está desativado para o status ativado
     
     '''
     exibir_subtitulos_menu('Alterar status do Restaurante')
     nome_restaurante = input('Digite o nome do Restaurante: ')
     restaurante_encontrado = False

     for restaurante in restaurantes:
          if nome_restaurante == restaurante['nome']:
               restaurante_encontrado = True
               restaurante['ativo'] = not restaurante['ativo']
               mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso 'if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
               print(mensagem)

               if not restaurante_encontrado:
                    print('O restaurante não foi encontrado')
    
     voltar_ao_menu()

def escolher_opcao():
    ''' Essa função é o menu de opções para o usuário escolher'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
                cadastrar_restaurante()
        elif opcao_escolhida == 2:
                listar_restaurantes()
        elif opcao_escolhida == 3:
                alterar_status_restaurante()
        elif opcao_escolhida == 4:
                finalizar_app()
        else:
             opcao_invalida()
    except:
          opcao_invalida()

def main():
    exibir_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__=='__main__':
    main()