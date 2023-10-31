'''
Copiar diccionarios
'''
thisDict = {
    'Brand': 'Ford',
    'Model': 'Mustang',
    'Year': 2023
}

print('--Copiar ccionarios--')
myDict = thisDict.copy()#copia todo el diccionario
print(myDict)

print('--Otra manera de hacer una copia es hacer la funcion dict()--')
myDictDos = dict(thisDict)
print(myDictDos)
