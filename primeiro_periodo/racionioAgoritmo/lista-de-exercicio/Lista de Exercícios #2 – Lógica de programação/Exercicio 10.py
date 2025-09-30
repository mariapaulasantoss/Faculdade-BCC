'''Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros)
dousuário e mostre  o valor do IMC e qual sua condição segundo o critério
 apresentado na tabela da OMS (Organização Mundial de Saúde)'''

#abaixo do peso = menor que 18,5
#no peso normal = entre 18,5 e 25
#acima do peso = entre 25 e 30
#obeso = acima de 30


peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual sua altura em metros? '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('abaixo do peso')
elif imc < 25:
    print('no peso normal')
elif imc < 30:
    print('acima do peso')
else:
    print('obeso')
