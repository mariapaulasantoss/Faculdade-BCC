from random import randint


modos = ('JogadorxJogador', 'JogadorxComputador', 'ComputadorxComputador')
print('''Selecione seu modo de jogo:
    [ 0 ] Jogador x Jogador
    [ 1 ] Jogador x Computador
    [ 2 ] Computador x Computador''')
modoDeJogo = int(input('Qual é o modo de jogo escolhido?'))
while True:  #faz com que o player continue jogando até que ele decida parar o jogo
    computador = randint(0, 2)
    computador2 = randint(0, 2)

    elif modoDeJogo == 2:  #Computador x Computador
        print('''Jogadas possíveis:
            [ 0 ] PEDRA
            [ 1 ] PAPEL
            [ 2 ] TESOURA''')
        jogada = ['Pedra', 'Papel', 'Tesoura']
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO')
        sleep(1)
        print('-*' * 16)
        print('O computador um escolheu {}'.format(jogada[computador]))
        print('O computador dois escolheu {}'.format(jogada[computador2]))
        print('-*' * 16)
        if computador2 == 0:   #computador2 escolheu PEDRA
            if computador == 0:  #computador1 escolheu PEDRA
                print('EMPATE!')
            elif computador == 1:  #computador1 escolheu PAPEL
                print('COMPUTADOR UM VENCE!')
                comp1 += 1
            elif computador == 2:  #computador1 escolheu TESOURA
                print('COMPUTADOR DOIS VENCE!')
                comp2 += 1
            else:
                print('JOGADA INVÁLIDA!')
        elif computador2 == 1:  #computador2 escolheu PAPEL
            if computador == 0:  #computador1 escolheu PEDRA
                print('COMPUTADOR DOIS VENCE!')
                comp2 += 1
            elif computador == 1:  #computador1 escolheu PAPEL
                print('EMPATE!')
            elif computador == 2:  #computador1 escolheu TESOURA
                print('COMPUTADOR UM VENCE!')
                comp1 += 1
            else:
                print('JOGADA INVÁLIDA!')
        elif computador2 == 2:  #computador2 escolheu TESOURA
            if computador == 0:  #computador1 escolheu PEDRA
                print('COMPUTADOR UM VENCE!')
                comp1 += 1
            elif computador == 1:  #computador1 escolheu PAPEL
                print('COMPUTADOR DOIS VENCE!')
                comp2 += 1
            elif computador == 2:  #computador1 escolheu TESOURA
                print('EMPATE!')
            else:
                print('JOGADA INVÁLIDA!')
        else:
            print('JOGADA INVÁLIDA!')

    else:
        print('Modo de jogo inválido')

    sleep(1)
    print('----- PLACAR ATUAL-----')
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

print('----* PLACAR FINAL*-----*-')
print(f'Jogador 1: {j1}')
print(f'Jogador 2: {j2}')
print(f'Computador: {comp}')
print(f'Computador 1: {comp1}')
print(f'Computador 2: {comp2}')
print('Obrigada por se aventurar nesse game. \nAna Luiza, Maria Paula, Thais e Sophia agradecem!')