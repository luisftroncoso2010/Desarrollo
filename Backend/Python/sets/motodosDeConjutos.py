'''
Algunos de los metodos de conjuntos mas usados
'''

import configparser


print('agregar un elemento al conjunto')
mySetsUno = {1, 2, 3, 4}
muySetsDos = {2, 3, 4, 5, 6}
mySetsUno.add(7)#agrega el numero 7
print(mySetsUno)

print('---Remueve un elemenento indicado---')
mySetsUno.remove(1)#Remueve le numero dos
#Dado el caos qued el elemntos no exista mandata una ecepsion
print(mySetsUno)

print ('---elimina un elemento---')
mySetPop = {4, 1, 2, 3}
mySetPop.pop()#Elimina el elemneto de menor valor de tipo int
print(mySetPop)
mySetPopString = {'Berta', 'Ana', 'Didier', 'Carlos'}
mySetPopString.pop()#Elimina cualquier string
print(mySetPopString)

print('---Clear. Elimina todos los elementos de la lista---')
mySetClear = {1, 2, 3}
mySetClear.clear()#Solo muestra la palabra set, es decir el tipo de coleccion
print(mySetClear)

print('---Copy. Copiar un conjunto---')
mySetCopy = {'ana', 'berta', 'amparo'}
setCopy = mySetCopy.copy()
print(setCopy)#Muestra la copy

print('---Union(iterable. Union de dos conjuntos) ')
mySetUnionUno = {1, 2, 3}
mySetUnionDos ={3, 4, 5}
#Creaun nuevo set y elimina los repetidos
setUnion = mySetUnionUno.union(mySetUnionDos)
print(setUnion)
print(type(setUnion))

print('---Diferencia. Diferencia de dos conjuntos---')
mySetDifferencesUno = {1, 2, 3, False, True, 'ana'}
mySetDifferencesDos = {1, 2, 'berta', 'luis', False}
#Muetra el valor que esta en el set uno y no en el dos
differences = mySetDifferencesUno.difference(mySetDifferencesDos)
print(differences)

print('---issubset. Muestra si A es un subconjunto de B---')
#Devuelve un vlaor booleano
print(mySetDifferencesDos.issubset(mySetDifferencesUno))
