## HackerHank - Nested Lists
## Paulo Henrique Teixeira de Oliveira - @paulohtoliveira

n = int(input())
name_lst = list()
score_lst = list()

i = 0
while (i < n):
    name = str(input())
    name_lst.append(name)
    score = float(input())
    score_lst.append(score)

    #encontrar o primeiro menor
    if len(score_lst) == 1:
        menor = score
    elif score < menor:
        menor = score
    i = i + 1;

## cocatena lista com zip() e transforma em lista de listas ##
listageral = [list(row) for row in zip(name_lst, score_lst)]
listageral.sort()

def busca_menor(elem):
    lmenor = []
    
    ## cria lista com menores valores compara com lista geral e deleta da lista geral##
    for i in listageral:
       if elem in i:
        lmenor.append(i[0:2])

    for i in lmenor:
        if i in listageral:
            listageral.remove(i)
    
    ## nova lista geral sem o menores ##
    x = 0;
    while( x < len(listageral)):
        if x == 0:
            novo_menor = listageral[x][1]
        elif listageral[x][1] < novo_menor:
            novo_menor = listageral[x][1]
        x = x + 1;

    for i in listageral:
       if novo_menor in i:
        print(i[0])

    return listageral

elem1 = menor
busca_menor(elem1)
