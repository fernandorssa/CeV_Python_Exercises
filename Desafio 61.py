n = int(input('Digite um número: '))
razao = int(input('Digite a razão da PA: '))
cont = 1

while cont <= 10:
    resultado = n + razao
    print(n)
    n = resultado
    cont += 1
print('Acabou =)')