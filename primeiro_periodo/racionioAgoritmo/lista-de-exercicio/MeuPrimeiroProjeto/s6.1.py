matrizVencedor = [['empate', 'jogador2', 'jogador1'],
                  ['jogador1', 'empate', 'jogador2'],
                  ['jogador1','jogador2', 'empate' ]
                  ]

print('''Escolha sua jogada:
[0] Pedra
[1] Papel
[2] Tesoura
''')
j1= int(input('Escolha: '))
j2= int(input('Escolha: '))

print(matrizVencedor[j1][j2])





