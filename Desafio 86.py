# Minha solução

matriz = [[], [], []]

for x in range(3):
    for y in range(3):
        matriz[x].append(int(input('Digite: ')))

print('=-' * 30)
print(matriz[0][0], matriz[0][1], matriz[0][2])
print(matriz[1][0], matriz[1][1], matriz[1][2])
print(matriz[2][0], matriz[2][1], matriz[2][2])
print('=-' * 30)

# Solução do Guanabara

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for x in range(3):
    for y in range(3):
        matriz[x][y] = int(input(f'Digite um valor para [{x}, {y}]: '))

print('=-' * 30)
for x in range(3):
    for y in range(3):
        print(f'[{matriz[x][y]:^5}]', end='')
    print()