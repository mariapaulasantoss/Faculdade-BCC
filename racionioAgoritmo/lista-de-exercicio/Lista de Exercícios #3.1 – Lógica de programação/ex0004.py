'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
elevado ao segundo número. Não utilize a função de potência da linguagem.'''
base = int(input('Entre com uma base '))
expoente = int(input('Entre com um expoente: '))
valor = 0

for i in range(expoente):
    mult = base * base
    valor = mult * base

print(f'O resultado da potenciação será {valor}')
