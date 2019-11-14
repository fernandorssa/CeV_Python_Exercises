def area():
    largura = float(input('Digite a largura (m): '))
    comprimento = float(input('Digite o comprimento (m): '))
    area_retangular = largura * comprimento
    print(f'A área de {largura} por {comprimento} é de {area_retangular} m²')


area()


# Guanabara
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} é {a}m²')


print('Controle de terrenos')
print('-' * 20)
larg = float(input('Largura: '))
comp = float(input('Comprimento: '))
area(larg, comp)
