'''Escreva um algoritmo que leia três números inteiros e mostre o valor do maior deles.'''
numero1= int(input('Entre com um número: '))
numero2= int(input('Entre com um número: '))
numero3= int(input('Entre com um número: '))

if numero1 >= numero2 and numero1 >= numero3:
    print('O maior valor será:', numero1)
elif numero2 >= numero1 and numero2 >= numero3:
    print('O maior valor será:', numero2)
else:
    print('O maior valor será:', numero3)