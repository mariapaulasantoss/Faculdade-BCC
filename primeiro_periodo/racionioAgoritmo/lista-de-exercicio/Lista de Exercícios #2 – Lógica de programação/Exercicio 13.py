'''Em uma determinada loja de eletrodomésticos, os produtos podem ser adquiridos da
seguinte forma. Elabore um algoritmo que leia a opção do cliente e o preço de tabela do produto, mostrando
então o valor calculado conforme a condição escolhida'''
''''''
opcoes= int(input(' Escolha uma opção de 1 a 4: '))

preco = float(input('Entre com o valor do produto: R$ '))

if opcoes ==1:
    valor1 = preco * 0.92
    print('O preço do produto será: R$', valor1)

elif opcoes == 2:
    valor2 = (preco * 0.96)/2
    print('O preço do produto será: R$', valor2)

elif opcoes == 3:
    valor3 = preco / 3
    print('O preço do produto será: R$', valor3)

else:
    valor4 = (preco * 1.04)/4
    print('O preço do produto será: R$', valor4)
