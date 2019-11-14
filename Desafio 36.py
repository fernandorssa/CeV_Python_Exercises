valorCasa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos pretende quitar a casa? '))
print('')

prestacoes = valorCasa/(anos*12)
porcentagem = (prestacoes * 100)/ salario

if porcentagem <= 30:
    print('Parabéns, seu financiamento foi aprovado!')
    print('Sua prestação será de R$ {:.2f} mensais'.format(prestacoes))
else:
    print('Sinto muito, mas seu financiamento não foi aprovado =(')
    print('Sua prestação seria de R$ {:.2f} mensais'.format(prestacoes))