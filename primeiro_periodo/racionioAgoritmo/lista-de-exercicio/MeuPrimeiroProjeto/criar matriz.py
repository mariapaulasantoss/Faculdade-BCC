#implementar um código Python que cria a matriz
m = []
nlinhas= int(input('Entre com a quantidade de linhas: '))
ncolunas = int(input('Entre com a quantidade de colunas: '))
#5x9
linha_matriz = []
for linha in range (nlinhas):
    linha_matriz = []
    for coluna in range (ncolunas):
        linha_matriz.append(1)
        m.append(linha_matriz)

for linha in range(nlinhas):
    print()
    for coluna in range(ncolunas):
            print(m[linha][coluna], end=' ')


