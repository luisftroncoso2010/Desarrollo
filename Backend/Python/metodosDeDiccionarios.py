diccionario = {
    'Nombre': 'Lucas',
    'Apellido': 'Dalto',
    'Subs': 1000
}
claves = diccionario.keys(); #Trae las claves del diccionario
#Trae la llave del un valor en un diccionario y no manda excepcion
claves2 = diccionario.get('Nombre')
print(claves2)
#Elimina todo del diccionario
#diccionario.clear() <-
#Eliminamos elementos del diccionario
#diccionario.pop('Dalto') #Elimina la llave. Si se le pasa el valor de la llave perdera el valor
diccionario.items() #Se usa mas que todo para iterar sobre el diccionario
print(diccionario)