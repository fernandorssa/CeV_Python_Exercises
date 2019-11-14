n = int(input('Digite um número qualquer: '))
soma = n
cont = 1

while n != 999:
    n = int(input('Digite outro número qualquer: '))
    if n != 999:
        soma += n
    cont += 1


print(soma)
print(cont)