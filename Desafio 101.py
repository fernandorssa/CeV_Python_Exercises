# Minha solução

def voto1(x):
    if 2019 - x <= 16:
        print(f'Com {2019 - x} anos: Não vota.')
    elif 2019 - x >= 16 and 2019 - x < 65:
        print(f'Com {2019 - x} anos: Voto obrigatório.')
    else:
        print(f'Com {2019 - x} anos: Voto opcional.')

nascimento = int(input('Em que ano você nasceu? '))

voto1(nascimento)

# Solução do Guanabara

"""
def voto2(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional!'
    else:
        return f'Com {idade} anos: Voto obrigatório!'

nasc = int(input('Em que ano você naceu? '))
print(voto2(nasc))
"""
