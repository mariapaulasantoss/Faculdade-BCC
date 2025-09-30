'''Em uma determinada papelaria a fotocópia custa R$ 0,25, caso sejam tiradas menos de 100
cópias. A partir de 100 cópias, o valor de cada fotocópia tirada cai para R$ 0,20. Elabore
um algoritmo que leia o número de cópias e mostre o valor a pagar pelo serviço.'''

quantidadeDeCopias= int(input('Entre com a quantidade de cópias:'))

valorInicial= 0.25
valorComDesc= 0.20

if quantidadeDeCopias < 100:
    valor = quantidadeDeCopias * valorInicial
    print('O valor a ser pago pelo serviço será: ', valor)

else:
    valorDescontado = quantidadeDeCopias * valorComDesc
    print('O valor a ser pago pelo serviço será:', valorDescontado)
