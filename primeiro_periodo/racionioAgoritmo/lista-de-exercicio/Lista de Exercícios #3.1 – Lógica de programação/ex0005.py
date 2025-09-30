'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5 x 4
x 3 x 2 x 1 = 120'''

n = int(input('Entre com um número: '))
fatorial = 1

for i in range(1,n + 1):
    fatorial *= i    #fatorial = fatorial * i (próximo valor da lista)

print(fatorial)
