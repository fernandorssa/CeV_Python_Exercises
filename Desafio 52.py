n = int(input('Digite um número: '))
valor = True

for c in range(2, n):
    if n % c != 0:
        pass
    else:
        valor = False

print('\n')

if valor == True:
    print('É um número primo')
else:
    print('Não é um número primo')

'''
O Guanabara criou uma variável TOT = 0. Então ele dividiu o N por todos os números de 1 até o próprio N, e quando
a divisão ocorria (como por exemplo 6 % 3 == 0), ele aumentava o TOT em 1. Então, se o TOT não fosse igual a 2,
o número não poderia ser primo.
'''