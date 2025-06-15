# matriz que corresponde aos valores determinados
matriz = [[1, 3.75, 2],
          [2, 3.67, 5],
          [3, 9.96, 1],
          [4, 1.25, 100],
          [5, 13.99, 2]]

# dicionário que relaciona os produtos com os IDs
nome_produtos = {
    1: "Coca-Cola",
    2: "Pepsi",
    3: "Monster",
    4: "Café",
    5: "Redbull"
}

print('''Selecione abaixo o Id correspondente à bebida que deseja comprar:
     [1] Coca-cola
     [2] Pepsi
     [3] Monster
     [4] Café
     [5] Redbull''')

# Loop para seleção do ID
while True:
    id_digitado = int(input('Insira o valor do Id desejado: '))
    if 1 <= id_digitado <= 5:
        produto_encontrado = matriz[id_digitado - 1]
        estoque = produto_encontrado[2]

        if estoque == 0:
            print('Esse produto está fora do estoque. Por favor, escolha outro.')
            continue  # volta para pedir um novo ID
        else:
            break
    else:
        print("ID inválido. Tente novamente.")

# Obtém informações do produto
nome = nome_produtos[produto_encontrado[0]]
valor = produto_encontrado[1]
estoque = produto_encontrado[2]

# Mostra os dados do produto escolhido
print(f"\nID: {id_digitado} | Nome: {nome} | Valor: R${valor:.2f} | Estoque: {estoque}")

# Loop para inserir o dinheiro
while True:
    valor_inserido = float(input('Insira o valor colocado na máquina: R$ '))
    if valor_inserido >= valor:
        troco = valor_inserido - valor
        if troco > 0:
            print(f"Troco: R${troco:.2f}")
        print("Em alguns segundos receberá sua bebida!")
        produto_encontrado[2] -= 1  # atualiza o estoque na matriz
        break
    else:
        print("Valor abaixo do requisitado. Insira um valor válido!")

# Exibe estoque atualizado
print(f"Compra concluída. Estoque restante de {nome}: {produto_encontrado[2]}")

