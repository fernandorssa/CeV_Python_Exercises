n = int(input('Digite um número para o while: '))
multiplicador = n - 1
while multiplicador >= 1:
    n = n * multiplicador
    multiplicador -= 1

m = int(input('Digite um número para o for: '))
for a in range(1, m):
    m = m * a

print(n, m)

'''
# SOLUÇÃO 1
from math import factorial
n = int(input())
f = factorial(n)
print(f)

# SOLUÇÃO 2
n = int(input('Digite um número: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
'''
