n = int(input('Digite um número qualquer: '))
parada = int(input('Quer parar? (Sim = 1, Não = 2): '))
cont = 1
soma = n
maior = menor = n
continua = False

while not continua:
    while parada != 1:
        n = int(input('Digite outro número qualquer: '))
        cont += 1
        soma += n
        if n >= maior:
            maior = n
        if n <= menor:
            menor = n
        parada = int(input('Quer parar? (Sim = 1, Não = 2): '))

    print('')
    print('Parou')
    print('A média foi {}'.format(soma/cont))
    print('O menor número foi {}'.format(menor))
    print('O maior número foi {}'.format(maior))
    print('')
    nova_parada = int(input('Quer refazer o programa? (Sim = 1, Não = 2): '))
    if nova_parada == 2:
        continua = True # ou break
    else:
        parada = 2