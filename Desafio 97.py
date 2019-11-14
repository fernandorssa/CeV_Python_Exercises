def escreva():
    texto = str(input('Digite um texto qualquer: '))
    print('~' * len(texto))
    print(texto)
    print('~' * len(texto))


escreva()


# Guanabara
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
