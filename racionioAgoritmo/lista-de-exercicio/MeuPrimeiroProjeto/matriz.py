m = [[ 1, 2, 3], #matriz com 3 colunas
     [ 4, 5, 6], #computação gráfica, objetos 3D
     [ 7, 8, 9]]
#como a matriz é bidimensional precisamos trabalhar com dois indices#linha / coluna

for linha in range (len(m)):
    for coluna in range (len(m[0])):
        if coluna > linha:
            print(m[linha][coluna],end='')
        else:
            print(0,end=' ')
        print('')




