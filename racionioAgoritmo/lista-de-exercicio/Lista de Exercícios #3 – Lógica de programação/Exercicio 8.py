'''Elabore um algoritmo que leia um conjunto de 10 números inteiros. Mostre então
qual o valor da soma e da média aritmética do conjunto'''


soma = 0
contador = 0
while contador < 10:
    entrada = float(input('Entre com um número: '))
    if contador <= 10:
      soma = soma + entrada
      contador += 1

print(' A média é : ', soma/ contador, 'E a soma é: ', soma)
