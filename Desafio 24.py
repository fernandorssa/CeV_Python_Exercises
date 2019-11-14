from time import sleep
n = str(input('Digite o nome de sua natal: ')).strip()
a = int(n.capitalize().find('Santo'))
cont = 0

while cont <= 5:
    sleep(1)
    print(cont)
    cont += 1

if a == 0:
    print('Sua cidade tem "Santo" no nome')
else:
    print('Sua cidade não tem "Santo" no nome')

'''
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')
'''