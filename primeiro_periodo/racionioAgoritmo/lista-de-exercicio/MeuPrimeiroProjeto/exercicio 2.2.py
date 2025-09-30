#verificar se o horário esta
#dentro do horário de funcionamento da PUCPR. Assumir entre
#7:30h e 23:10h

hora= int(input('Entre com a hora: '))
minutos= int(input('Entre com os minutos: '))

inicio = 7 * 60 + 30
fim = 23 * 60 + 10

horarioDeFuncionamento = hora * 60 + minutos

if  inicio <= horarioDeFuncionamento <= fim:
    print('Está dentro do horário de funcionamento')

else:
    print('Fora do horário de funcionamento')