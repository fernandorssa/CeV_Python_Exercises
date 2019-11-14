n = str(input('Digite uma frase qualquer: ')).lower().strip()
print('Existe(m) {} letra(s) A em sua frase'.format(n.count('a')))
print('O primeiro "A" aparece no caractere {}'.format(n.find('a') + 1))
print('O último "A" aparece no caractere {}'.format(n.rfind('a') + 1))

# Esse rfind foi novidade, pois ele não falou no curso