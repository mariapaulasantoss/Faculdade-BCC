'''Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabela
de conversão de metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10
quilômetros.'''

metrosmilha= 1609.344
km = 20

while km <= 160:
    milhas = km * 1000 / metrosmilha
    print(milhas, km *1000)
    km += 10

print("Fim")
