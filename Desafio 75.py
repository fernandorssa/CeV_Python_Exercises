tupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite outro valor: ')),\
     int(input('Digite outro valor: ')))

if tupla.count(9) > 0:
    print(f'A) O número 9 apareceu {tupla.count(9)} vez(es)')
else:
    print('A) O número 9 não apareceu')
print('')

if 3 in tupla:
    print(f'B) O valor 3 apareceu na posição {tupla.index(3) + 1}')
else:
    print(f'B) O número 3 não apareceu')
print('')

print('C) Os valores pares são: ')
for i in range(4):
    if tupla[i] % 2 == 0:
        print(tupla[i])
