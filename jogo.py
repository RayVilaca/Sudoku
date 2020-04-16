import funcoes as F


#--------------------------------- Preenche a matriz ----------------------------------------
def backtracking(linha, c, mat, ordem):

    if c > 8:
        linha += 1
        c = 0

    if linha > 8:
        return

    l = ordem[linha][1]

    if mat[l][c] != 0:
        backtracking(linha, c+1 ,mat, ordem)
    else:
        for i in range(1, 10):
            flag =  i * F.verificacao(i, l, c, mat)
            if flag != 0:
                mat[l][c] = flag
                backtracking(linha, c+1, mat, ordem)
        if F.tembranco(mat):
            mat[l][c] = 0
    return
#--------------------------------- MAIN ------------------------------------------------

n = int(input())

for i in range(n):
    matriz = []
    aux = input()
    ordem = []

    for i in range(9):
        matriz.append(aux[9 * i: 9 * (i+1)])
        ordem.append((9 - matriz[i].count('.'), i))

    ordem = sorted(ordem, reverse=True)

    matConvertida = F.convertor(matriz)
    backtracking(0, 0, matConvertida, ordem)

    F.printa(matConvertida)
    F.printaprob(matConvertida)

    if F.tembranco(matConvertida):
        print('A matriz não possui solução')
    else:
        print('Resolução encontrada')
