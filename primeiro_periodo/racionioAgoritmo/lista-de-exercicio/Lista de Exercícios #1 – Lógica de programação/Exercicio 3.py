#Faça um algoritmo que receba o salário de um profissional e calcule quantos salário
#mínimos ele recebe

#Entrada do valor do salário mínimo
salarioMinimo = 1518.00

#Sálario que o profissional recebeu
salario = float(input('Entrada do salário do profissional: R$ '))

# Calculo da quantidade de salários mínimos
quantidadeSalariosMinimos= salario // salarioMinimo

#Resultado
print('A quantidade de salários mínimos recebidos é' , quantidadeSalariosMinimos)
