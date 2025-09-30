#Entrada com o valor do produto
valorDoProduto = float(input('Valor do Produto: R$'))

# A vista com 5% de desconto
valorAvista= valorDoProduto - (valorDoProduto * 0.05)
#O valor da parcela em 2x
valorParcelado2= valorDoProduto/2
#O valor da parcela em 3x com acréscimo de 5%
valorComAcresimos= valorDoProduto * 1.05 /3

#Saídas
print('Valor do produto a vista: ', valorAvista)
print('Valor do produto parcelado em 2x: ', valorParcelado2)
print('Valor do produto parecelado em 3x e com acrecimo de 5%:', valorComAcresimos)
