''' Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um
algoritmo que leia o código da moeda que o cliente quer comprar e qual o montante
que ele quer adquirir nessa moeda. Mostre então quanto ele deverá pagar em reais
para concretizar a operação. Além da cotação, a empresa cobra uma comissão de 5%
(quando o valor for menor que R$ 1.000), ou de 3% (quando maior ou igual a
R$1.000). Considere o câmbio do dia.
'''
continuar = True
while continuar:

 dolares = 1
 libras = 2
 euro = 3

 cotacaoDolares = 6.7
 cotacaoLibras = 7.34
 cotacaoEuro = 6.13

 moedaEscolhida = int(input('Entre de com uma das três opções: 1 - Dolar, 2 - Libra e 3 - Euro:  '))
 montante = int(input('Qual o montante que  dejesa adiqueirir? '))

 #dolar
 if moedaEscolhida ==1:
    operacao = montante * cotacaoDolares
    print('Valor a ser pago em reais: R$', operacao)
 #libra

 elif moedaEscolhida == 2:
     operacao= montante * cotacaoLibras
     print('Valor a ser pago em reais: R$', operacao)
 #libra
 else:
     operacao= montante * cotacaoEuro
     print('Valor a ser pago em reais: R$', operacao)


 if operacao >= 1000:
     valor = operacao * 0.03
     print('Comisão', valor)
 else:
     valor = operacao * 0.05
     print('Comisão ', valor)

 print('O valor total a ser pago será: R$', valor+operacao)

 opcao = input('Deseja continuar (s/n): ')
 if opcao != 's':
    continuar = False
    print('Fim!')