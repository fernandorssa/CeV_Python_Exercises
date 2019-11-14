mediaIdade = 0
maiorIdadeHomem = 0
menorIdadeMulher = []
for c in range(4):
    nome = str(input('Digite o seu nome: ')).strip()
    idade = int(input('Digite a sua idade: '))
    mediaIdade += idade
    sexo = int(input('Se você é homem, digite 1. Caso não seja, digite 2: '))
    if idade >= maiorIdadeHomem and sexo == 1:
        nomeHomemMaisVelho = nome
        maiorIdadeHomem = idade
    if idade < 21 and sexo == 2:
        menorIdadeMulher.append(nome)
print('')
print('Esta é a média de idade de grupo: {} anos'.format(mediaIdade/4))
print('')
if maiorIdadeHomem == 0:
    print('Não há homens nesse grupo.')
else:
    print('O nome do homem mais velho é {} e ele tem {} anos'.format(nomeHomemMaisVelho, maiorIdadeHomem))
print('')
if menorIdadeMulher == []:
    print('Não há mulheres com idade inferior a 21 anos nesse grupo.')
else:
    print('Há {} mulher(ers) com menos de 21 anos nesse grupo:'.format(len(menorIdadeMulher)))
    for x in menorIdadeMulher:
        print(x)
