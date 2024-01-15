from collections import namedtuple
'''namedtuples: Convierte las tuplas en contenedores. '''


print('-- Convertir tuplas a Diccionarios')
'''Creamos la tupla.
* El primer valor es el nombre de ella(Tupla tipo diccionario)
* El segundo es el nombre de los indices de los elementos
'''
# Creamos el namedtuple. Solo acepta dos argumentos
Animal = namedtuple('Animal', 'nombre edad tipo dueño')
# Creamos el objeto de tipo diccionario con tuplas
perry = Animal(nombre='Perry', edad=15, tipo='Cat', dueño='Luis')
# Imprimimos la tupla
print(perry)
# Podemos acceder a los indices por medio del nombre de ella
print(perry.nombre)  # Accedemos atraves de una de las llaves
print(perry.tipo)  # Acedemos atraves de las llaves tipo
print(perry[0])  # Tambien se puede acceder atraves de los indices
'''NOTA: No es necesario usar los indices, ya que se puede
acceder atraves de las keys. Aparte son mas ligeras, aparte
los atributos de las tuplas son inmutables'''


print('-- Convertir en un diccionario')
# convertimos la tupla en un diccionario
Pc = namedtuple('Pc', 'modelo marca')
ordenador = Pc(marca='Hp', modelo='Pentium')
print(ordenador._asdict())  # Convertimos named tuple a un diccionario
print(f'Retornamos una tupla con el nombre de los compos: {ordenador._fields}')


print('-- Ejemplo de una namedtuple en una lista')


Persona = namedtuple('Persona', ['nombre', 'edad'])
personas = [Persona('alice', 26), Persona('Luis', 26)]
# Imprime de tal manera de como se le pasaron los datos
print(personas)
# Mostramos de tal manera unos datos estructurados
for persona in personas:
    print(f'Nombre: {persona.nombre}\tEdad: {persona.edad}')
