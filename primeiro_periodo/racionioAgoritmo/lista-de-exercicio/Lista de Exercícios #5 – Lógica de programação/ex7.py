cidades = ['Curitiba','Florianópolis', 'Porto Alegre', 'São Paulo','Rio De Janeiro']
distancias =[[0, 310, 716,408,852],
            [310,0,470,705,1144],
            [716,470,0,1119, 1553],
             [408,705,1119,0,429],
            [852,1144,1553,429,0]]
roteiro = []

print("Digite o nome das cidades do seu roteiro, uma por vez.")
print("Quando terminar, digite '1' para encerrar.")

while True:
    cidade = input("Digite a cidade: ").strip().title()
    if cidade == '1':
        break
    if cidade in cidades:
        roteiro.append(cidade)
    else:
        print("Cidade inválida. Tente novamente.")

if len(roteiro) < 2:
    print("Você precisa informar pelo menos duas cidades para calcular o roteiro.")
else:
    print("Roteiro fornecido:")
    for cidade in roteiro:
        print(f"- {cidade}")

    distancia_total = 0

    print("Distâncias entre os trechos:")
    for i in range(len(roteiro) - 1):
        origem = roteiro[i]
        destino = roteiro[i + 1]
        pos1 = cidades.index(origem)
        pos2 = cidades.index(destino)
        dist = distancias[pos1][pos2]
        distancia_total += dist
        print(f"{origem} → {destino} = {dist} km")

    print(f"\nDistância total do roteiro: {distancia_total} km")

