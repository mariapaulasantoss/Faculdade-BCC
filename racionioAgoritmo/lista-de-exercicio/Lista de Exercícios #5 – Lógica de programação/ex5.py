'''Escreva um programa que popule uma matriz (15×7) de números inteiros sorteados dentro do
intervalo 10 a 99. Modifique então a matriz de forma que, caminhando da esquerda para a direita, de
cima para baixo, tenhamos primeiro todos os números pares, depois, os números impares. Mostre a
matriz antes e depois da modificação'''
from random import randint
matriz = []
for linha in range (15):
    linhaMatriz = []
    for coluna in range (7):
        linha= randint(10,99)
        linhaMatriz.append(linha)
    matriz.append(linhaMatriz)
print(10*' ','Matriz', ' '*10)
for linha in matriz:
    print(linha)
pares = []
impares = []
for linha in matriz:
    for valor in linha:
        if valor %2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)
todos = pares + impares
novaMatriz = []


for i in range(15):
    novalinha = todos [i*7:(i+1)*7]
    novaMatriz.append(novalinha)

print()
print(10*' ','Matriz 2 ', ' '*10)
for linha in novaMatriz:
    print(linha)