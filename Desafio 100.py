from random import randrange


def sorteia():
    n1 = randrange(1, 11)
    n2 = randrange(1, 11)
    n3 = randrange(1, 11)
    n4 = randrange(1, 11)
    n5 = randrange(1, 11)

    numeros = [n1, n2, n3, n4, n5]

    print(numeros)

    return somapar(*numeros)


def somapar(*numeros):
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i

    print(soma)


sorteia()