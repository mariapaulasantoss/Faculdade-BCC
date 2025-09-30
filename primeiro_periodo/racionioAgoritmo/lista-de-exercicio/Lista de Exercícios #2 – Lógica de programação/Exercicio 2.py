'''A partir do ano de nascimento informado pelo usuário, elabore um algoritmo que informe
a idade que completará (ou já completou) em 2023. Verifique se ele já pode fazer a carteira
de motorista ou não, informando sua situação'''

#Entrada com o ano de nascimento
anoDeNascimento = int(input('Ano de Nascimento: '))

#Idade em 2023
idade = 2023 - anoDeNascimento

#Resultado
if idade >= 18:
    print('Já pode tirar a carteira de motorista')

else:
    print('Ainda não é permitido')