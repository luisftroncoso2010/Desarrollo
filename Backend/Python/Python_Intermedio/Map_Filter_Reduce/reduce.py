from functools import reduce
'''Reduce: Cuando queremos relizar cierta operaciones sobre
una lista y devolver los resultados. '''


print('-- Realizar reduce a cierta operaciones')
producto = 1  # Uniciamos el valor en 1 para poder almacenarlo
lista = [1, 2, 4, 6]  # Creamos la lsita que se multiplicara en uno
for num in lista:  # Recorremos la lista
    producto *= num
print(producto)
# Multiplicamos todos los elementos de la lista
_producto = reduce((lambda x, y: x * y), lista)
print(_producto)
