'''
Eliminar elementos de un diccionario
'''
thisDict = {
    'Brand': 'Ford',
    'Model': 'Mustang',
    'Year': 2023
}

#Agregamos un elemento al dict
thisDict['Color'] = 'Red'
thisDict.update({'Placa': 'XXCV12', 'Tecno': True})

print('--Eliminamos elementos del diccionario (Por llaves)--')
thisDict.pop('Model')#Se debe pasar un argumento (LLva del dict)
print(thisDict)

print('--Elimina un elemento de manera aleatoria--')
thisDict.popitem()
print(thisDict)

print('--eliminamos un elemento de la lista--')
del thisDict['Color']
print(thisDict)

print('--vaciamos el elemento por completo. Clear()--')
thisDict.clear()
print(thisDict)

print('--Eliminamos el diccionario por completo--')
del thisDict
print(thisDict) #Me dira que no esta definido