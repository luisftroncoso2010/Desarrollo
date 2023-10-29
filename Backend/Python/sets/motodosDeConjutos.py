'''
Algunos de los metodos de conjuntos mas usados
'''
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

print('--difference_update--')
#Trae las diferecias que tiene el uno y no el otro
set1 = {1, 4, 6, 7, 'luis'}
set2 = {'ana', 'luis', 1, 'pedro'}
set1.difference_update(set2)
print(set1)

print('--discard()--')
#Remueve el elemnto pasado por parametro, si no esta no hace nada ni devuelve una ecepsion
setDiscard = {1, 2, 3}
setDiscard.discard(0)
print(setDiscard)

print('--intersection()--')
#Muestra los elementos que se comparten en ambos sets
setIntersectionUno = {1, 2, 3, 'ana'}
setIntersectionDos = {'ana', 'elena', 1, 2}
updateIntersection =setIntersectionDos.intersection(setIntersectionUno)
print(updateIntersection)

print('--intersection_update()--')
#Muestra los elemenos que estan en ambos conjuntos
setIntersection_updateUno = {1, 2, 'ana', False}
setIntersection_updateDos = {1, 2, 'ana'}
setIntersection_updateUno.intersection_update(setIntersectionDos)
print(setIntersection_updateUno)

print('---isdisjoint()---')
#Devuelve True si son sets TOTALMENTE DIFERENTE
setIsdisjointUno = {1, 2}
setIsdisjointDos = {3, 4, 5}
updateIsdisjoint = setIsdisjointUno.isdisjoint(setIsdisjointDos)
print(updateIsdisjoint)

print('--issubset()--')
#Devuelve TRUE si todos los elementos del A estan en B (Subconjuto)
setIssubsetUno = {"a", "b", "c", "d"}
setIssubsetDos = {"f", "e", "d", "c", "b", "a"}
updateissubset = setIssubsetUno.issubset(setIssubsetDos)
updateissuperset = setIssubsetDos.issuperset(setIssubsetUno)
updatesymetryc_difference = setIssubsetUno.symmetric_difference(setIssubsetDos)
setIssubsetUno.symmetric_difference_update(setIssubsetDos)
print(f'issubset() subconjuto:  {updateissubset}')
print(f'issuperset() superconjunto: {updateissuperset}')
print(f'symetric_difference() Elementos que no se comparten: {updatesymetryc_difference}')#Este y el de abajo don practicamente igual
print(f'symmetric_difference_update(): Elimina todo lo repetido en A y B: {setIssubsetUno}')