lista = list()
while True:
    nome = str(input("Nome: "))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append([[nome], [nota1, nota2]])
    # alunos = [[str(input('Nome: '))], [float(input('Nota: ')), float(input('Nota: '))]]
    # lista.append(alunos)
    continuar = str(input('Quer continuar(S/N)? ')).strip().upper()[0]
    if continuar in 'Nn':
        break

print(f'{"Nome":^10}{"Número":^10}{"Média":^10}')
for p, v in enumerate(lista):
    print('{:^10}'.format(p), v[0], (v[1][0] + v[1][1]) / 2)
    # Qual o motivo de eu não poder usar f string do v[0] em diante?

n = int(input('Mostrar notas de qual aluno (999 para sair)? '))

while n != 999:
    for p, v in enumerate(lista):
        if n == p:
            print(v[0], v[1][0], v[1][1])
    n = int(input('Mostrar notas de qual aluno(999 para sair)? '))
