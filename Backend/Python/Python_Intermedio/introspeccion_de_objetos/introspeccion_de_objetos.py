import inspect
''' Introspeccion de objetos: Se refiere a la capacidad de examinar
un objeto para determinar tu tipo y obtener informacion sobre
sus propiedades, métodos y atributos en tiempo de ejecucion
'''

print('-- type(), isintance()')


x = 5
print(f'Validar el tipo de variable: {type(x)}')
print(f'De que tipo de instacia es: {isinstance(x, int)}')


print('-- dir()')


lista = [3, 5, 1]
print(f'Nombre de atributos y metodos de un objeto: {dir(lista)}')


print('-- help()')


cadena = 'Hola, mundo'
'''Ayuda para cadena'''
help(cadena)


print('-- id()')


nombre = 'Pelayo'
# Identificador unico de cada objeto
print(f'Identificador unico de cada objeto: {id(nombre)}')


print('-- Módulo inspect')

print(inspect.getmembers(str))


def ejemplo_inspect(parametroUno, parametroDos='Valor por defecto'):
    return parametroUno + parametroDos


print(inspect.signature(ejemplo_inspect))


print('-- __dict__')


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona = Persona('Luis', 30)
# Mapea nombres de atributos y valores
print(persona.__dict__)
