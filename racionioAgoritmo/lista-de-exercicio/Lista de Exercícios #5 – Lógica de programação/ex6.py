''' A distância rodoviária entre algumas capitais brasileiras está disponível na tabela abaixo. Para
consultar a distância basta cruzar as cidades origem e destino, ou seja, a distância entre Curitiba e
São Paulo é de 408 km.
Construa um programa que inicialize uma matriz contendo as distâncias apresentadas na tabela acima
e que então informe ao usuário o tempo necessário para percorrer duas cidades por ele fornecidas'''

cidades = ['Curitiba','Florianópolis', 'Porto Alegre', 'São Paulo','Rio De Janeiro']
distancias =[[0, 310, 716,408,852],
            [310,0,470,705,1144],
            [716,470,0,1119, 1553],
             [408,705,1119,0,429],
            [852,1144,1553,429,0]]

origem = input('entre com o nome da cidade: ').title().strip()
destino = input('Entre o seu destino:  ').title().strip()
velocidade = int(input('Qual sua velocidade em KM/h? '))

#onde a cidade de origem estar
pos1 = -1
for i in range(len(cidades)):
    if origem== cidades[i]:
        pos1 = i
        break

pos2 = -1
#onde a cidade de destino estar
for j in range(len(cidades)):
    if destino == cidades[j]:
        pos2 = j
        break
#verifica se é uma das cidades da lista de listas
if pos1 == -1 or pos2 ==-1:
    print('Cidade inválida!Verifique o nome digitado.')
else:
    dist= distancias[pos1][pos2]
    tempo = dist / velocidade
    print(f'A distâcia entre a origem e o destino é {dist}Km')
    print(f'O tempo estimado é {tempo:.2f}  Km/h')

