'''
Accdeder a un elemento
'''
thisSets = {'apple', 'banana', 'cherry'}

print('---Mostrar elementos con un ciclo---')
for i in thisSets:
    print(i)
    
print('---Comprobar si un elemento especifico esta presente en conjunto---')
print('banana' in thisSets) #Devielve un valor bool

print('---Agregar uno o varios elementos a un sets---')
mySetsUno = {1, 2, 3}
mySetsdos = [6, 7]
mySetsUno.discard(0)#Elimina un elemento si lo encontra y si no, no pasa nada
mySetsUno.add(4)
mySetsUno.update(mySetsdos)#Agrega un conjunto a otro, cualquier iterable
print(mySetsUno)