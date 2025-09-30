'''Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de
crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de
1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população
do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento'''

hA = 80000
hB = 200000
anos = 0


while hA <= hB:
    hA += hA * 0.03
    hB+= hB *  0.015
    anos += 1
print(f'"A"ultrapassa ou iguala sua população ao país "B" em {anos} anos')