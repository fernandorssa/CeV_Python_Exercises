cont = 1

while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    while cont <= 10:  # ou for c in range (1, 11)
        print(f'{n} * {cont} = {n * cont}')
        cont += 1
    cont = 1

print('')
print('Fim do programa')
