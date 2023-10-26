'''
Las tuplas los ninmutables.
SOLO SI SE CONVIERTE A LISTA Y LUEGO SE VUELVE CONVERTIR A TUPLA
'''
thisTuple = ('apple', 'banana', 'cherry')
turnTuple = list(thisTuple) #Se convertir de tupla a lista
print(type(turnTuple)) #Mostramos el tipo de coleccion
turnTuple[1] = 'kiwi' #Se posciona en la poscion indicada, rempalza le valor que tenia antes de.
turnTuple.append(True)#Se arega el valor ne la ultima posicion de la tupla 
print(turnTuple)
turnTuple.insert(0,10) #Se inserta un elemento a la lista (tupla) se indica la poscion y el valor que se le dará
print(turnTuple)
thisTuple = tuple(turnTuple) # Se vuelve a pasar la lista a tupla
print(type(thisTuple)) #Se imprime el tipo de dato

'''
Agregar una tupla a una tupla
'''
thisTupleDos = ('apple', 'banana', 'cherry')
add_ = ('orange',)#NOTA: Recuerda para que un SOLO elemente se considere una tupla se debe agregar la coma

thisTupleDos += add_
print(thisTupleDos)

'''
NOTA: No se puede eliminar un elemento de uan tupla.
PERO se puede eliminar uno cambiando latupla a lista (tuple() a list()), 
ahi si se aplica el metodo remove() y como parametro el elemento, 
ya sea de tipo string, int, float o bool o se puede eliminar la tulpa 
completa usando el metodo del EJMPLO...
'''
del thisTupleDos
print(thisTupleDos) # Me manda un error "is no defined" por que ya a sido borrada antes de eliminar