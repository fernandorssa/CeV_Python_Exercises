ano = int(input('Digite o ano de nascimento: '))
atual = 2018
n = atual - ano

print('Legal, você tem {} anos!'.format(n))

if n < 18:
    print('Ainda falta(m) {} ano(s) para o seu alistamento. Fique atento ao período de alistamento!'.format(18-n))
elif n == 18:
    print('Este é o ano no qual você deve se alistar!!!')
else:
    print('O prazo para alistamento ocorreu há {} ano(s)! Procure o serviço militar mais pŕoximo de sua residência e regularize sua situação!'.format(n-18))
