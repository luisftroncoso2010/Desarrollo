import inspect
import modulo_inspect
from pprint import pprint


print('-- Mostramos todo lo que contiene el modulo')


# Usamos getmembers. Muestra todo lo del modulo
for name, data in inspect.getmembers(modulo_inspect):
    if name.startswith('__'):
        continue
    print(f'{name} : {data}')


print('-- getmembers()')
# Obtiene todo lo de objeto incluyendo clases y objetos
pprint(inspect.getmembers(modulo_inspect.A), width=65)


print('-- getmembers() metodos de una Clase. Clase A')


# Metodo y funciones de una clase
pprint(inspect.getmembers(modulo_inspect.A, inspect.isfunction))


print('-- getmembers() metodos de una Clase. Clase B')


# Metodo y funciones de una clase
pprint(inspect.getmembers(modulo_inspect.B, inspect.isfunction))


print('-- Inspeccion de instancias')


# Devuelve todos los metodos y atributos para el uso de las instancias
# Creamoa una instancia y le asignamos un nombre
a = modulo_inspect.A(name='inspect_getmembers')
''' Usamos el metodo getmembers para obtener
los atributos y metodos de la instancia de a.
NOTA: ismethod reconoce las dos instacias vinculadas a A'''
pprint(inspect.getmembers(a, inspect.ismethod))


print('-- getmembers() y insclass()')


# Omitimos todo los otro y solo imprimimos las clases
for name, data in inspect.getmembers(modulo_inspect, inspect.isclass):
    if name.startswith('__'):
        continue
    print(f'{name} : {data}')

print(f'Modulo: {inspect.ismodule(modulo_inspect)}')
print(f'Clase: {inspect.isclass(modulo_inspect)}')
print(f'Funcion: {inspect.isfunction(modulo_inspect.module_level_function)}')
print(f'Metodo: {inspect.ismethod(modulo_inspect.A.get_name)}')
print(f'built-in: {inspect.isbuiltin(modulo_inspect)}')
print(f'Funcion o Metodo: {inspect.isroutine(modulo_inspect)}')
