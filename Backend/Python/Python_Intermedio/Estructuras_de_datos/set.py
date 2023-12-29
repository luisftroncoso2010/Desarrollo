'''Los sets se comportan como las listas, con la diferencia
de que no pueden contener elementos duplicados. Tambien son
inmutables y una vez definidos sus elementos no se pueden
modificar '''


print('-- Sets')
conjunto_numeros = {1, 1, 2, 5, 6, 3, 4}
conjunto_letras = {'a', 'b', 'e', 'd', 'g', 'z', 'a', 'b'}
print(conjunto_numeros)
print(conjunto_letras)


print('-- set. Lista con duplicados o no')
# Creamos una lista de duplicados
lista_letras = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# Creamos una lista vacia para almacenar los duplicados
duplicados = list()
for value in lista_letras:  # Recorremos la lista con los duplicados
    if lista_letras.count(value) > 1:  # Contalos los valores que son mayores a uno
        # Se valida si dicho valor no esta en la lista duplicados
        if value not in duplicados:
            duplicados.append(value)  # Se añade a la lista vacia


print(f'Lista de letras duplicadas: {lista_letras}')
print(f'Lista de duplicados de letras: {duplicados}')


'''Forma simple, para eliminar duplicados'''
# Se crea uan compresion de listas y se almacena un set() para que no se repita
_duplicados = set([x for x in lista_letras if lista_letras.count(x) > 1])
print(_duplicados)  # Mostramos la lista solamente de los valores duplicados


'''Los sets tambien tienen otros métodos, vemos algunos a
continuación. '''
print('-- Interseccion y Diferencia de sets')
set_uno_colores = set(['amarillor', 'rojo', 'azul', 'verde', 'negro'])
set_dos_colores = set(['rojo', 'marron'])
# Muestra el repetido. Elemento que esta en ambos conjuntos
print(set_dos_colores.intersection(set_uno_colores))
# Muestra el elemento que solo esta en un conjunto
print(set_dos_colores.difference(set_uno_colores))



