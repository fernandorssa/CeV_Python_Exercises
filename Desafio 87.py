matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = maior = 0

for x in range(3):
    for y in range(3):
        matriz[x][y] = int(input(f'Digite um valor para [{x}, {y}]: '))

        if matriz[x][y] % 2 == 0:
            soma += matriz[x][y]

        if y == 2:                          # Guanabara fez:
            soma3 += matriz[x][y]           # for x in range(0, 3): soma3 += matriz[x][2]

        if x == 1:                     # Guanabara fez:
            if matriz[x][y] >= maior:  # for y in range(0, 3):
                maior = matriz[x][y]   # if y == 0: maior = matriz[1][y] elif matriz[1][y] > maior: maior = matriz[1][y]

print('=-' * 30)
for x in range(3):
    for y in range(3):
        print(f'[{matriz[x][y]:^5}]', end='')
    print()
print('=-' * 30)

print(f'A) {soma}')
print(f'B) {soma3}')
print(f'C) {maior}')

