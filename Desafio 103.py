def ficha(x, y):
    print(f'O jogador {x} fez {y} gol(s).')


jogador = input('Digite o nome do jogador: ').strip()
if jogador == '':
    jogador = 'Desconhecido'
gols = input('Quantos gols ele fez? ').strip()
if gols == '':
    gols = 0

ficha(jogador, gols)


# Solução do Guanabara

"""
def ficha(jog='Desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))  # Como string, para não dar erro ao deixar em branco
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
"""
