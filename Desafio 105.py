def notas(*resp, sit=False):
    """
    Vai receber vários valores numéricos e mostrar os resultados.
    """
    soma = 0
    for i in resp:
        soma += i
    media = soma / len(resp)
    
    if media < 7:
        situacao = 'Ruim'
    else:
        situacao = 'Boa'
    
    if sit:
        dicionario = {'Quantidade de notas': len(resp),
                      'Maior nota': max(resp),
                      'Menor nota': min(resp),
                      'Média da turma': media,
                      'Situação': situacao}
    
        return dicionario

    else:
        dicionario = {'Qtd. de notas': len(resp), 'Maior ': max(resp), 'Menor': min(resp), 'Média': media}
    
        return dicionario


resposta = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resposta)
# help(notas)
