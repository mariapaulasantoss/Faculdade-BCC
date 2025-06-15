'''Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é
triangular'''

num = int(input('Entre com um número inteiro positivo: '))

teste = 1  # Começa em 1, pois 0 não faz sentido nesse contexto
conta = 0

while conta <= num:
    conta = teste * (teste + 1) * (teste + 2)

    if conta == num:
        i = True
        break
    elif conta > num:
        i = False
        break

    else:
        teste += 1
if i == True:
   print(f'{num} é um número triangular (produto de {teste}, {teste + 1} e {teste + 2})')
else:
   print(f'{num} não é um número triangular')