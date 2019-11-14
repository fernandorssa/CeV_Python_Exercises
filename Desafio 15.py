# R$ 60 / dia
# R$ 0.15 / km

dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos quilômetros rodados? '))

print('O total a pagar é de R$ {:.2f}'.format(dia * 60 + km * 0.15))