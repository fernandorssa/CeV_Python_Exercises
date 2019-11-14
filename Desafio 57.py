sexo = input('Digite o seu sexo (M/F): ').strip()

while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o seu sexo (M/F): ').strip()
print('ok')

'''
sexo = str(input('Informe o seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

'''