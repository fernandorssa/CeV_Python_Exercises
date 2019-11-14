from random import randint
from time import sleep

lista = []
jogos = []

print()
quantidade = int(input('Quantos jogos? '))
print()
total = 1

while total <= quantidade:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print(f'Sorteando {quantidade} jogo(s)...')
sleep(1)
print()

for p, v in enumerate(jogos):
    print(f'Jogo {p + 1}: {v}')
    sleep(1)
