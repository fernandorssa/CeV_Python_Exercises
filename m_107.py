def aumentar(n):
    return n + (n * 10 / 100)


def diminuir(n):
    return n - (n * 13 / 100)


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(n):
    if n == int:
        n = str(n)
        return f'R$ {n},00'
    else:
        x = f'{n:.2f}'
        x = str(x)
        x = x.replace('.', ',')
        return f'R$ {x}'

""" Na resolução, o Guanabara incluiu outro parâmetro nas funções aumentar
e diminuir : a taxa. Dessa forma, no lugar do 13 e do 10, seria calculado o
aumento com base na taxa."""
