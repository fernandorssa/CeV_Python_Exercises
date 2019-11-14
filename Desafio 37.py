n = int(input('Escreva um número inteiro: '))
lista = []

conv = int(input('Digite "1" para binário, "2" para octal ou "3" para hexadecimal: '))

if conv == 1:
    print('')
    print('Você escolheu binário')
    print('')
    print(bin(n)[2:])
    while n!= 0:
        x = n % 2
        lista.append(x)
        n//= 2
    print(lista[::-1])

elif conv == 2:
    print('')
    print('Você escolheu octal')
    print('')
    print(oct(n)[2:])
    while n!= 0:
        x = n % 8
        lista.append(x)
        n //= 8
    print(lista[::-1])

else:
    print('')
    print('Você escolheu hexadecimal')
    print('')
    print(hex(n)[2:])
