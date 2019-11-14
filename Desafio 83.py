''' Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
a expressão passada está com os parênteses abertos e fechados na ordem correta'''

cont = 0
expressao = str(input('Digite uma expressão matemática qualquer: '))
tudoJunto = expressao.replace(' ', '')
tudoJuntoV2 = expressao.split()

for analise in tudoJunto:
    cont += analise.count('(')
    cont += analise.count(')')

print('')
if cont % 2 == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está incorreta')

print('')
print(tudoJuntoV2)