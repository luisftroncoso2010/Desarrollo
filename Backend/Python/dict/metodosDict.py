'''
Diccionarios anidados
'''
print('--Primer diccionario anidado--')
myFamily = {
    'Child1':{
        'name': 'Emil',
        'year': 2004
    },
    'Child2': {
      'Name': 'Tobias',
      'Year': 2007  
    },
    
    'Child3': {
        'Name': 'Luis',
        'Year': 2011    
    }        
}
print('--Copiar un diccionario--')
copyDict = myFamily.copy()
print(myFamily)

print('--Fromkeys()--')
fromkeysDict = dict.fromkeys(myFamily, True) #crea diccionarios vacios apartir de sus llaves y se le asigna el valor manual
print(fromkeysDict)

print('--Medo get()--')
getDict = myFamily.get('Child3')#trae el valor especificado y si no es el vasado devuelve none
print(getDict)

print('--items()--')
itemsDict = myFamily.items()#muestra todos los diccionarios del anidado
print(itemsDict)

print('--Keys()--')
keisDict = myFamily.keys()
print(keisDict)#Devuelve todas las keys
print(type(keisDict))

print('--Pop()--')
popKeys = myFamily.pop('Child1')#Resive un arguemnto para poder eliminar
print(myFamily)

print('--Elimina el ultimo elemento del diccionario--')
myFamily.popitem()#elimina el ultimo elemento del diccionario
print(myFamily)

print('--setdefault()--')
setdefaultDict = myFamily.setdefault('Child', True)
print(myFamily)

print('--update()--')
updateDict = myFamily['Child2'].update({'Name': 'Fernando'})
print(myFamily)#Actualiza el list/diccionario

print('--Values()--')
valuesDict = myFamily.values()#Devuelve los valores
print(valuesDict)
