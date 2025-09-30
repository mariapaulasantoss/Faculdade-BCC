'''Elabore um programa que leia um vetor de 10
 posições inteiras. Depois, solicite para o usuário um
número que ele gostaria de pesquisar neste vetor, caso o
número exista no vetor, mostre em qual(is)
posição(ões) ele foi encontrado e quantas ocorrências foram detectadas.'''
vetor = []
for i in range(1,11):
    n = int(input(f'Digite o {i}° número: '))
    vetor.append(n)
pesquisa = int(input('Digite o número que você deseja encontrar: '))
ocorrencia = 0
posicao = []
for i in range(len(vetor)):
    if vetor[i]== pesquisa:
        ocorrencia += 1
        posicao.append(i)
if ocorrencia > 0:
    print(f'O número {pesquisa} aparece na(s) posição(ções) {posicao} e foi detectado {ocorrencia} vez(es)')
else:
    print(f'O número {pesquisa}não foi encontrado na lista')