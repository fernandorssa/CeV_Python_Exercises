
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 > (r3 - r2) and r1 < (r3 + r2):
    if r2 > (r3 - r1) and r2 < (r3 + r1):
        if r3 > (r2 - r1) and r3 < (r2 + r1):
            print('É um triângulo')
        else:
            print('Não é um triângulo')
    else:
        print('Não é um triângulo')
else:
    print('Não é um triângulo')

# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: # Isso porque o cálculo é cada lado tem que ser menor do que a soma dos outros 2
# print('É triângulo')
# else:
# print('Não é um triângulo')



