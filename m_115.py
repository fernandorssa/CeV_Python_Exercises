def menu():
    print('-' * 30)
    print(f'{"Menu principal":^30}')
    print('-' * 30)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova pessoa')
    print('3 - Sair do sistema')
    print('4 - Ver o menu principal')
    print('5 - Limpar cadastro')
    print('-' * 30)


def cadastro():

    dicionario = {}
    cont = 1

    while True:
        try:
            option = int(input('Sua opção: '))

            if option == 1:
                abertura = open('d_115.txt', 'r')
                print(abertura.read())

            elif option == 2:
                abertura = open('d_115.txt', 'a')
                nome = str(input('Digite o nome da pessoa: '))
                idade = int(input('Digite a idade da pessoa: '))
                dicionario[f'{cont}'] = nome, idade
                abertura.write(f'{nome}, {idade} anos\n')
                cont += 1

            elif option == 3:
                print('Volte sempre!')
                abertura.close()
                break

            elif option == 4:
                menu()

            elif option == 5:
                abertura = open('d_115.txt', 'w')

            else:
                print('Opção inválida!')

        except ValueError:
            print('É preciso digitar um número inteiro!')
