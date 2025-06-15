'''Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de
1 a 20 polegadas. A conversão entre estas duas unidades é dada por: polegada =
centímetro × 2,54'''

polegada = 1

while polegada <=20:
    centimetro= polegada * 2.54
    print(polegada, '|', centimetro)
    polegada += 1

