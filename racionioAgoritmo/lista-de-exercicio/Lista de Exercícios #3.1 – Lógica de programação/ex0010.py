'''10. Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
No final, mostre a soma também.'''
n = int(input('Entre com um número inteiro: '))
denominador = 1
soma = 0
numerador = 1

for i in range(n):
    s = numerador / denominador

    soma += s
    denominador += 2
    numerador += 1


print(termos, soma)