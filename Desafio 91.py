from random import randint
from time import sleep

resultados = {'jogador1': randint(1, 6),
            'jogador2': randint(1, 6), 
            'jogador3': randint(1, 6), 
            'jogador4': randint(1, 6)
            }

print()
sleep(2)

for k,v in resultados.items():
    print(f'O {k} tirou {v}')

print()
sleep(2)

cont = 1

for item in sorted(resultados, key=resultados.get, reverse=True):
    print(f'{cont} lugar: jogador que tirou', resultados)
    cont += 1

# Solução do Guanabara

'''
from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1,6), 'jogador2': randint(1,6), 'jogador3': randint(1,6), 'jogador4': randint(1,6)}
print('Valores sorteados:')

ranking = dict()

for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # 0 ordena pro chave, 1 ordena por valor.

for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0] com v[1]}.')
    sleep(1)
'''