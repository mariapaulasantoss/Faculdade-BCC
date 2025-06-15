'''Ler do teclado uma quantidade de números inteiros a serem lidos e calcular:
a) a soma total entre eles
b) a soma dos que forem pares.
c) a soma dos que forem ímpares
d) a amplitude amostral considerando todos os números lidos (diferença entre o maior e o menor.'''

quantidade = int(input('coloque a quantidade de númeroes inteiro a calcular: '))

soma = 0
impar = 0
par = 0
numeros = []

for i in range(quantidade):
    num= int(input('Entre com um número: '))
    numeros.append(num)
    soma += num

    if num % 2 == 0:
        par += num
    else:
        impar += num

    inserir = input("Deseja continuar? (sim/não): ")
    if inserir == 'não':
        continuar = False

amplitude = max(numeros) - min(numeros)

print("Soma total:", soma)
print("Soma dos pares:", par)
print("Soma dos ímpares:", impar)
print("Amplitude amostral:", amplitude)

