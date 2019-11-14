from valores import m__109

v = float(input('Digite um valor: R$ '))

print(f'A metade de {m__109.moeda(v, s=True)} é {m__109.moeda(m__109.metade(v), s=True)}')
print(f'O dobro de {m__109.moeda(v,s=True)} é {m__109.moeda(m__109.dobro(v), s=True)}')
print(f'Aumentando 10% temos {m__109.moeda(m__109.aumentar(v), s=True)}')
print(f'Diminuindo 13% temos {m__109.moeda(m__109.diminuir(v), s=True)}')
