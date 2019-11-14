listaGeral = []
listaPar = []
listaImpar = []

while True:
    n = int(input('Digite um número: '))  # listaGeral.append(int(input('Digite: ')))
    listaGeral.append(n)
    continuar = int(input('Digite 1 para continuar e 2 para sair: '))
    if continuar == 2:
        break

for analise in listaGeral:
    if analise % 2 == 0:
        listaPar.append(analise)
    if analise % 2 == 1:
        listaImpar.append(analise)

'''
for i, v in enumerate(listaGeral):
    if v % 2 == 0:
    listaPar.append(v)
    elif v % 2 == 1:
    listaImpar.append(v)
'''

print('')
print(listaGeral)
print(listaPar)
print(listaImpar)
