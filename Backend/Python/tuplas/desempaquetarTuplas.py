'''
Desempaquetar tuplas.
Cuando se cre la tupla de mantiene empaquetada, esdecir "empaquetar"

Asigna valores individuales a una secuencia
'''
fruits = (1, 2, 3, 4)
(cherry) = fruits
print(type(cherry))

miTuple = (5, 10, 15, 20, 25)
primero, segundo, *resto1 = miTuple
print('---Primero---')
print(primero)
print('---Segundo---')
print(segundo)
print('---Resto---')
print(resto1)

miTuple2 = (50, 55, 60, 70, 80)
*resto2, ultimo2 = miTuple2

print('---Resto---')
print(resto2)
print('---Ultimo---')
print(ultimo2)