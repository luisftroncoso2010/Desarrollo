from collections import defaultdict
import json


print('-- Iteracion de una tupla de tuplas normal')
# Cramos una tupla con colores
colours = (
    ('Austias', 'Ovioedo'),
    ('Galicia', 'Ourense'),
    ('Extremadura', 'Cáceres'),
    ('Austrias', 'Gijón'),
    ('Cataluña', 'Barcelona'),
    ('Cataluña', 'Madrid'),
)
# Imprimimos la lista de manera normal
for i in colours:
    # Liberamos las tuplas, es decir imprimimos una por una
    for j in i:
        print(j)


print('-- Uso de collections')
# Ahora usaremos el defauldict
ciudades = defaultdict(list)  # Cremaoa una lista vacia con defaultlist

# Iteramos la tupla colours
for name, colour in colours:
    # Añadimos clave [name] valor =colour
    ciudades[name].append(colour)
''' Si ve un valor con una clave igual,
añade dicho valor a esa clave (lista)'''
print(ciudades)

print('-- Creamos un funcion lambda')


# Estructura de datos aninada. Por cada llamada
def tree():
    return defaultdict(tree)


# Esta funcion lambda, no es recomendado
'''default_dict = lambda: defaultdict(default_dict)'''
# Cre
default_dict = defaultdict(tree)
some_dict = default_dict
some_dict['region']['ciudad'] = "Oviedo"
some_dict['departamentos']['ciudad'] = 'Medellin'
# Aca lo primprimimos tipo json
print(json.dumps(some_dict))


print('-- creamos un diccionario')
_some_dict = {'Region': {'Caribe': ['Atlantico', 'Bolivar', 'Magdalena']},
              'Paises': {'Colombia': ['Leticia', 'Caldas', 'Caquetá']}}

_some_dict['Region']['Caribe'].append('La guajira')
print(_some_dict)


print('-- Uso del defaultdic metodo interno')


# Usando un metodo __missing__
d = defaultdict(lambda: 'Not Present')
d['a'] = 1
d['b'] = 5


print(d['a'])
print(d['b'])
print(d['v'])
