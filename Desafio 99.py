def maior(*n):
    aux = None
    for i in range(len(n)):
        if i == 0:
            aux = n[i]
        else:
            if n[i] >= aux:
                aux = n[i]

    print(f'Foi/Foram informados {len(n)} valor(es)')
    print(f'O maior valor foi {aux}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)


# Guanabara

from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ', flush = True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()