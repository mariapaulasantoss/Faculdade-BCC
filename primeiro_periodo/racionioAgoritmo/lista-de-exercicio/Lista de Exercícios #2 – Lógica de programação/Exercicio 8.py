''''Em um determinado estacionamento a primeira hora custa R$ 8,00, que é o valor mínimo
praticado. Após uma hora o valor é fracionado, R$ 1,50 a cada 15 minutos. Elabore um
algoritmo que leia um número inteiro correspondente a quantidade de minutos usados no
estacionamento e mostre a mensagem “Valor mínimo, R$ 8,00” ou “Valor fracionado, R$
x”, no qual x será o valor a pagar calculado pelo algoritmo.'''

minutos = int(input('Quantidade de minutos no estacionamento: '))
valorMinimo= 8
minutosAcima = minutos - 60
blocos15 = (minutosAcima + 14) // 15
valorFracionado = valorMinimo + blocos15 * 1.5

if minutos > 60:
    print('Valor fracionado, R$ ', valorFracionado)

else:
    print('Valor mínimo, R$ 8,00')