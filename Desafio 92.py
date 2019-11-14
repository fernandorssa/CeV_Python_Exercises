nome = str(input('Digite o seu nome: '))
ano = int(input('Digite o ano de nascimento: '))
ctps = int(input('Digite o número da carteira de trabalho: '))

if ctps != 0:
    contrato = int(input('Digite o ano de contrato: '))
    salario = float(input('Digite o salário: R$ '))
    dados = {'Nome': nome,
             'Idade': 2019 - ano,
             'CTPS': ctps,
             'Ano de contrato': contrato,
             'Salário: R$': salario,
             'Aposentadoria': contrato + 35}
else:
    dados = {'Nome': nome,
             'Idade': 2019 - ano,
             'CTPS': 'Não possui cadastro CTPS ativo'}

for k,v in dados.items():
    print(k,v)

# Solução do Guanabara

"""
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}') # Idade
"""
