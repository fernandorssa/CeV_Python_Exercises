print('')
print('')
print('Olá, bem vindo à Fernandense, a maior empresa de transporte coletivo intermunicipal do Estado')
print('')
n = float(input('Por favor, nos informe a distância entre o ponto de partida e o ponto de chegada: '))

if n <= 200:
    print('Valor a pagar: R$ {:.2f}'.format(n*0.50))
else:
    print('Valor a pagar: R$ {:.2f}'.format(n*0.45))

'''
valor = n * 0.50 if n <= 200 else n * 0.45
print(valor)
'''