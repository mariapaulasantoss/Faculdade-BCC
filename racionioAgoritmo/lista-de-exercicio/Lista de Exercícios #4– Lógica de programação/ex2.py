'''Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição'''
for i in range(1, 101):
    mult = (i - 1) // 10 + 1
    multiplicador = (i - 1) % 10 + 1
    print(f'{mult} x {multiplicador} = {mult * multiplicador}')
print()