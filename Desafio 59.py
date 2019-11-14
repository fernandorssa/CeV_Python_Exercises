n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

print('''
O que você deseja fazer?

[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
''')

x = int(input('Selecione uma das opções: '))

while x != 5:
    # Se colocar as opções aqui, elas sempre aparecerão no momento que o usuário for digitar uma nova opção
    if x == 1:  # Aqui, o Guanabara criou uma opção SOMA e depois dei um print do resultado
        x = int(input('O resultado é {}. Selecione outra opção: '.format(n1 + n2)))
    elif x == 2:
        x = int(input('O resultado é {}. Selecione outra opção: '.format(n1 * n2)))
    elif x == 3:
        if n1 > n2:
            x = int(input('{} é o maior. Selecione outra opção: '.format(n1)))
        elif n1 < n2:
            x = int(input('{} é  maior. Selecione outra opção: '.format(n2)))
        else:
            x = int(input('Iguais. Selecione outra opção: '))
    elif x == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        x = int(input('Selecione uma das opções: '))
    elif x > 5:
        x = int(input('Opção Inválida. Selecione outra opção: '))

print('')
print('Programa encerrado com sucesso')
