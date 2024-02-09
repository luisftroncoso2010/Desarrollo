'''Metodos Especiales'''


# Creamoas la clase. APra usar metodos especiales
# double underscore
class GetTest(object):
    # Constructor de la clase
    def __init__(self):
        self.info = {
            'name': 'Covadonga',
            'country': 'Austrias',
            'number': 123456789
        }

    # Creamos el metodo getitem, se le coloca
    # un parametro tipo iterable o suscriptable
    def __getitem__(self, i):
        return self.info[i]


# Instanciamos la clase
foo = GetTest()
print(foo['name'])
print(foo['country'])
