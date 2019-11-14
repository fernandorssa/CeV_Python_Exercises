def fatorial(n, show=False):
    """
    Função que calcula o fatorial de um número.
    Caso queira ver o cálculo completo, insira o parâmetro show=True
    """
    cont = n - 1
    resultado = 1
    lista = [n]
    
    while cont >= 1:
        lista.append(cont)
        resultado = n * cont
        n = resultado
        cont -= 1
        
    lista.append(resultado)
    
    if show:
        print('-' * 20)
        for i in lista:
            if i != resultado:
                if i != 1:
                    print(i, end=' * ')
                else:
                    print(i, end=' = ')
            else:
                print(i)
    else:
        print('-' * 20)
        print(resultado)


fatorial(10, show=True)
# help(fatorial)
