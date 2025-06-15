lista = []
for i in range (1,4):
    n = int(input('Digite um número: '))
    lista.append(n)
print( 'O maior valor de entrada foi', max(lista),'e o menor', min(lista))