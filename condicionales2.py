#Los tres numeros "dados" de muestran en una lista
lista_numeros = [45, 50, 40]


#verifico el tipo de dato int para comparar      
print (type(lista_numeros[0]))


if lista_numeros[0]> lista_numeros[1] and lista_numeros[0]> lista_numeros[2]:
    if lista_numeros[1]> lista_numeros[2]:
        print(lista_numeros[0], lista_numeros[1], lista_numeros[2])
    else:
        print(lista_numeros[0], lista_numeros[2], lista_numeros[1])
elif lista_numeros[1]> lista_numeros[0] and lista_numeros[1]> lista_numeros[2]:
    if lista_numeros[0]> lista_numeros[2]:
        print(lista_numeros[1], lista_numeros[0], lista_numeros[2])
    else:
        print(lista_numeros[1], lista_numeros[2], lista_numeros[0])
elif lista_numeros[2]> lista_numeros[1] and lista_numeros[2]> lista_numeros[0]:
    if lista_numeros[1]> lista_numeros[0]:
        print(lista_numeros[2], lista_numeros[1], lista_numeros[0])
    else:
        print(lista_numeros[2], lista_numeros[0], lista_numeros[1])        



"""
Forma de resolverlo utilizando conocimiento de clases más avanzadas:

def demayoramenor():
    lista_numeros.sort(reverse=True)
    print(lista_numeros)


demayoramenor() """