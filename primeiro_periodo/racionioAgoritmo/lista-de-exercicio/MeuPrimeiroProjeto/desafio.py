# Desenvolver um algoritmo que lê
# um vetor de 10 números inteiros
# e retorna uma lista com elementos pares

lista = []
for i in range(1,11):
    n = int(input('Digite um número: '))
    if n %2 == 0:
        lista.append(n)
print(lista)