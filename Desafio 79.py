lista = list()

while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado com sucesso.')
    else:
        print('Duplicado. Número não adicionado.')
    continuar = str(input('Quer continuar (S/N)? ')).strip().upper()[0]
    if continuar == 'N':
        break

print('=-' * 30)

lista.sort()  # Para funcionar, é preciso primeiro digitar essa linha, e depois imprimir a lista
print(f'Você digitou os valores {lista}')

print(sorted(lista))  # Já esse comando faz tudo automaticamente
