def leiaint(inteiro):
    while 1:
        try:
            return int(input(inteiro))
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados...')
            return 0
        except (ValueError, TypeError):
            print('Digite um número inteiro válido.')


def leiafloat(flutuante):
    while 1:
        try:
            return float(input(flutuante))
        except KeyboardInterrupt:
            print('O usuário preferiu não informar os dados...')
            return 0
        except (ValueError, TypeError):
            print('Digite um número real válido.')


n = leiaint('Digite um número inteiro: ')
y = leiafloat('Digite um número real: ')

print(f'Você acabou de digitar o número inteiro {n} e o número real {y}')
