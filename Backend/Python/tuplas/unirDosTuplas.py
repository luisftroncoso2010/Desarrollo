''''
Unir TUPLAS 
'''

tupleUno = ('a', 'b', 'c')
tupleDos = (1, 2, 3)
tupleTres = tupleUno + tupleDos # Se unen las dos tuplas
print('---Unir tuplas---')
print(tupleTres)
print(type(tupleTres))#Se valida el tipo de coleccion

'''
Multipllicar las tuplas
'''
print('---Multiplicar las tuplas---')
myTuple = tupleUno * 2
print(myTuple)
tupleDos *= 2 
print(tupleDos)

'''
Metodos de tuplas
'''
tupleCuatro = 100, 200, 300, 400
print('---Metodos de tuplas---')
 
print(tupleCuatro.count(100)) #Cuantas cuantas vecesta el numero 100
print(tupleCuatro.index(200)) #decuelve la poscion donde esta elemento
print(len(tupleCuatro)) #Cuenta cuantas elementos hayen la tupla  