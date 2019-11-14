times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético', 'Atlético - PR', 'Cruzeiro',
         'Botafogo', 'Santos', 'Bahia', 'Corinthians', 'Ceará', 'Fluminense', 'Vasco', 'Chapecoense', 'América',
         'Sport', 'Vitória', 'Paraná')
print('')

print('Classificação dos 5 primeiros colocados:')                       # Guanabara fez times[0:5]
for a in range(0, 5):
    print(f'{a + 1}°', f'{times[a]}')
print('')

print('Classificação dos 4 últimos colocados:')                         # Guanabara fez times[-4:]
for b in range(16, 20):
    print(f'{b + 1}°', f'{times[b]}')
print('')

print('Lista dos times em ordem alfabética:')
ordenados = sorted(times)
for c in range(0, 20):
    print(f'{c + 1}°', f'{ordenados[c]}')
print('')

chapeco = times.index('Chapecoense')
print(f'C) O Chapecoense está na {chapeco + 1}ª posição')