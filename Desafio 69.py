maiorDeIdade = homens = mulheres = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input(f'Digite o sexo (M/F): ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input(f'Digite o sexo (M/F): ')).strip().upper()[0]
    '''
    Guanabara:
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input(f'Digite o sexo (M/F): ')).strip().upper()[0]
    '''

    if idade >= 18:
        maiorDeIdade += 1
    if sexo == 'M':
        homens += 1
    if idade < 21 and sexo == 'F':
        mulheres += 1

    continuar = str(input('Quer continuar (S/N)? ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar (S/N)? ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'A) Há {maiorDeIdade} pessoa(s) com idade igual ou superior a 18 anos')
print(f'B) Há {homens} homens cadastrados')
print(f'C) Há {mulheres} mulher(es) com idade inferior a 20 anos')

