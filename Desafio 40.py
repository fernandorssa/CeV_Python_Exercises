
try:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
except:
    print('Formato de nota inválido!')

media = (n1+n2)/2

print('')
print('Sua média foi {}'.format(media))
print('')
if media < 5:
    print('Reprovado!')
elif media >= 7:
    print('Aprovado!')
else:
    print('Em recuperação!')