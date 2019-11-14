n = int(input('Digite sua idade: '))

if n <= 9:
    print('MIRIM')
elif n >= 10 and n <= 14:
    print('INFANTIL')
elif n >= 15 and n <= 19:
    print('JÚNIOR')
elif n == 20:
    print('SÊNIOR')
else:
    print('MASTER')