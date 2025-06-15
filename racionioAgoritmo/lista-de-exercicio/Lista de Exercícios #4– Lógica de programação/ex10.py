'''Escreva um programa que leia um vetor de números inteiros de 10 posições,
aceitando apenas valores positivos. Modifique então o vetor de forma que,
tenhamos primeiro todos os números pares, depois, os números impares. Mostre
o vetor antes de depois da modificação'''

num = []
par = []
impar = []
lista = 0
for i in range (1,11):
    n = int(input('Entre com um número: '))
    num.append(n)
for i in num:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
    lista = par + impar
print(f' Os valores de entrada foram:{num}')
print(f'A lista em ordem de primeiro os pares e depois os impares: {lista}')
