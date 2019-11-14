n = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))

for c in range(10):
    resultado = n + razao
    print(n) # Se for a partir do n, ok. Se for a partir da primeira contagem, só trocar por print(resultado)
    n = resultado
print('Acabou =)')

'''
Nesse, o Guanabara complicou mais do que eu =D

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
décimo = primeiro + (10-1) * razao
for c in range (primeiro, décimo + razao, razao):
    print('{}'.format(c), end='--> '
print('Acabou')
'''
