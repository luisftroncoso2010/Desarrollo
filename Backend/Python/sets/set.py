'''
thisSets.
Tipo de coleccion desordenada, no indexada 
y mutable (atraves de los metodos add(), remove()).
Los set NO muestran valores repetidos
'''
print('---Primer sets---')
'''
NOTA: Los valores True y False se consideran en el sets
1 y 0 respectivamente. Solo motrara el elemento que 
en una poscision de primera
'''
thisSets = {2, True,  False, 0,  1, 5, 4, 4, 5} #No muestra valores repetidos
print(sorted(sorted(thisSets))) #Solo ordena la duncion de un solo tipo de valor 
print(type(thisSets))

print('---Creando un SETS con su misma funcion set()')
thisSetsDos = set(('apple', 'Luis', 'barco'))
print(thisSetsDos)
print(type(thisSetsDos))

print('---Obtener la longitud de elementos del set---')
print(len(thisSetsDos)) #Tiene 3 elementos

print('---Agregar elementos al set---')
thisSetstres = set(('ana', 1, False))
print(thisSetstres)
thisSetstres.add(4) #solo agrega un solo elemento
print(thisSetstres)