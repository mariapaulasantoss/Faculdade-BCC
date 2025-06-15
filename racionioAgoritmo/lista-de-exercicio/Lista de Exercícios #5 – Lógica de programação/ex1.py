'''Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4×4), e
então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo
índice é o mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e
assim por diante. Mostre então a matriz, o vetor e a média aritmética do vetor.'''


m = []

for linha in range (4):  #construindo a matriz 4x4
    linha_matriz = []
    for coluna in range (4):
        num = int(input('Entre com os números da matriz: '))
        linha_matriz.append(num)
    m.append(linha_matriz)

mValorColuna = [] #Encontrando o maior número de cada coluna
for coluna in range (4):
    maior= m[0][coluna]  #Inicio o primeiro número como sendo o maior
    for linha in range (4):
        if m[linha][coluna] > maior: #Em seguida vou comparando
            maior = m[linha][coluna]
    mValorColuna.append (maior)

soma = 0
for i in mValorColuna:
    soma += i

print('MATRIZ')
for linha in m: #printar a matriz linha por linha
    print(linha)

print(f'O vetor com o maior número de cada coluna é: {mValorColuna} \nA média entre esses valores é {soma/4}')
