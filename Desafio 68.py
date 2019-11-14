import random
'''
Guanabara usou:
jogo = ''
while jogo not in 'PI':
    jogo = str(input('Par ou Ímpar (P/I): ')).strip().upper()[0]
'''
cont = 0
while True:
    # Eu estava iniciando a variável computador fora do loop. Então, não importava quantas vezes eu jogasse, o resultado
    # do computador seria sempre o mesmo.
    computador = random.randint(0, 10)
    jogador = int(input('Quantos dedos você vai mostrar? '))
    jogo = str(input('PAR OU IMPAR? ')).strip().upper()
    total = computador + jogador
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if total % 2 == 0 and jogo == 'PAR':
        print('Jogador venceu!')
        cont += 1
    elif total % 2 != 0 and jogo == 'PAR':
        print('Jogador perdeu!')
        break
    elif total % 2 == 0 and jogo == 'IMPAR':
        print('Jogador perdeu!')
        break
    elif total % 2 != 0 and jogo == 'IMPAR':
        print('Você venceu!')
        cont += 1
print('')
print(f'Você conseguiu vencer {cont} partida(s) consecutiva(s)...')
# Conforme a correção do exercício, uma forma mais fácil
'''
if jogo == 'PAR':
    Isso evita o if total % 2 == 0 and jogo == 'PAR'
elif jogo == 'IMPAR':
'''
