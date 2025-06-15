'''Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário
e mostre o valor do IMC e se ele está na faixa considerada “normal” segundo o critério
apresentado na tabela da OMS (Organização Mundial de Saúde): 18,5 ≤ IMC< 25. Caso
não esteja, calcule sua massa máxima considerada normal (usando IMC igual a 24,9)'''

peso = float(input('Qual o seu peso em quilogramas? '))
altura = float(input('Qual sua altura em metros? '))

imc = peso / (altura * altura)
print('O resultado do imc é: ', imc)
massaMaxima = 24.9 * (altura* altura)

if 18.5 <= imc < 25:
    print('peso normal ')

else:
    print ('Massa máxima normal', massaMaxima)

