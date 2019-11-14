valor = float(input('Digite o valor do produto: R$ '))
print('')
print('0 - pagamento em dinheiro')
print('1 - Débito')
print('2 - Em até 2 vezes no cartão de crédito')
print('3 - Em 3 vezes ou mais no cartão de crédito')
print('')

pagamento = int(input('Selecione a forma de pagamento: '))

if pagamento == 0:
    valorFinal = (valor * 90) / 100
    print('O valor final é de R$ {:.2f}'.format(valorFinal))

elif pagamento == 1:
    valorFinal = (valor * 95) / 100
    print('O valor final é de R$ {:.2f}'.format(valorFinal))

elif pagamento == 2:
    valorFinal = valor
    print('O valor final é de R$ {:.2f}'.format(valorFinal))
else:
    valorFinal = (valor * 120) / 100
    print('O valor final é de R$ {:.2f}'.format(valorFinal))