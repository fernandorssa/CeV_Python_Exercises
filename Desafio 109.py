from m_109 import moeda, metade, dobro, aumentar, diminuir

v = float(input('Digite um valor: R$ '))

print(f'A metade de {moeda(v, True)} é {moeda(metade(v), True)}')
print(f'O dobro de {moeda(v,True)} é {moeda(dobro(v), True)}')
print(f'Aumentando 10% temos {moeda(aumentar(v), True)}')
print(f'Diminuindo 13% temos {moeda(diminuir(v), True)}')

