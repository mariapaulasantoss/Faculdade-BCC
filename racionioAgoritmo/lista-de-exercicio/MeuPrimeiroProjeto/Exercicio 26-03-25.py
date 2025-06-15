
soma = 0
contador = 0
entrada = 0
while entrada != -1:
    entrada = float(input('Entre com um número: '))
    if entrada!= -1:
      soma = soma + entrada
      contador += 1

print(' A média é : ', soma/ contador)