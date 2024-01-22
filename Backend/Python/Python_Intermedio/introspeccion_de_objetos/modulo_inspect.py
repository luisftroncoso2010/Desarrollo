# Primer comentario del modulo


'''Creamos este modulo de prueba para trabajarlo
con el modulo inspect  '''


def module_level_function(arg1, arg2='default', *args, **kawargs):
    local_varible = arg1 * 2
    return local_varible


def ejemplo_funccion(arg: int, argDos: str = 'default') -> float:
    return 3.14


'''Modulo inspect'''


class A(object):
    '''Estas en la clase A'''
    def __init__(self, name):
        self.name = name

    def get_name(self):
        '''Metodo get_name clase A'''
        return self.name


instance_of_a = A('sample_instance')


# El modulo inspec. Creando clase
class B(A):
    '''Estas en el inicio de la clase B, que heradade A'''

    def do_something(self):
        '''Esta en B no en A'''
        pass

    # Comentarios prefijos del metodo. Calase B, metodo get_name
    def get_name(self):
        '''Metodo get_name de la clase B'''
        return f'B({self.name})'
