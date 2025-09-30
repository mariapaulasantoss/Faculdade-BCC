'''A partir das informações contidas na tabela abaixo, elabore um algoritmo que leia a
massa em kg de um boxeador e mostre a qual categoria ele pertence. Caso ele não se
encaixe, informe “Categoria inferior a Super-médio”. Lembrando que 1 quilograma =
2,20462262 libras.'''

peso = float(input('Qual o seu peso em kg? '))

pesoLibras = peso * 2.20462262

if pesoLibras >= 201:
    print('Peso-pesado')
elif  176 <= pesoLibras <= 200:
    print('Cruzador')
elif 169 <= pesoLibras <= 175:
    print('Meio-pesado')
elif 161 <= pesoLibras <= 168:
    print('Super-Médio')
else:
    print('Categoria Inferior a Super-médio')