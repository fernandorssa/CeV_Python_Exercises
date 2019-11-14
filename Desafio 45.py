from random import choice

lista = ['pedra', 'papel', 'tesoura']
escolhaComputador = choice(lista)
escolhaJogador = str(input('Pedra, papel, ou tesoura? ')).lower()
print('')

if escolhaComputador == 'pedra' and escolhaJogador == 'pedra':
    print('O computador escolheu pedra. Empate!')
elif escolhaComputador == 'pedra' and escolhaJogador == 'papel':
    print('O computador escolheu pedra. Você venceu!')
elif escolhaComputador == 'pedra' and escolhaJogador == 'tesoura':
    print('O computador escolheu pedra. Você perdeu!')

elif escolhaComputador == 'papel' and escolhaJogador == 'pedra':
    print('O computador escolheu papel. Você perdeu!')
elif escolhaComputador == 'papel' and escolhaJogador == 'papel':
    print('O computador escolheu papel. Empate!')
elif escolhaComputador == 'papel' and escolhaJogador == 'tesoura':
    print('O computador escolheu papel. Você venceu!')

elif escolhaComputador == 'tesoura' and escolhaJogador == 'pedra':
    print('O computador escolheu tesoura. Você venceu!')
elif escolhaComputador == 'tesoura' and escolhaJogador == 'papel':
    print('O computador escolheu tesoura. Você perdeu!')
elif escolhaComputador == 'tesoura' and escolhaJogador == 'tesoura':
    print('O computador escolheu tesoura. Empate!')