# O Guanabara fez de forma bem mais simples, aproveitando a variavel "c", enquanto eu criei a variável "cont" para fazer
# a mesma coisa. Além disso, ele eliminiu o "cont%2" fazendo a range (1, 501, 3), que pegou só os números ímpares

cont = 1
s = 0

for c in range(500):
    if cont % 2 == 1:
        if cont % 3 == 0:
            print(cont)
            s += cont
            cont += 1
        else:
            cont += 1
    else:
        cont += 1

print('A soma final é {}'.format(s))