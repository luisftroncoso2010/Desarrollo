'''
Iterar diccionarios
'''
thisDict = {
    'Brand': 'Ford',
    'Model': 'Mustang',
    'Year': 2023
}
print('--Muestrame todos los elementos del dicionario--')
for x in thisDict:
    print(x) #Memuestra solo las llaves solo sin valor
    
print('--Manera de iterar los valores una por una')
for i in thisDict:
    print(thisDict[i])
    
print('--Devolvemos los valores con el metodo values--')
for x in thisDict.values():
    print(x) #Devuelve los valores de un diccionario

print('--Devolvemos las calves de un diccionario')
for i in thisDict.keys():
    print(i)

print('--Devolvemos llaves valor--')
for x, y in thisDict.items():
    print(f'Llave: {x} y Valor {y}')