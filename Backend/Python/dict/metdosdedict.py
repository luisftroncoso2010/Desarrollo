''''
Metodos de dict
'''
diccionario = {
    'Nombre': 'lucas',
    'Apellido': 'Dalto',
    'Subs': 100000
}
#Devuelve las claves. Tambien nos sirve para iterar
claves = diccionario.keys()
print(claves)

#Devuelve el valor de la clave que se le pida
getClaves = diccionario.get('Nombre')
print(getClaves)

#Si buscamos la clave de esta maenra y no la encuentra mandara una exepcoion y con el metodo get() NO!. el programa continua
searchClavesCorchetes = diccionario['Apellido']
print(searchClavesCorchetes)

itemsDict = diccionario.items()
print(itemsDict)
print(type(itemsDict))

popDict = diccionario.pop('Apellido')
print(popDict)
print(diccionario)

#elimina todos elementos del diccionario. Devuelve vacio
clearDict = diccionario.clear()
print(clearDict)
