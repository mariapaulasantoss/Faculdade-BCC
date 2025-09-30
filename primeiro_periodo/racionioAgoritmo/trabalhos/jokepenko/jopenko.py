from time import sleep
from random import randint

j1 = 0
j2 = 0
comp = 0       # Computador no modo Jogador x Computador
comp1 = 0      # Computador 1 no modo Computador x Computador
comp2 = 0      # Computador 2 no modo Computador x Computador
modos = ('JogadorxJogador', 'JogadorxComputador', 'ComputadorxComputador')

print('''Selecione seu modo de jogo:
[ 0 ] Jogador x Jogador
[ 1 ] Jogador x Computador
[ 2 ] Computador x Computador''')

modoDeJogo = int(input('Qual é o modo de jogo escolhido? '))

while True:  # continua até o jogador decidir parar
    computador = randint(0, 2)
    computador2 = randint(0, 2)

    if modoDeJogo == 0:  # Jogador x Jogador
        jogada = ['Pedra', 'Papel', 'Tesoura']
        print('''Selecione as jogadas:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
        jogada1 = int(input('Insira a primeira jogada escolhida: '))
        jogada2 = int(input('Insira a segunda jogada escolhida: '))

        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO')
        sleep(1)

        print('-*' * 16)
        print('O jogador 1 jogou {}'.format(jogada[jogada1]))
        print('O jogador 2 jogou {}'.format(jogada[jogada2]))
        print('-*' * 16)

        if jogada1 == jogada2:
            print('EMPATE!')
        elif (jogada1 == 0 and jogada2 == 2) or \
             (jogada1 == 1 and jogada2 == 0) or \
             (jogada1 == 2 and jogada2 == 1):
            print('JOGADOR UM VENCE!')
            j1 += 1
        else:
            print('JOGADOR DOIS VENCE!')
            j2 += 1

    elif modoDeJogo == 1:  # Jogador x Computador
        jogada = ['Pedra', 'Papel', 'Tesoura']
        print('''Selecione sua jogada:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
        jogada1 = int(input('Insira a jogada escolhida: '))

        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO')
        sleep(1)

        print('-*' * 16)
        print(f'O jogador jogou {jogada[jogada1]}')
        print(f'O computador jogou {jogada[computador]}')
        print('-*' * 16)

        if jogada1 == computador:
            print('EMPATE!')
        elif (jogada1 == 0 and computador == 2) or \
             (jogada1 == 1 and computador == 0) or \
             (jogada1 == 2 and computador == 1):
            print('JOGADOR UM VENCE!')
            j1 += 1
        else:
            print('COMPUTADOR VENCE!')
            comp += 1

    elif modoDeJogo == 2:  # Computador x Computador
        jogada = ['Pedra', 'Papel', 'Tesoura']
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO')
        sleep(1)

        print('-*' * 16)
        print(f'O computador um escolheu {jogada[computador]}')
        print(f'O computador dois escolheu {jogada[computador2]}')
        print('-*' * 16)

        if computador == computador2:
            print('EMPATE!')
        elif (computador == 0 and computador2 == 2) or \
             (computador == 1 and computador2 == 0) or \
             (computador == 2 and computador2 == 1):
            print('COMPUTADOR UM VENCE!')
            comp1 += 1
        else:
            print('COMPUTADOR DOIS VENCE!')
            comp2 += 1

    else:
        print('Modo de jogo inválido')
        break

    sleep(1)
    print('----- PLACAR ATUAL -----')
    print(f'Jogador 1: {j1}')
    print(f'Jogador 2: {j2}')
    print(f'Computador: {comp}')
    print(f'Computador 1: {comp1}')
    print(f'Computador 2: {comp2}')

    print('''Deseja continuar?
[ 0 ] Finalizar
[ 1 ] Reiniciar''')
    finalizar = int(input('Escolha: '))
    if finalizar == 0:
        print('Encerrando o jogo. Até a próxima!')
        break
    elif finalizar == 1:
        print('\nReiniciando...\n')
        sleep(1)
    else:
        print('Opção inválida. Encerrando por segurança.')
        break

print('----* PLACAR FINAL *-----')
print(f'Jogador 1: {j1}')
print(f'Jogador 2: {j2}')
print(f'Computador: {comp}')
print(f'Computador 1: {comp1}')
print(f'Computador 2: {comp2}')
print('Obrigada por se aventurar nesse game.')
print('Ana Luiza, Maria Paula, Thais e Sophia agradecem!')
