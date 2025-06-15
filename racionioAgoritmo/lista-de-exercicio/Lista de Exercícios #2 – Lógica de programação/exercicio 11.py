''' Elabore um algoritmo que, dada a idade de um nadador, mostre sua classificação
segundo uma das seguintes categorias:'''

'''
° 5 até 7 anos: Infantil A;
• 8 até 10 anos: Infantil B;
• 11 até 13 anos: Juvenil A;
• 14 até 17 anos: Juvenil B;
° Maiores de 18 anos: Adulto'''

idade = int(input('Entre com sua idade: '))
adulto = idade >= 18

if idade < 5:
    print('Idade fora das categorias disponíveis')
elif 5 <= idade <= 7:
    print('Infantil A')
elif 8 <= idade <= 10:
    print('Infantil B')
elif 11 <= idade <= 13:
    print('Juvenil A')
elif 14 <= idade <= 17:
    print('Juvenil B')
else:
    print('Adulto')
