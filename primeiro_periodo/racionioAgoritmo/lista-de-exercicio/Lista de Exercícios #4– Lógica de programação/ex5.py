'''Ler 4 números inteiros e calcular a soma dos que forem par'''
par = 0
cont = 0
for i in range (1,5):
    n = int(input(f'Digite o {i} valor: '))
    if n%2 == 0:
        par += n
        cont += 1
print(f'Você informou {cont} números pares e a soma entre ele resulta em {par}')