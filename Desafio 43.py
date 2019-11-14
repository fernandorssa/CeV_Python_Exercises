peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)

print('')
print('O seu IMC é de {:.2f}'.format(imc))
print('')

if imc < 18.5:
    print('FERNANDA? BETA? Você está abaixo do peso. Quer uma paçoca?')
elif imc >= 18.5 and imc < 25:
    print('Seu peso é ideal. PARABÉNS')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('OBESIDADE!!!! VAI FAZER ACADEMIA, PORRA!!!!!')
else:
    print('OBESO MÓRBIDO, CARALHOOOOOOO!!!!!!!!!!!!!')

print('')
print('Tenha um bom dia =)')
print('')
