'''Elabore um programa que preencha uma matriz quadrada (4x4) denúmeros inteiros, sorteados dentro
do intervalo 100 a 999, garantindo que não haverá nenhuma repetição (os 16 números devem ser
únicos). Encontre então o valor do menor elemento da linha em que se encontra o maior elemento da
matriz. Mostre a matriz e os dois valores encontrados'''
from random import sample
m = []
maior = 0
for i in range (4):
    linhaMatriz = sample (range(100,999),4)
    m.append(linhaMatriz)
maior = [0][0]
posicao = 0
for linha in range (4):
    for coluna in range (4):
        if m[linha][coluna] > maior:
            maior = m[linha][coluna]
            posicao = linha
menor = min(m[posicao])


print('*-*-*-*-*MATRIZ*-*-*-*-*')
for linha in m:
    print(linha)
print(f'O maior elemento da matriz é: {maior}')
print(f'O menor valor da linha do maior é: {menor}')