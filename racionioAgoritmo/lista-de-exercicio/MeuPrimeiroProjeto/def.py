def soma10(x): # 1 usage
    x = x+ 10
    return x
def encontra_poiscao(vetor, valor):
    vetor [0] = 0
    vetor[len(vetor) -1] = 0
    for i in range (len(vetor)):
        if valor == vetor[i]:
            return i
    return -1
def fatorial (n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n -1)

valor = 50
teste =100
y = soma10(valor)
vetor = [3,6,8,12,25]
print('x:', valor, 'y', teste)
pos = encontra_poiscao(vetor,12)
print('fatorial', fatorial(500))
print('poisção',pos,'vetor', vetor)