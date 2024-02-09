'''Nuevos estilos de clases'''


print('-- Old class')


# Creamos la clase antigua
class Oldclass():
    def __init__(self):
        print('I am an old class')


# Creamos la clase antigua
class NewClass(object):

    def __init__(self):
        print('I am ajazzy new class')


# Instanciamos la vieja clase y la imprimos, y la clase nueva
old = Oldclass()
new = NewClass()
