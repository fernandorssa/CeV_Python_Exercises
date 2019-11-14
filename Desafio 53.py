print('')
frase = str(input('Digite uma frase qualquer: ')).lower()
lista = []
print('')

for c in frase:
    if c == ' ':
        pass
    else:
        lista.append(c)

print(lista)
print(lista[::-1])
print('')

if lista[:] == lista[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

