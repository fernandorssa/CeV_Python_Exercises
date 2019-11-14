nome = str(input('Digite o nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou: '))

dict_final = {'Nome do jogador': nome, 'Quantidade de partidas': partidas}

soma = 0

for i in range(1, partidas+1):
    gols = int(input(f'Quantos gol na partida {i}: '))
    dict_final[f'Partida {i}'] = gols
    soma += gols

dict_final['Total de gols'] = soma
print()
for k,v in dict_final.items():
    print(f'{k}: {v}')


# Solução do Guanabara

"""
jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range(0, tot):
        partidas.append(int(input(f'Quantos gol na partida {c}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')

for i, v in enumerate(jogador['gols']):
        print(f'=> Na partida {i}, fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols.')
"""
