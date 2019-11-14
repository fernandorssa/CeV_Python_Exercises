from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
ordenados = sorted(tupla)

print('')
print(f'A tupla gerada foi = {tupla}')
print(f'menor = {ordenados[0]}')
print(f'maior = {ordenados[-1]}')

# Guanabara
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')
