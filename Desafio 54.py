from datetime import date

cont = 1
maiores = []
menores = []
dataAtual = date.today().year

for c in range(7):
    n = int(input('Digite o ano de nascimento da pessoa {}: '.format(cont)))
    if (dataAtual - n) >= 21:
        maiores.append(cont)
    else:
        menores.append(cont)
    cont += 1

print('')
if len(maiores) == 1:
    print('Somente 1 pessoa atingiu a maioridade')
else:
    if len(maiores) > 1:
        print('{} pessoas já atingiram a maioridade'.format(len(maiores)))

if len(menores) == 1:
    print('Somente 1 pessoa é menor de idade neste grupo')
else:
    if len(menores) > 1:
        print('{} pessoas ainda não atingiram a maioridade'.format(len(menores)))

# Na solução do Guanabara, em vez de listas, ele usou uma variável como totalMaiores, então foi somando quando a pessoa
# tinha idade maior do que 21. Bem mais simples.

