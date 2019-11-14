soma = 0
cont = 1

while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'A soma final dos {cont} valores é {soma}')

# Guanabara iniciou o "n" com a primeira linha: n = 0, em vez de um input
