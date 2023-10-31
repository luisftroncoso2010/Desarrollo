'''
Cambiar elementos de un diccionario
'''
thisDict = {
    'Brand': 'Ford',
    'Model': 'Mustag',
    'Year': 1964
}
'''
cambiamo los valores de un diccionario
'''
print('Asi lo cambiamos de manera arbitraria')
thisDict['Year'] = 2023
print(thisDict) 

print('--Actualizamos un valor con el metodo update()--')
thisDict.update({'Year': 1997})
print(thisDict)

print('--Agregamos un llave/valor añ diccionario--')
thisDict['Color'] = 'Green'
print(thisDict)