"""
Aqui é um exemplo de como o desafio pode funcionar, que vale também para os desafios 108, 109 e 110. É possível ver
outros exemplos relacionados ao Desafio 111 na pasta "utilidades". No código do Guanabara foi colocado algo como:

from Desafios_Python.utilidades import valores

"Desafios_Python" é a pasta principal dos desafios, "utilidades" é o pacote, e "valores" é o pacote dentro do pacote.
Enquanto o Guanabara colocou as funções dentro do arquivo __init__.py da pasta "valores", chamando
"valores.nome_da_função", eu coloquei essas funções em arquivos individuais, nomeados como m__107, m__108,
m__109 e m__110, chamando por exemplo "m__107.nome_da_função"...
"""

from utilidades.valores import m__107

v = float(input('Digite um valor: R$ '))

print(f'Aumentando 10% temos R$ {m__107.aumentar(v):.2f}')
print(f'Diminuindo 13% temos R$ {m__107.diminuir(v):.2f}')
print(f'O dobro de R$ {v} é R$ {m__107.dobro(v):.2f}')
print(f'A metade de R$ {v} é R$ {m__107.metade(v):.2f}')
