#Elabore um algoritmo que leia um número inteiro e verifique se ele é par ou ímpar
numero = int(input('Entre com um número: '))
resto = numero % 2
if resto > 0:
    print('Número impar')
else:
    print('Número par')