'''Implemente uma máquina de venda de bebidas em Python, de acordo com os requisitos abaixo:'''

"""ID Produto  Valor  Estoque
 1 Coca-cola |R$ 3,75 | 2
 2 Pepsi     |R$ 3,67 | 5
 3 Monster   |R$ 9,96 | 1
 4 Café      |R$ 1,25 | 100
 5 Redbull   |R$ 13,99| 2
"""
#imprime a tabela de bebidas para o consumidor
print('''Tabela de bebidas 
[1] Coca-cola
[2] Pepsi
[3] Monster
[4] Café
[5] Redbull''')

while True:
   id_produto = int(input('Insira o ID da sua bebida: '))
      if 0 < id_produto < 6:
         break
    else:
        continue

