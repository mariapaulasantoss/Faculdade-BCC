'''Escreva um algoritmo que leia três números inteiros e mostre-os em ordem decrescente.'''
numero1= int(input('Entre com um número: '))
numero2= int(input('Entre com um número: '))
numero3= int(input('Entre com um número: '))


#Onde a variavel "número1" vai começar sendo o maior número:
if numero1 >= numero2 and numero2 >= numero3:
    print('A ordem descrescente será:', numero1, numero2, numero3)
elif numero1 >= numero3 and numero3 >= numero2:
    print('A ordem descrescente será:', numero1, numero3, numero2)

#Onde a variavel "número2" vai começar sendo o maior número:
elif numero2 >= numero1 and numero1 >= numero3:
    print('A ordem descrescente será:', numero2,numero1, numero3)
elif numero2 >= numero3 and numero3 >= numero1:
    print('A ordem descrescente será:', numero2, numero3, numero1)

#Onde a variavel "número3" vai começar sendo o maior número:
elif numero3 >= numero1 and numero1 >= numero2:
    print('A ordem descrescente será:', numero3, numero1, numero2)
else:
    print('A ordem descrescente será:', numero3, numero2, numero1)