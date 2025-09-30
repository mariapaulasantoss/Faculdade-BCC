'''Desenvolva um programa que leia um vetor de 20 posições inteiras e o coloque em ordem crescente,
utilizando a seguinte estratégia de ordenação:
• selecione o elemento do vetor de 20 posições que apresenta o menor valor;
• troque este elemento pelo primeiro;
• repita estas operações, envolvendo agora apenas os 19 elementos restantes (trocando o de
menor valor com a segunda posição), depois os 18 elementos (trocando o de menor valor com a
terceira posição), depois os 17, 16 e assim por diante, até restar um único elemento, o maior
deles.
Observação: este método de ordenação é conhecido como Seleção Direta.
'''

v = []
print('Entre com um vetor de 20 posições')
for i in range(1,21):
    num = int(input('Entre com um número: '))
    v.append(num)
menor = []
for i in range(1,21):
    menor.append(min(v))
    v.remove(min(v))
print(menor)