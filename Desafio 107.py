import m_107

v = float(input('Digite um valor: R$ '))

print(f'Aumentando 10% temos R$ {m_107.aumentar(v):.2f}')
print(f'Diminuindo 13% temos R$ {m_107.diminuir(v):.2f}')
print(f'O dobro de R$ {v} é R$ {m_107.dobro(v):.2f}')
print(f'A metade de R$ {v} é R$ {m_107.metade(v):.2f}')

"""
Na resolução do Guanabara o Desafio 107 e o Módulo m_107 foram colocados em
uma pasta. Dessa forma, o desafio poderia ser chamado da mesma forma, utilizando o
"import m_107". Também poderia utilizar "from m_107 import aumentar, diminuir,
etc". Possíveis avisos de erro na chamada dos módulos podem ser corrigidos
citando o nome da pasta criada, algo como:

import nome_da_pasta.m_107
from nome_da_pasta import m_106

Isso acabaria com o erro de referência. Outra solução foi criada no próprio
pycharm, onde as pastas que possuem módulos foram classificadas como pastas
raíz.
"""
