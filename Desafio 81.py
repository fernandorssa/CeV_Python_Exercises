lista = []
cont = 0
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    cont += 1
    continuar = int(input('Digite 1 para continuar e 2 para sair: '))
    if continuar == 2:
        break
listaInvertida = sorted(lista)

# lista.sort(reverse=True) --> Mais fácil...

print('')
print(f'O número de valores digitados foi {cont}')
print(listaInvertida[::-1])
if 5 in lista:
    if lista.count(5) > 1:
        print('O valor 5 foi digitado e está em mais de uma posição')
    else:
        print(f'O valor 5 foi digitado e está na posição {lista.index(5)} da lista')
else:
    print('O valor 5 não foi encontrado na lista original')

