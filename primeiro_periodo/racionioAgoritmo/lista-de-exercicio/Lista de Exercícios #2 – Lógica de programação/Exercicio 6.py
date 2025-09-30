altura= float(input('Entre com a sua altura:'))
sexo= int(input('Entre com o seu sexo indicando (1) se for masculino e (2) feminino:'))

if sexo ==1:
    pesoIdealH= (72.7 * altura) - 58
    print('O seu peso ideal será: ', pesoIdealH)

else:
    pesoIdealM= (62.1 * altura) - 44.7
    print('O seu peso ideal será: ', pesoIdealM)
