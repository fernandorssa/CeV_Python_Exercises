import random
from time import sleep
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = random.choice(lista)  # Guanabara usa o randint (0, 10), em vez de uma lista. É mais simples, but...
tentativas = 1
print('')
chute = int(input('Olá, eu pensei em um número de 1 a 10. Qual é o número? '))
print('PENSANDO...')
sleep(2)


while chute != n:
    if chute <= 10:
        if chute < n:
            chute = int(input('ERROU! Eu pensei em um número maior! Tente outra vez!: '.format(n)))
            print('PENSANDO...')
            sleep(2)
            tentativas += 1
        else:
            chute = int(input('ERROU! Eu pensei em um número menor! Tente outra vez!: '.format(n)))
            print('PENSANDO...')
            sleep(2)
            tentativas += 1
    else:
        chute = int(input('NÚMERO DE 1 a 5!!!!!. Digite outro número, entre 1 e 10!!!: '))
        print('PENSANDO...')
        sleep(2)
        tentativas += 1

if tentativas == 0:
    print('PARABÉNS! Você acertou de primeira!')
elif 0 < tentativas < 5:
    print('Você acertou depois de {} tentativa(s)...'.format(tentativas))
else:
    print('Demorou mas veio! Depois de {} tentativas, você conseguiu!'.format(tentativas))