'''A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor
máximo e o valor mínimo de uma amostra. Elabore um programa que leia um vetor de 10 posições
inteiras e então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto
fornecido.'''

vetor = []
n = 0
for i in range(1,11):
    n = int(input('Entre com o valor: '))
    vetor.append(n)

print(f'O maior valor é {max(vetor)} e o menor é o {min(vetor)}')
print(f'A amplitude amostral desse vetor  é {max(vetor)- min(vetor)}')
