'''Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.'''

n = int(input('Entre com um número inteiro: '))
cont = 1
soma = 0

for i in range(n):
    h = 1 / cont
    soma += h
    cont += 1

print('H vai ser igual a',  soma)