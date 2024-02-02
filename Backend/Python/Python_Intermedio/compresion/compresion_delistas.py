'''Compresion de listas'''


print('-- Compresion de listas. Ejmplo: 1')


multiples = [i for i in range(30) if i % 3 == 0]
print(f'Lista de multiples de 3: {multiples}')


print('-- Diccionarios compresion')


mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}


# Creamos un nuevo diccionario y sumamos dos llaves
mcase_frequency = {
    # Es cogemos una llave y le asignamos un valor.
    # Ya sea minuscula o mayuscula
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}
print(f'Nuevo diccionario: {mcase_frequency}')
otra = {v: k for k, v in mcase.items()}
print(f'-- Invertimos llave/valor:\n{otra}')


print('-- Set de compresiones')


# Exponente a la 3
squared = {x**3 for x in [1, 1, 2]}
print(f'-- Set. Numeros al cubo:\n{squared}')


print('-- generator Compresions')


# Generadores. Almacenados en tupla. solo se generan cuando se necesita
multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)

for x in multiples_gen:
    print(x, end=' ')
