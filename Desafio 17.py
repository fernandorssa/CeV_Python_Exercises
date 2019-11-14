from math import sqrt
a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
calc1 = pow(a, 2) # ou a ** 2
calc2 = pow(b, 2) # ou b ** 2
# A fórmula é h² = a² + b²
print('O valor da hipotenusa é {}'.format(sqrt(calc1+calc2)))

'''
hip = (a ** 2 + b ** 2) ** (1/2) # é uma das maneiras de fazer
hip = math.hypot(a, b) # bem mais simples
'''