#------------------------------------ PRINTA ---------------------------------------
def printa(mat):
    for i in range(9):
        if i % 3 == 0:
            print("-------------------------------------")
        print("|", mat[i][:3], "|", mat[i][3:6], "|", mat[i][6:9], "|")
    print("-------------------------------------")


#------------------------------------ PRINTA ---------------------------------------
def printaprob(mat):
    for i in mat:
        for j in i:
            print(j, end='')
    print()

#--------------------- Converte o vetor de String para uma matriz de int ---------------------
def convertor(mat):
    matConvertida = []
    for i in range(9):
        linha = []
        for x in mat[i]:
            if x == '.':
                linha.append(0)
            else:
                linha.append(int(x))
        matConvertida.append(linha)
    return matConvertida

#------------------------------ Verifica se preencheu a matriz -------------------------------
def tembranco(mat):
    for i in mat:
        for j in i:
            if j == 0:
                return 1
    return 0

#--------------------------------- Verifição das regras ---------------------------------------
def verificacao(i, l, c, mat):
    if linha(l, i, mat) and coluna(c, i, mat) and minimatriz(l, c, i, mat):
        return 1
    return 0

#----------------------------------- Verificação da linha -------------------------------------
def linha(l, valor, mat):
    for i in range(9):
        if (mat[l][i] == valor):
            return 0
    return 1

#----------------------------------- Verificação da coluna -------------------------------------
def coluna(c, valor, mat):
    for i in range(9):
        if(mat[i][c] == valor):
            return 0
    return 1

#----------------------------------- Verificação da mat 3x3 -------------------------------------
def minimatriz(l, c, valor, mat):
    l = l//3 * 3
    c = c//3 * 3
    for i in range(l, l+3):
        for j in range(c, c+3):
            if valor == mat[i][j]:
                return 0
    return 1

