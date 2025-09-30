'''Faça um programa que leia uma quantidade indeterminada de números positivos, encerrando quando
a entrada for -1 e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-
100].'''

cont1= 0
cont2= 0
cont3= 0
cont4= 0

while True:

   n = int(input('Entre com um número e para inciiar o cálculo digite -1: '))
   if n == -1:
       break
   if n <=25:
       cont1 += 1
   elif n <= 50:
       cont2 += 1
   elif n <= 75:
       cont3 += 1
   elif n <= 100:
       cont4 += 1
   else:
       print('não se encontra em nenhum dos intervalos')

print(f'Há {cont1} dentros do intervalor [0-25])')
print(f'Há {cont2} dentros do intervalor [26-50])')
print(f'Há {cont3} dentros do intervalor [51-75])')
print(f'Há {cont4} dentros do intervalor [76-100])')