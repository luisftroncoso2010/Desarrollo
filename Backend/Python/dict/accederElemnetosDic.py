'''
Accdeder a lso elementos de un diccionario
'''
thisDict = {
    'Brand': 'Ford',
    'Model': 'Mustag',
    'Year': 1964
}
print('---Accedemos al valor de un elemento---')
modelDict = thisDict['Model']#Accedemos por su valor, direccto 
print(modelDict)
modelDict = thisDict.get('Model')#Manda vacio si no lo encuentra
print(modelDict)

print('--Obtener las claves del diccionario--')
keysDict = thisDict.keys()
print(keysDict)

print('--Agregamos una clave al diccionario con valor--')
thisDict['Color'] = 'red'
print(thisDict)

print('--Obtenemos todos los valores del diccionario--')
valuesDict = thisDict.values()
print(valuesDict)

print('--Obtener obtener articulos--')
itemsDict = thisDict.items()#Devuelve llave/valor en una lista de tuplas
print(itemsDict)

print('--Comprobar si la lista existe--')
if 'Model' in thisDict:
    print('Yes, Model in one of the keys in the thitsdict dictionary')
    
