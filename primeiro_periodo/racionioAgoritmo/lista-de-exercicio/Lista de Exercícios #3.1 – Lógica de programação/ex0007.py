'''Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que
peça um número inteiro e determine se ele é ou não um número primo.'''

n = int(input('Entre com um número inteiro: '))

if n < 2:
    print(f'{n} **não** é um número primo.')
else:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    if primo:
        print(f'{n} é um número primo.')
    else:
        print(f'{n} não é um número primo.')
