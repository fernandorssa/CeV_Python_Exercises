tupla = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for i in tupla:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for a in range(len(i)):  # Aqui acho que pode ser "for a in i:"
        if i[a].lower() in 'aeiou':  # E aqui i.lower()
            print(i[a], end=' ')
