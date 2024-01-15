from enum import Enum, unique
from collections import namedtuple
import json
''' Enum: Trabaja con conjuntos de valores predefinidos '''

print('-- Ejemplo dias enum')


class Dias(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7


print(Dias.LUNES)
print(Dias.MARTES.value)

# Serializacion con un json
diasJson = json.dumps(Dias.LUNES, default=lambda x: x.value)
print(diasJson)

# Acceder a los miembros por nombre
print(Dias.LUNES)  # Salida: Dias.LUNES

# Acceder al valor de un miembro
print(Dias.MIERCOLES.value)  # Salida: 3


print('-- Ejmeplo enum y namedtuple')


# asegura que los valores que tengan asignados sean unicos.
@unique
class Especies(Enum):
    gato = 1
    perro = 2
    lobo = 3
    mariposa = 5
    buho = 6
    # usando alias
    gatito = 7
    perrito = 4


Animal = namedtuple('Animal', 'name age type')
perry = Animal(name='Perry', age=31, type=Especies.gato)
print(perry)
atena = Animal(name='Atena', age=25, type=Especies.gato)
print(atena)
