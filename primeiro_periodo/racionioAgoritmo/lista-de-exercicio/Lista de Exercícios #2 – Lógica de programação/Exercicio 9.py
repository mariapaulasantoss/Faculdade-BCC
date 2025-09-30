''' partir da idade informada de uma pessoa, elabore um algoritmo que informe a sua
classe eleitoral, sabendo que menores de 16 não votam (não votante), que o voto é
obrigatório para adultos entre 18 e 65 anos (eleitor obrigatório) e que o voto é opcional
para eleitores entre 16 e 18, ou maiores de 65 anos (eleitor facultativo).
'''
idade = int(input('Entre com a sua idade: '))

#eleitores opicionais
if 16 <= idade < 18:
    print('Opicional')
#eleitor obrigatório
elif 18 <= idade <65:
    print('eleitor obrigatório')
#não votante
elif idade < 16:
    print('não votante')
#eleitor facultativo
else:
    print('eleitor facultativo')