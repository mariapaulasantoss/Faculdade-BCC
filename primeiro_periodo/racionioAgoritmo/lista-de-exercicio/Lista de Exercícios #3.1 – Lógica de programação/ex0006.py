'''Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a
média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem,
adulta ou idosa, conforme a média calculada'''


soma = 0
cont = 0
continuar = 's'

while continuar != 'n':
    idade = int(input('Entre com a sua idade: '))
    soma += idade
    cont += 1
    opcao = input('Deseja continuar (s/n)? ')
    if opcao == 'n':
        break
media = soma/ cont
print(media)

if media <= 25:
    print(f'Temos uma turma jovem, com uma media de {media} anos ')
elif media <= 60:
    print(f'Temos uma turma adulta, com uma media de {media} anos ')
else:
    print(f'Temos uma turma idosa, com uma media de {media} anos ')
















