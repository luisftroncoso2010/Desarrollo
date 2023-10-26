'''
Creacion de conjuntos.
Se impliemntan usando la clase set()
Los valores en los conjuntos no se repiten
'''
conjunto1 = {1, 2, 3}
conjunto2 = set([1, 2, 3, 3]) #Solo me muesta un solo valor, no el repetido
print(conjunto2)
'''
Metodos de conjunto
'''
conjunto1.add(4); #Se añade un elemento al conjunto
print(conjunto1)

conjunto1.remove(2) #Mandara error si elemento no existe en el conjunto
print(conjunto1)

conjunto2.discard(0) #Si el elemento no exite no mostrara error, si se generara nada. Si existe lo eliminara
print(conjunto2)

conjunto1.pop()# Elimina el primer elemento
print(conjunto1)

conjunto2.clear() #Elimona todos los elementos del conjunto
print(conjunto2)

'''
Operacion de conjuntos
'''
conjunto3 = {6, 2, 3, 11}
conjunto4 = {3, 6, 4, 10, 2, 5, 15}

print('---Une los conjuntos y los ordena de manera ascendente---')
union = conjunto3 | conjunto4
print(union)

print('---Interseccion. Solo muestra el valor repetido---')
interseccion = conjunto3 & conjunto4
print(interseccion)

print('--- Diferencia (Muestra los elementos que faltan entra uno y el otro)---')
diferencia = conjunto3 - conjunto4
print(diferencia)

print('--- difernecia simetrica (Muestra los elementos que no son repetidos)---')
diferencia_simetrica = conjunto3 ^ conjunto4
print(diferencia_simetrica)

