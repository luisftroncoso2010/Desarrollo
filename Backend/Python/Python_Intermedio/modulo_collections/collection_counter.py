from collections import Counter
'''El uso de counter: Nos permite contar el número de elementos
que una llave tiene.'''

print('-- Uso del counter')


colores = (
    ('Covadonga', 'Amarillo'),
    ('Pelayo', 'Azul'),
    ('Xavier', 'Verde'),
    ('Pelayo', 'Negro'),
    ('Covadonga', 'Rojo'),
    ('Amaya', 'Plata')
)

favoritos = Counter(name for name, colours in colores)
print(favoritos)

print('-- Contar valor de un diccionario de manera normal')
# Tu diccionario
colours_ = {'Rojo': 180,
            'Amarillo': 70,
            'Azul': (160, 140, 754),
            'Verde': {750, 740, 800},
            'Naranja': (180, 178, 60),
            'Negro': [500, 400],
            'Blanco': 100,
            'Gris': 400}

'''for llave, valor in colours_.items():
    tuple_.append(tuple_(valor))'''

for llave, valor in colours_.items():
    if isinstance(valor, tuple):
        print(f'La clave {llave} tiene {len(valor)} valores')
    if isinstance(valor, list):
        print(f'La clave {llave} tiene {len(valor)} valores')
    if isinstance(valor, set):
        print(f'La clave {llave} tiene {len(valor)} valores')
    else:
        print(f'La clave {llave} tiene UN valor')
