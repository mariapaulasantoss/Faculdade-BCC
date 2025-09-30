cidades = ['pg','curitiba','sjp', 'castro', 'paranagua']

distancias = [[0,120, 140, 25,210],
[120,0, 20, 145, 80],
[140,20, 0, 140, 60],
[20,140, 160, 0, 220],
[210,80, 60, 220,0]]

cidade = input('entre com o nome da cidade: ')
distMax = int(input('Entre com a distância máxima: '))

pos = -1
for i in range(len(cidades)):
    if cidade == cidades [i]:
        pos = i
    vetorResposta = []
    if pos == -1:
       print('cidade inexistente')
    else:
        for i2 in range (len(cidades)):
           if distancias [pos][i2] <= distMax:
               vetorResposta.append(cidades[i2])
print(f'As cidades encontradas são: {vetorResposta}')



