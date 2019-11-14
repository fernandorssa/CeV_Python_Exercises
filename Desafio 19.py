from random import choice # Pode ser import random ou pode ser from random import choice (nesse caso, lá embaixo só utiliza choice (lista)
a01 = str(input('Nome do primeiro aluno: '))
a02 = str(input('Nome do segundo aluno: '))
a03 = str(input('Nome do terceiro aluno: '))
a04 = str(input('Nome do quarto aluno: '))
lista = [a01, a02, a03, a04]
escolhido = choice(lista)
print('O nome do(a) aluno(a) escolhido(a) foi {}'.format(escolhido))