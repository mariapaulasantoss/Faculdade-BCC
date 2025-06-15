'''Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final). Os
valores inteiros de li e lf devem ser informados pelo usuário e não pertencem ao
intervalo, ou seja, intervalo aberto.'''

li = int(input("Digite o limite inicial (li): "))
lf = int(input("Digite o limite final (lf): "))

numero = li + 1

while li < numero < lf:
    resto = numero % 3
    if resto == 0:
        print(numero)
        numero += 3

    else:
        numero += 1

print('Fim!')


