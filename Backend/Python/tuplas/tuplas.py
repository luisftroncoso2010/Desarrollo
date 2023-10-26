#Acceder a los elementos  de una tupla
'''
Acceder a los elementos de uan tupla 
'''
thisTuple = ('apple', 'banana', 'cherry', 'orange', 'Kiwi', 'Melon', 'Mango')
print(thisTuple[1])#Me arroja el SEGUNDO elememento, indice 1

'''
Indexacion negativa
'''
print(thisTuple[-1]) # Me tre el primer elemento contando de derecha a izquierda

'''
Rango de indices
'''
print(thisTuple[2:5])
'''
Cabe destacar al iniciar el conteo lo hace por indice y
finalizar, cuenta los elementos por elementos y no por indice. 
'''
print(thisTuple[:4]) # finalizar
print(thisTuple[2:]) #Iniciar

'''
Rango de indices negativos
'''
#De esta manera los cuenta por elementos, es decir da las posciones de los elementos mas no 
print(thisTuple[-4:-1])

'''
Comprobar sik el articulo existe
'''
if 'apple' in thisTuple:
    print('Yes, apple is in the tihislist tuple')