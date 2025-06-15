''' Ler do teclado uma quantidade de números inteiros a serem lidos e calcular:
a) a soma total entre eles
b) a soma dos que forem pares.
c) a soma dos que forem ímpares
d) a amplitude amostral considerando todos os números lidos (diferença entre o maior e o menor)'''

soma = 0
somaPar = 0
somaImpar = 0
numeros = 0
continuar = True
par = 0
maior =
menor =

while continuar:
  numeros= int(input('Entre com um número '))

  soma += numeros
  resto = numeros % 2

  if resto == 0:
        somaPar += numeros
  else:
      somaImpar += numeros

  inserir = input("Deseja continuar sim ou não? ")
  if inserir == 'não':
   continuar = False

  else:
      continuar = True
print(soma, somaPar, somaImpar)


