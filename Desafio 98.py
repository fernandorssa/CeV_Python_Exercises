from time import sleep


def contador():

    # Contagem de 1 até 10
    for i in range(1, 11):
        if i == 10:
            print(i, end=' ')
            sleep(0.5)
            print('FIM!')
        else:
            print(i, end=' ')
            sleep(0.5)
    print()

    # Contagem de 10 até 0
    for f in range(10, -2, -2):
        if f == 0:
            print(f, end=' ')
            sleep(0.5)
            print('FIM!')
        else:
            print(f, end=' ')
            sleep(0.5)

    # Contagem personalizada
    print('Agora é a sua vez de personalizar a contagem!')
    inicio = int(input('Digite o início: '))
    fim = int(input('Digite o fim: '))
    passo = int(input('Digite o passo: '))
    
    if fim < inicio:
        if passo == 0:
            passo = 1
            if passo > 0:
                for p in range(inicio, fim - passo, -passo):
                    print(p, end=' ')
            else:
                for p in range(inicio, fim + passo, passo):
                    print(p, end=' ')
        else:
            if passo > 0:
                for p in range(inicio, fim - passo, -passo):
                    print(p, end=' ')
            else:
                for p in range(inicio, fim + passo, passo):
                    print(p, end=' ')
    else:
        if passo == 0:
            passo = 1
            for p in range(inicio, fim, passo):
                print(p, end=' ')
        else:
            for p in range(inicio, fim, passo):
                print(p, end=' ')
    print('FIM!')
        

contador()
