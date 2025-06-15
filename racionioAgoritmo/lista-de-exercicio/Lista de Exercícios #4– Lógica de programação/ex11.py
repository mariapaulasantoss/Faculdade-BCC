'''Construa um programa que sugira uma aposta de Mega-Sena ou seja,
um algoritmo que gera e mostra um conjunto de 6 números aleatórios
entre [1, 60] sem repetição. Em seguida, obtenha a aposta do
usuário (sem repetição) e indique quantos acertos ele teve'''
from random import sample
computador = sample(range(1,61),6)
bet = []
print('Faça sua aposta! Escolha entre 1 a 60 e boa sorte!')
for i in range(1,7):
    choice = int(input(f'NÚMERO {i}: '))

    if choice in bet:
        while True:
            print ('Você já utilizou esse número. Por favor, tente novamente!')
            choice = int(input(f'NÚMERO {i}: '))
            if choice not in bet:
                break
    if choice <1 or choice >60:
        print('Número fora das alternativa. Tente novamente com um número entre 1 a 60')
        while True:
            choice = int(input(f'NÚMERO {i}: '))
            if choice >= 1 or choice <=60:
                break

    bet.append(choice)
acertos = []
for num in bet:
    if num in computador:
        acertos.append(num)

print(f'Mega-Sena: {computador}')
print(f'Sua aposta: {bet}')
print(f'Você acertou {acertos} número(s): {acertos}')




