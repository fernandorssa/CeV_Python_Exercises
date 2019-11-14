import random
a01 = str(input('Nome do primeiro aluno: '))
a02 = str(input('Nome do segundo aluno: '))
a03 = str(input('Nome do terceiro aluno: '))
a04 = str(input('Nome do quarto aluno: '))
lista = [a01, a02, a03, a04]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista) # Eu tentei apagar a linha  7 e escrever na linha 9 o código print(random.shuffle(lista)), mas não deu certo; apareceu "none" no resultado
