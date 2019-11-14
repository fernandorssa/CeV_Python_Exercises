s = float(input('Qual é o seu salário atual: '))

if s > 1250:
    s = (s*110) / 100 # ou s + (s * 10 / 100)
    print('Seu novo salário será de R$ {:.2f}'.format(s))
else:
    s = (s*115 / 100) # ou s + (s * 15 / 100)
    print('Seu novo salário será de R$ {:.2f}'.format(s))