import m_108

v = float(input('Digite um valor: R$ '))

print(f'Aumentando 10% temos {m_108.moeda(m_108.aumentar(v))}')
print(f'Diminuindo 13% temos {m_108.moeda(m_108.diminuir(v))}')
print(f'O dobro de {m_108.moeda(v)} é {m_108.moeda(m_108.dobro(v))}')
print(f'A metade de {m_108.moeda(v)} é {m_108.moeda(m_108.metade(v))}')

