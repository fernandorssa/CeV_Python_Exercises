# Minha solução

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
print('')

if r1 > (r3 - r2) and r1 < (r3 + r2):
    if r2 > (r3 - r1) and r2 < (r3 + r1):
        if r3 > (r2 - r1) and r3 < (r2 + r1):
            if r1 == r2 and r1 == r3:
                print('Triângulo equilátero')
            elif r1 != r2 and r1 != r3 and r2 != r1 and r2 != r3 and r3 != r1 and r3 != r2:
                print('Triângulo escaleno')
            else:
                print('Triângulo isósceles')

        else:
            print('Não é um triângulo')
    else:
        print('Não é um triângulo')
else:
    print('Não é um triângulo')

# Solução do Guanabara

