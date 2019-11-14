from time import sleep

print('')
print('Vai começar a contagem regressiva!!!!!')
print('')
sleep(1)
cont = 10
for tempo in range(10, -1, -1):
    if cont == 0:
        print('0!!!!!!!!!!!!!!    AEEEEEEEEEE!!!!!!!!!!! BUUUUUUUM TCHAMMMMMMMMMMMM CATAPUMMMMMMM!!!!!')
    else:
        print(cont)
        cont -= 1
        sleep(1)

# Para fazer a contagem, eu poderia ter usado somente a variável tempo, e não o cont -=1. Isso porque essa variável
# diminiu a cada passo do range. Aí também não precisaria do cont == 0, colocando o AEEE fora do range...