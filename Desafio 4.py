n = input('Qual é o bebê mais lindo deste mundo: ')
print('O tipo primitivo é {}'.format(type(n)))
print(type(n))
print('O que foi digitado só tem espaços?', n.isspace())
print('O que foi digitado é Alfabético?', n.isalpha())
print('O que foi digitado é Numérico?', n.isnumeric())
print('O que foi digitado é Decimal?', n.isdecimal())
print('O que foi digitado pode ser impresso?', n.isprintable())
print('O que foi digitado é identificável? ', n.isidentifier())
print('O que foi digitado está somente em maiusculas? {}'.format(n.isupper()))

# Is.titled() é capitalizada, ou seja, começa com maiuscula.
