'''
Eliminar cuaquier elemento del conjunto
metodos remove(), discard(), pop() clear() y del
'''
thisSet = {'apple', 'banana', 'cherry'}
print('--Metodo Remove--')
thisSet.remove('apple')#Si no encuentra el elemento manda ecepcion
print(thisSet)

print('--Metodo discard--')
thisSet.discard('apple')#Si no lo encunetra no pasa nada
print(thisSet)

print('--Metodo Pop--')
thisSet.pop()#Elimina cualquier elemento al azar del iterable
print(thisSet)
thisSetUpdate = {'baloto', 'colombia', 'Argentina'}
thisSet.update(thisSetUpdate)

print('--Metodo clear--')
thisSet.clear()#Elimina todos los elemntos del set
print(thisSet)

print()

print('--Metodo del--') #eliimna el conjunto completo
del thisSet
print(thisSet)#Muestra error 'thisSet is not definido'



