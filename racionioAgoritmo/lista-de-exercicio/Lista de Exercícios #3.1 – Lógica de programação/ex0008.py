'''Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro
informado pelo usuário.'''
max= int(input('Digite um número inteiro: '))
primos = []

for num in range(2, max + 1):
    primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        primos.append(num)

print(f'Números primos entre 1 e {max}:')
print(primos)
