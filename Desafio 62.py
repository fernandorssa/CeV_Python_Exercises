'''# Minha solução
n = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
cont = 1

while cont <= 10:
    resultado = n + razao
    print(n)
    n = resultado
    cont += 1
termos = int(input('Acabou? Digite 0 para sair ou digite um valor para continuar a PA: '))

while termos != 0:
    cont = 1
    while cont <= termos:
        resultado = n + razao
        print(n)
        n = resultado
        cont += 1
    termos = int(input('Acabou? Digite 0 para sair ou digite um valor para continuar a PA: '))

print('')
print('Programa encerrado')'''

# Guanabara
primeiro = int(input())
razao = int(input())
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input())
print('Programa encerrado com {} termos mostrados'.format(total))
