lista = []
cont = 1

anterior = int(input('Digite um número 1: '))
print('Adicionado na posição 0')
lista.append(anterior)

while cont < 5:
    if cont == 1:
        proximo = int(input('Digite o número 2: '))
        if proximo <= anterior:
            lista.insert(0, proximo)
            print('Adicionado na posição 0')
        else:
            lista.append(proximo)
            print('Adicionado na posição 1')
        anterior = proximo
    if cont == 2:
        proximo = int(input('Digite o número 3: '))
        if proximo <= lista[0] <= lista[1]:
            lista.insert(0, proximo)
            print('Adicionado na posição 0')
        elif lista[0] <= proximo <= lista[1]:
            lista.insert(1, proximo)
            print('Adicionado na posição 1')
        else:
            lista.append(proximo)
            print('Adicionado na posição 2')
    if cont == 3:
        proximo = int(input('Digite o número 4: '))
        if proximo <= lista[0] <= lista[1] <= lista[2]:
            lista.insert(0, proximo)
            print('Adicionado na posição 0')
        elif lista[0] <= proximo <= lista[1] <= lista[2]:
            lista.insert(1, proximo)
            print('Adicionado na posição 1')
        elif lista[0] <= lista[1] <= proximo <= lista[2]:
            lista.insert(2, proximo)
            print('Adicionado na posição 2')
        else:
            lista.append(proximo)
            print('Adicionado na posição 3')
    if cont == 4:
        proximo = int(input('Digite o número 5: '))
        if proximo <= lista[0] <= lista[1] <= lista[2] <= lista[3]:
            lista.insert(0, proximo)
            print('Adicionado na posição 0')
        elif lista[0] <= proximo <= lista[1] <= lista[2] <= lista[3]:
            lista.insert(1, proximo)
            print('Adicionado na posição 1')
        elif lista[0] <= lista[1] <= proximo <= lista[2] <= lista[3]:
            lista.insert(2, proximo)
            print('Adicionado na posição 2')
        elif lista[0] <= lista[1] <= lista[2] <= proximo <= lista[3]:
            lista.insert(3, proximo)
            print('Adicionado na posição 3')
        else:
            lista.append(proximo)
            print('Adicionado na posição 4')
    cont += 1

print('')
print(lista)