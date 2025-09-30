'''Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido.
Depois, crie dois outros vetores: vPares, contendo somente os números pares de vLido, e vImpares
contendo somente os números ímpares de vLido. Os vetores vPares e vLido não deverão conter
zeros. Mostre então os três vetores'''

vLido = []
vPar = []
vImpar = []
for i in range (1,11):
    n= int(input(f'Digite o {i}° número: '))
    if n > 0:
      vLido.append(n)
for i in vLido:
    if i %2 ==0:
        vPar.append(i)
    else:
        vImpar.append(i)
print(f'Os número digitados foram: {vLido}')
print(f'Os números pares: {vPar}')
print(f'Os número ímpares: {vImpar}')