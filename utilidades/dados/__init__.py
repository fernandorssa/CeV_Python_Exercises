def aumentar(n, aumento):
    return n + (n * aumento / 100)


def diminuir(n, reducao):
    return n - (n * reducao / 100)


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(n, s=False):
    if s:
        if n == int:
            n = str(n)
            return f'R${n},00'
        else:
            x = f'{n:.2f}'
            x = str(x)
            x = x.replace('.', ',')
            return f'R${x}'
    else:
        return n


def resumo(n, soma, subt):
    var = [f'{"Preço analisado:":20}{moeda(n, True)}',
           f'{"Dobro do preço:":20}{moeda(dobro(n), True)}',
           f'{"Metade do preço:":20}{moeda(metade(n), True)}',
           f'{soma:<3}{"% de aumento:":17}{moeda(aumentar(n, soma), True)}',
           f'{subt:<3}{"% de redução:":17}{moeda(diminuir(n, subt), True)}']
    print('-' * 20)
    print(f'{"Resumo do valor":^20}')
    print('-' * 20)
    for i in var:
        print(i)
    print('-' * 20)


def leia_dinheiro(n):
    while n != float:
        try:
            var = input(n)
            if ',' in var:
                c = var.replace(',', '.')
                return float(c)
            else:
                return float(var)
        except:
            print('Digite um número válido...')
