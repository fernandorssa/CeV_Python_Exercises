'''# Pede quantos termos da sequência Fibonacci
n = int(input('Digite quantos termos da sequência: '))
# O contador foi definido como 4 pois n0, n1 e n2 não entram no WHILE. Dessa forma, o programa roda 3 vezes a menos
cont = 4
n1 = n2 = 1

# Se o usuário pede 5 termos, o cont vai rodar 2 vezes, somado ao n0, n1 e n2: totalizando os 5 termos
while cont <= n:
    # Essas quatro linhas são usadas para imprimir os 3 primeiros números da sequência
    if n1 == 1 and n2 == 1:
        print(n1 - n2)
        print(n1)
        print(n2)
    # Daqui em diante são calculados os próximos termos da sequência, depois de 0, 1, 1...
    resultado = n1 + n2
    # Aqui será impresso o próximo termo da sequência Fibonacci
    print(resultado)
    n2 = n1
    n1 = resultado
    cont += 1'''

# Meu programa funciona mas a lógica é complicada
n = int(input('Quantos termos: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')

