'''Implemente um programa que permita multiplicar
uma matriz de ordem (3×3) de números inteiros
fornecida pelo usuário por um número também
fornecido pelo usuário. Lembrete: para multiplicar
uma matriz Am×n por um escalar k, basta multiplicar
cada entrada aij de A por k. Assim, a matriz resultante B
será também da ordem (m×n) e bij = k * aij.'''

m = []

for linha in range (3):
    linhaMatriz = []
    for coluna in range (3):
        n = int(input('Entre com um número da matriz: '))
        linhaMatriz.append(n)
    m.append(linhaMatriz)
m1 = []
coluna1= 0
for linha in range (3):
    linhaMatriz = []
    for coluna in range (3):
        num =  m[linha][coluna] *3
        linhaMatriz.append(num)
    m1.append(linhaMatriz)

print('MATRIZ')
for linha in m:
    print(linha)
print('MATRIZ X 3')
for linha in m1:
    print(linha)