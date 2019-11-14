cont = 1

for c in range(51): # (2, 51, 2) --> Menos Loop...
    if cont % 2 == 0:
        print(cont)
        cont += 1
    else:
        cont += 1

# eu poderia ter usado o c no lugar do cont...