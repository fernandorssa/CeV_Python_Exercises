saque = int(input('Qual o valor do saque: R$ '))

c50 = saque // 50
r50 = saque % 50
c20 = r50 // 20
r20 = r50 % 20
c10 = r20 // 10
r10 = r20 % 10
c1 = r10 // 1
r1 = r10 % 1

while True:
    if c50 > 0 and r50 == 0:
        break
    else:
        pass
    if c20 > 0 and r20 == 0:
        break
    else:
        pass
    if c10 > 0 and r10 == 0:
        break
    else:
        pass
    if c1 > 0 and r1 == 0:
        break
    else:
        pass

if c50 > 0:
    print(f'{c50} nota(s) de R$ 50 reais, sobrando R$ {r50} reais.')
if c20 > 0:
    print(f'{c20} nota(s) de R$ 20 reais, sobrando R$ {r20} reais')
if c10 > 0:
    print(f'{c10} nota(s) de R$ 10 reais, sobrando R$ {r10} reais')
if c1 > 0:
    print(f'{c1} nota(s) de R$ 1 real, sobrando R$ {r1} reais')

'''
# Minha solução, sem o while

saque = int(input('Qual o valor do saque: R$ '))

c50 = saque // 50
r50 = saque % 50
c20 = r50 // 20
r20 = r50 % 20
c10 = r20 // 10
r10 = r20 % 10
c1 = r10 // 1
r1 = r10 % 1

if c50 > 0:
    print(f'{c50} nota(s) de R$ 50 reais, sobrando R$ {r50} reais.')
if c20 > 0:
    print(f'{c20} nota(s) de R$ 20 reais, sobrando R$ {r20} reais')
if c10 > 0:
    print(f'{c10} nota(s) de R$ 10 reais, sobrando R$ {r10} reais')
if c1 > 0:
    print(f'{c1} nota(s) de R$ 1 real, sobrando R$ {r1} reais')

# Solução do Guanabara

print('=' * 30)
print('{:^30}'.formaat('Banco')
print('=' * 30)

valor = int(input())
total = valor
cedula = 50
totCedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totCedula += 1
    else:
        if totCedula > 0:
            print(f'Total de {totCedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totCedula = 0
        if total == 0:
            break
'''




