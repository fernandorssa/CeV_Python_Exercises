def pyhelp():
    aux = True
    while aux:
        print()
        print('\033[0;30;44mSistema de ajuda Pyhelp!\033[m')
        print()
        a = input('\033[0;30;44mFunção ou biblioteca\033[m: ').lower().strip()
        
        if a == 'fim':
            print()
            print('Até logo!')
            aux = False
        else:
            print(help(a))


pyhelp()
