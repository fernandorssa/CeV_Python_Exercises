nome = input('Nome: ')
media = float(input(f'Média de {nome}: '))

dados = {'Nome': nome, 'Média': media}

if media >= 7:
    print('Nome é igual a {}'.format(dados['Nome']))
    print('Média é igual a {}'.format(dados['Média']))
    print('Situação é igual a APROVADO')
else:
    print('Nome é igual a {}'.format(dados['Nome']))
    print('Média é igual a {}'.format(dados['Média']))
    print('Situação é igual a REPROVADO')

# Solução do Guanabara:

"""
# aluno = dict()
# aluno['nome'] = str(input('Nome: '))
# aluno['media'] = float(input(f'Média de {alno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'

for k,v in aluno.items():
    print(f'{k} é igual a {v}')
"""