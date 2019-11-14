n = int(input('Quantas pessoas: '))

dict = {}
acima_da_media = {}
mulheres = []
cont = soma = 0

for i in range(n):
    nome = str(input('Digite um nome: '))
    sexo = str(input('Digite o sexo (m/f): '))
    idade = int(input('Digite a idade: '))
    if sexo == 'f':
        mulheres.append(nome)    
    soma += idade
    dict[f'Nome da pessoa {cont + 1}'] = nome
    dict[f'Sexo da pessoa {cont + 1}'] = sexo
    dict[f'Idade da pessoa {cont + 1}'] = idade
    acima_da_media[f'{nome}'] = idade
    cont += 1
media = soma / cont

print(f'A: foram cadastradas {cont} pessoa(s)')
print(f'B: A média de idade é {media} anos')
print(f'C: Lista de mulheres: {mulheres}')

print('D: Lista de pessoas com idade acima da média:')
for k,v in acima_da_media.items():    
    if int(v) > media:
        print(f'{k}, com {v} anos')


# Solução do Guanabara
"""
galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo(M/F): ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar (S/N)? ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responsa apenas S ou N.')

    if resp == 'N':
        break


print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end=',')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}')
        print()
print('ENCERRADO')
"""
