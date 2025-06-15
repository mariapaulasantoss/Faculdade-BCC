'''Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada (informe
“Valor inválido” para números negativos).'''
numero = int(input('Entre com um número: '))

if numero < 0:
  print('Valor inválido')

else:
  raizQuadrada = numero ** 0.5
  print('A raiz quadrada é: ', raizQuadrada)