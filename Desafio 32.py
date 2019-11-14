'''
ano = int(input('Escreva o ano: '))

if ano % 400 == 0:
    print('É um ano bissexto!')
elif ano % 400 >= 100:
    print('Não é um ano bissexto!')
elif ano % 4 == 0:
    print('É um ano bissexto!')
else:
    print('Não é um ano bissexto!')
'''
from datetime import date
ano = int(input('Escreva o ano. Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO!'.format(ano))