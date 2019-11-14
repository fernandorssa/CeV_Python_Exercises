print('''Crie um programa que leia o nome completo de uma pessoa e mostre:
1)o nome com todas as letras maisculas
2) o nome com todas minúsculas
3) Quantas letras no total (sem considerar os espaços)
4) Quantas letras tem o primeiro nome''')

nome = str(input('Digite seu nome completo: ')).strip()

print('1) {}'.format(nome.upper()))
print('2) {}'.format(nome.lower()))
print('3) {}'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
p1 = len(dividido[0])
print('4) {}'.format(p1))
print('4) {}'.format(nome.find(' ')))   # Neste caso, ele vai dizer qual é o caractere aparece o
                                        # primeiro espaço que coincidentemente é o número de letras
