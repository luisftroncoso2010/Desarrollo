'''Funciones Lambda'''

# Funcion suma (Basica)
suma = lambda x, y: x + y
print(f'Usamos la funcion lambda: {suma(5, 5)}')


print('-- Ordenar una lista')
a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])
print(f'La lista ordenada es: {a}')


print('-- Ordenar las lista paralelamente')
listaUno = [(1, 2), (4, 1), (9, 10), (13, -3)]
listaDos = [(2, 2), (4, 1), (9, 10), (13, -1)]
datos = list(zip(listaUno, listaDos))
datos.sort()
listaUno, listaDos = map(lambda t: list(t), zip(*datos))
print(f'Lista uno: {listaUno}')
print(f'Lista Dos: {listaDos}')
