#Entradas de altura e raio
altura= float(input('Entre com a altura do cilindro:'))
raio= float(input('Entre com o raio do cilindro:'))

#Informaçõe/variáveis
valorLata= 50 #(em reais)
litrosPorLata= 5
metrosQuadradosPorL= 3

#Cálculo da área a ser pintada
areaDaBase = 3.14 * (raio * raio)
areaLateral = 2 * 3.14 * raio * altura
areaTotal = areaLateral + 2 * areaDaBase

#Quantos Litros de Tinta são necesssários:
litros= areaTotal/metrosQuadradosPorL

#Quantas latas de tinta são:
latasTinta = litros/litrosPorLata

#Valor a ser pago:
valorFinal= latasTinta * 50

#Saída
print('Valor gasto: R$',valorFinal)
print('Quantidade de latas: ', latasTinta)