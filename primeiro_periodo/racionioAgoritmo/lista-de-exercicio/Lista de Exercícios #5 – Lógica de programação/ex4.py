'''Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5×5)
com valores inteiros (dentro do intervalo 10 a 99). Para cada uma das figuras abaixo (elabore quatro
versões do programa): mostre a matriz original, mostre a matriz apenas com os valores que estão na
parte hachurada e mostre a soma destes valores:'''
from random import sample
m= []

for i in range (5):
    linha = sample (range (10,99),5)
    m.append(linha)
for linha in m:
    print(linha)

somaA = 0
for linha in range (len(m)):
    print()
    for coluna in range (len(m[0])):
        if (linha == 0 or linha == 4) or (coluna == 0 or coluna == 4):
            print(m[linha][coluna],end=' ')
            somaA += m[linha][coluna]
        else:
            print('  ',end=' ')
print(f'Soma = {somaA}')

print()
somaB = 0
for linha in range (len(m)):
    print()
    for coluna in range (len(m[0])):
        if coluna == 2 or linha ==2:
            print(m[linha][coluna],end=' ')
            somaB += m[linha][coluna]
        else:
            print('  ',end=' ')
print(f'Soma = {somaB}')
print()
somaC = 0
for linha in range (len(m)):
    print()
    for coluna in range (len(m[0])):
        if (linha  + coluna)%2 != 0:
            print(m[linha][coluna],end=' ')
            somaC += m[linha][coluna]
        else:
            print(' ',end=' ')
print(f'Soma = {somaC}')
print()
somaD = 0
for linha in range (len(m)):
    print()
    cont = 1
    for coluna in range (len(m[0])):
        if (linha == coluna +1) or (linha +1== coluna):
            print(m[linha][coluna],end=' ')
            somaD += m[linha][coluna]

        else:
            print(' ',end=' ')

print(f'Soma = {somaD}')



