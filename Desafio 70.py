cont = soma = aux = 0

while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    valor = float(input('Digite o valor do produto: R$ '))

    if aux == 0:
        barato = valor
        nomeBarato = nome
        aux += 1
    soma += valor
    if valor > 1000:
        cont += 1
    if valor < barato:
        barato = valor
        nomeBarato = nome
    continuar = int(input('Quer continuar (Sim = 1, Não = 2): '))
    if continuar == 2:
        break

print('')
print(f'A) R$ {soma:.2f} foi o total gasto')
print(f'B) {cont} produto(s) custa(m) mais do que R$ 1.000,00')
print(f'C) {nomeBarato} é o produto mais barato')

