frutas = ['laranja', 'maça', 'pera',
'banana', 'kiwi', 'maça', 'banana']
indice = 0
while indice < len(frutas):
  print(frutas[indice])
  indice = indice + 1
#implementa um código em python que retorna
# a posição de uma fruta dentro do vetor,
#sendo o nome fornecido pelo usuário.

fruta = input('entre com o nome da fruta a pesquisar: ')
i = 0
'''encontrou = False #uma flag é uma variável bool
while i < len(frutas) and not encontrou:
    if fruta == frutas[i]:
        encontrou =True
        print('A fruta', fruta,'está na posição', i)
    i += 1
if not encontrou:
    print('A fruta não existe')'''

for i in range (len(frutas)):
    if fruta == frutas[i]:
        print('A fruta', fruta, 'está na posição', i)

