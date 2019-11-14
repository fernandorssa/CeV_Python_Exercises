import requests

try:
    r = requests.get('http://www.pudim.com.br/')
    print()
    print('O site do Pudim está funcionando normalmente...')
except:
    print()
    print('O site do Pudim não está acessível no momento!')


# Solução Guanabara

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site não está disponível...')
else:
    print('O site pudim está funcionando...')
    print(site.read())
