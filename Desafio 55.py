for c in range(5):
    print('')
    peso = float(input('Digite o seu peso: '))
    if c == 0:
        menorPeso = peso  # O Guanabara definiu essa variável, e a próxima, antes do loop. Não precisava =)
        maiorPeso = peso
    else:
        if peso >= maiorPeso:
            maiorPeso = peso
        if peso <= menorPeso:
            menorPeso = peso

print('')
print('O maior peso é {}'.format(maiorPeso))
print('O menor peso é {}'.format(menorPeso))
