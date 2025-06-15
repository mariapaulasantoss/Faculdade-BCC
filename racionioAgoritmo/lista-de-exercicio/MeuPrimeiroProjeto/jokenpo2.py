from random import randint

j = 0
j1 = 0
j2 = 0
comp = 0
comp1 = 0
comp2 = 0

continuar = 's'
while continuar == 's':

    print('Escolha o modo de jogo:')
    print('[0] HUMANO vs HUMANO')
    print('[1] HUMANO vs MÁQUINA')
    print('[2] MÁQUINA vs MÁQUINA')

    modo = int(input('Qual sua escolha? '))

    if modo == 0:
        print('Muito bem! \n [1]PEDRA \n [2]PAPEL \n [3]TESOURA')
        player1 = int(input('Considerando as opções acima, faça a sua escolha?'))
        player2 = int(input('Considerando as opções acima, faça a sua escolha?'))
        itens = ('PEDRA', 'PAPEL', 'TESOURA')
        print(f'O jogador 1 escolheu  {(itens[player1 - 1])}')
        print(f'O jogador 2 escolheu {(itens[player2 - 1])}')
        if player1 == 1:
            if player2 == 1:
                print('Empate!')
            elif player2 == 2:
                print('Vitória do jogador 2')
                j2 += 1
            elif player2 == 3:
                print('Vitória do jogador 1')
                j1 += 1
            else:
                print('Ops...Valor inválido')
        elif player1 == 2:
            if player2 == 1:
                print('Vitória do jogador 2')
                j2 += 1
            elif player2 == 2:
                print('Empate!')
            elif player2 == 3:
                print('Vitória do jogador 1')
                j1 += 1
            else:
                print('Ops...Valor inválido')
        elif player1 == 3:
            if player2 == 1:
                print('Vitória do jogador 2')
                j2 += 1
            elif player2 == 2:
                print('Vitória do jogador 1')
                j1 += 1
            elif player2 == 3:
                print('Empate!')
            else:
                print('Ops...Valor inválido')
        else:
            print('Ops...valor inválido, tente novamente!')

    elif modo == 1:
        print('Muito bem! \n [1]PEDRA \n [2]PAPEL \n [3]TESOURA')
        player = int(input('Considerando as opções acima, faça a sua escolha?'))
        pc = randint(1, 3)
        itens = ('PEDRA', 'PAPEL', 'TESOURA')
        print(f'O jogador 1 escolheu  {(itens[player - 1])}')
        print(f'O computador escolheu {(itens[pc - 1])}')
        if pc in:
            if player == 1:
                print('Empate!')
            elif player == 2:
                print('Vitória do jogador')
                j += 1
            elif player == 3:
                print('Vitória do pc')
            else:
                print('Ops...Valor inválido')
        elif pc == 2:
            if player == 1:
                print('Vitória do pc')
            elif player == 2:
                print('Empate!')
            elif player == 3:
                print('Vitória do jogador')
            else:
                print('Ops...Valor inválido')
        elif pc == 3:
            if player == 1:
                print('Vitória do jogador ')
            elif player == 2:
                print('Vitória do pc')
            elif player == 3:
                print('Empate!')
            else:
                print('Ops...Valor inválido')
        else:
            print('Ops...valor inválido, tente novamente!')

    elif modo == 2:
        pc1 = randint(1, 3)
        pc2 = randint(1, 3)
        itens = ('PEDRA', 'PAPEL', 'TESOURA')
        print(f'O computador 1 escolheu  {(itens[pc1 - 1])}')
        print(f'O computador 2 escolheu {(itens[pc2 - 1])}')
        if pc1 == 1:
            if pc2 == 1:
                print('Empate!')
            elif pc2 == 2:
                print('Vitória do pc2')
            elif pc2 == 3:
                print('Vitória do pc1')
            else:
                print('Ops...Valor inválido')
        elif pc1 == 2:
            if pc2 == 1:
                print('Vitória do pc1')
            elif pc2 == 2:
                print('Empate!')
            elif pc2 == 3:
                print('Vitória do pc2')
            else:
                print('Ops...Valor inválido')
        elif pc1 == 3:
            if pc2 == 1:
                print('Vitória do pc2')
            elif pc2 == 2:
                print('Vitória do pc1')
            elif pc2 == 3:
                print('Empate!')
            else:
                print('Ops...Valor inválido')
        else:
            print('Ops...valor inválido, tente novamente!')

    print('\n--- PLACAR ATUAL ---')
    print(f'Jogador: {j}')
    print(f'Jogador 1: {j1}')
    print(f'Jogador 2: {j2}')
    print(f'Computador (vs jogador): {comp}')
    print(f'Computador 1: {comp1}')
    print(f'Computador 2: {comp2}')

    continuar = input('\nDeseja jogar novamente? (s/n): ')

print('\n--- PLACAR FINAL ---')
print(f'Jogador (vs comp): {j}')
print(f'Jogador 1: {j1}')
print(f'Jogador 2: {j2}')
print(f'Computador (vs jogador): {comp}')
print(f'Computador 1: {comp1}')
print(f'Computador 2: {comp2}')
print('Obrigada por se aventurar nesse game. \nAna Luiza, Maria Paula, Tais e Sophia agradecem!')

