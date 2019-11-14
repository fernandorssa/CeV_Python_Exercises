lista = []
lista_minimo = []
lista_maximo = []
cont = 0

while cont < 5:  # Ou for algo in range (0, 5), sem o cont
    n = int(input('Digite um número: '))  # lista.append(int(input('Digite um número: ')))
    lista.append(n)
    cont += 1

for c, v in enumerate(lista):  # O 'c' é a posição e o 'v' é o item da lista
    if v == min(lista):
        lista_minimo.append(c)
    if v == max(lista):
        lista_maximo.append(c)
print('')

if lista.count(min(lista)) == 1:
    print(f'O menor número é o {min(lista)}, que está na {lista.index(min(lista))}ª posição')
else:
    print(f'O menor número é o {min(lista)}, que aparece {lista.count(min(lista))} vezes, nas posições {lista_minimo}')

if lista.count(max(lista)) == 1:
    print(f'O maior número é o {max(lista)}, que está na {lista.index(max(lista))}ª posição')
else:
    print(f'O maior número é o {max(lista)}, que aparece {lista.count(max(lista))} vezes, nas posições {lista_maximo}')
print('')




