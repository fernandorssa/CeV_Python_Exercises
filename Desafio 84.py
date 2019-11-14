lista = list()
total = list()
leve = list()
nomeLeve = list()
pesado = list()
nomePesado = list()

while True:
    lista.append(str(input('Digite o nome: ')))
    lista.append(float(input('Digite o peso: ')))
    total.append(lista[:])
    lista.clear()
    continuar = str(input('Quer continuar(S/N)? ')).strip().upper()[0]
    if continuar in 'Nn':
        break

print()
print(f'foram cadastradas {len(total)} pessoas')

print()
for p, v in enumerate(total):
    if p == 0:
        print(f'{v[0]} tem {v[1]} kg')
        nomePesado.append(v[0])
        nomeLeve.append(v[0])
        pesado.append(v[1])
        leve.append(v[1])
    else:
        print(f'{v[0]} tem {v[1]} kg')
        if v[1] > pesado[-1]:
            pesado.clear()
            pesado.append(v[1])
            nomePesado.clear()
            nomePesado.append(v[0])
        elif v[1] == pesado[-1]:
            pesado.append(v[1])
            nomePesado.append(v[0])
        elif v[1] < leve[-1]:
            leve.clear()
            leve.append(v[1])
            nomeLeve.clear()
            nomeLeve.append(v[0])
        else:
            if v[1] == leve[-1]:
                leve.append(v[1])
                nomeLeve.append(v[0])

print('')
print(f'O mais pesado do grupo é o {nomePesado}, com {pesado} kg')
print(f'O mais leve do grupo é o {nomeLeve}, com {leve} kg')

