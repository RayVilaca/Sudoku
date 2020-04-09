import funcoes as F


#--------------------------------- Preenche a matriz ----------------------------------------
def backtracking(l, c, mat):

    if c > 8:
        l += 1
    if l > 8:
        return
    c = c%9

    if mat[l][c] != 0:
        backtracking(l, c+1 ,mat)
        return
    else:
        for i in range(1, 10):
            flag =  F.verificacao(i, l, c, mat)
            if flag != 0:
                mat[l][c] = flag
                backtracking(l, c+1, mat)
        if F.tembranco(mat):
            mat[l][c] = 0
    return
#--------------------------------- MAIN ------------------------------------------------
matriz = []
for i in range(9):
    matriz.append(input())

matConvertida = F.convertor(matriz)
backtracking(0, 0, matConvertida)
F.printa(matConvertida)

if F.tembranco(matConvertida):
    print('A matriz não possui solução')
else:
    print('Resolução encontrada')
