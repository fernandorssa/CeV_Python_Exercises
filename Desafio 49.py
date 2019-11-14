n = int(input('Digite um número: '))
cont = 1

for c in range(10):
    print('{} x {} = {}'.format(n, cont, n * cont))
    cont += 1

# desnecessário o cont quando se tem o c!