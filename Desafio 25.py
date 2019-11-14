print('Método 3')
nome = str(input('Digite o seu nome completo: ')).lower().strip()
x = str('silva' in nome)
print('Seu nome tem "Silva"?')
print(x)


'''
MÉTODO 1
n = str(input('Digite o seu nome completo: '))
a = int(n.count('Silva'))

print('Vejamos...')

if a >= 1:
    print('Seu nome tem Silva')
else:
    print('Seu nome não tem Silva')

MÉTODO 2
n = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
'''
