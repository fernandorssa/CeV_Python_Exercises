from time import sleep
print('')
n = str(input('Digite o seu nome completo: ')).strip()
s = n.split()
print('Olá!')
sleep(2)
print('Seu primeiro nome é {}'.format(s[0]))
print(s)
print('Seu último nome é {}'.format(s[len(s)-1]))
print('Seu nome é composto por {} palavras'.format(len(s)))
