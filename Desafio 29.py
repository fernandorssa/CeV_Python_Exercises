v = float(input('Velocidade: '))

if v <= 80:
    print('Você está respeitando os limites de velocidade.')
else:
    print('Você passou no radar a {} km/h e excedeu o limite de velocidade.'.format(v))
    print('MULTADO no valor de R$ {:.2f}'.format((v-80)*7))
print('Tenha um bom dia! Dirija com segurança!')
