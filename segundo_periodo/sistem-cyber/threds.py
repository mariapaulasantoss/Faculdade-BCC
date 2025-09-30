import threading
list = [90,81,78,95,79,72,85]

def maximo(list):
    maximo = max(list)
    return print (maximo)

def minimo(list):
    minimo = min(list)

    return print (minimo)

def media(list):
    media = sum(list)/len(list)
    return print (media)

def calculos(list):     
    media_thread = threading.Thread(target = media,args=(list,))
    minimo_thread = threading.Thread(target = minimo,args=(list,))
    maximo_thread = threading.Thread(target = maximo,args=(list,))


    media_thread.start()
    minimo_thread.start()
    maximo_thread.start()

thread_principal = threading.Thread(target = calculos, args=(list,))
thread_principal.start()

