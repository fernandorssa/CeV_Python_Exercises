import random
from time import sleep
lista = [1, 2, 3, 4, 5]
n = random.choice(lista)
print('')
chute = int(input('Olá, eu pensei em um número de 1 a 5. Qual é o número? '))
print('PENSANDO...')
sleep(3)
if chute == n:
    print('PARABÉNS! Você acertou!')
else:
    if chute <= 5:
        print('ERROU! Eu pensei no número {}! Tente outra vez!'.format(n))
    else:
        print('NÚMERO DE 1 a 5!!!!!')

'''
from random import randint
computador = randint(0, 5) # Faz o computador "pensar"
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei?')) # jogador tenta adivinhar
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}!'.format(computador, jogador))

'''