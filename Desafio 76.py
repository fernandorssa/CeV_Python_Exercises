tupla = ('Queijo', 15, 'Cerveja', 10, 'Whisky', 100, 'Caneta', 2, 'Sorvete', 10, 'Mochila', 59, 'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for i in range(14):
    if i % 2 == 0:
        print(f'{tupla[i]:.<30}', end='')
    else:
        print(f'R$ {tupla[i]:>7.2f}')
print('-' * 40)
