'''Leia dois valores reais do teclado, calcular e imprimir na tela:
a) A soma destes valores b) O produto deles c) O quociente entre eles'''
lista= []
for i in range (1,3):
    n = float(input('Digite um número: '))
    lista.append(n)
print(f'A soma dos valores será:{lista[0]+ lista[1]}')
print(f'O produto dos valores será:{lista[0] * lista[1]}')
print(f'O quociente dos valores será:{lista[0] / lista[1]}')



