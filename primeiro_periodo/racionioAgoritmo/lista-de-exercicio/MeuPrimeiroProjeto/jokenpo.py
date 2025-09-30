from random import randint

j = 0
j1 = 0
j2 = 0
comp = 0
comp1 = 0
comp2 = 0

continuar = 's'
while continuar == 's':
    itens = ['PEDRA', 'PAPEL', 'TESOURA']

    print('\nEscolha o modo de jogo:')
    print('[1] - HUMANO vs HUMANO')
    print('[2] - HUMANO vs COMPUTADOR')
    print('[3] - COMPUTADOR vs COMPUTADOR')

    modo = int(input('Qual sua escolha? '))
    if modo == 0:
        jogadas = [1,2,3]
        print('\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA')
        player1 = int(input('Jogador 1, escolha: '))
        player2 = int(input('Jogador 2, escolha: '))

        if player1 in jogadas and player2 in jogadas:
            print(f'Jogador 1 escolheu: {itens[player1 - 1]}')
            print(f'Jogador 2 escolheu: {itens[player2 - 1]}')

            if player1 == player2:
                print('Empate!')
            elif (player1 == 1 and player2 == 3) or (player1 == 2 and player2 == 1) or (player1 == 3 and player2 == 2):
                print('Vitória do jogador 1!')
                j1 += 1
            else:
                print('Vitória do jogador 2!')
                j2 += 1
        else:
            print('Escolha inválida!')
    elif modo == 1:
        jogadas = [1, 2, 3]
        print('\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA')
        player = int(input('Jogador, escolha: '))
        pc = randint(1, 3)

        if player in jogadas:
            print(f'O jogador escolheu: {itens[player - 1]}')
            print(f'O computador escolheu: {itens[pc - 1]}')

            if player == pc:
                print('Empate!')
            elif (player == 1 and pc == 3) or (player == 2 and pc == 1) or (player == 3 and pc == 2):
                print('Vitória do jogador!')
                j += 1
            else:
                print('Vitória do computador!')
                comp += 1
        else:
            print('Escolha inválida!')
    elif modo == 2:
        print('\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA')
        pc1 = randint(1, 3)
        pc2 = randint(1, 3)

        print(f'O computador 1 escolheu: {itens[pc1 - 1]}')
        print(f'O computador 2 escolheu: {itens[pc2 - 1]}')

        if pc1 == pc2:
            print('Empate!')
        elif (pc1 == 1 and pc2 == 3) or (pc1 == 2 and pc2 == 1) or (pc1 == 3 and pc2 == 2):
            print('Vitória do computador 1!')
            comp1 += 1
        else:
            print('Vitória do computador 2!')
            comp2 += 1
    else:
        print('Modo inválido!')

    print('--- PLACAR ATUAL ---')
    print(f'Jogador : {j}')
    print(f'Jogador 1: {j1}')
    print(f'Jogador 2: {j2}')
    print(f'Computador (vs jogador): {comp}')
    print(f'Computador 1: {comp1}')
    print(f'Computador 2: {comp2}')

    continuar = input('\nDeseja jogar novamente? (s/n): ')

print('--- PLACAR FINAL ---')
print(f'Jogador (vs comp): {j}')
print(f'Jogador 1: {j1}')
print(f'Jogador 2: {j2}')
print(f'Computador (vs jogador): {comp}')
print(f'Computador 1: {comp1}')
print(f'Computador 2: {comp2}')
print('Obrigada por se aventurar nesse game! Ana Luiza, Maria Paula, Tais e Sophia agradecem e esperam o novamente!')


