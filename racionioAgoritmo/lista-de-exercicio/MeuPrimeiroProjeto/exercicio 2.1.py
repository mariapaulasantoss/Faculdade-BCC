# Qual o peso do usuário?
peso = float(input('Qual o seu peso em quilogramas? '))

#Qual a altura do usuário?
altura = float(input('Qual sua altura em metros? '))

# Cálculo do IMC
imc = peso / (altura * altura)
print(' O resultado do seu IMC é: ', imc)

# muito abaixo de ideal: imc < 16
# normal: imc >= 16 and imc <= 25

if imc < 16 :
    print('seu imc está muito abaixo do ideal')
elif imc < 25:
    print ('seu imc é ideal')
elif  imc < 30:
    print ('seu imc está acima do ideal')
else:                                                   #não adimite condição
    print ('seu imc está muito acima do ideal')
    print ('entrou else')