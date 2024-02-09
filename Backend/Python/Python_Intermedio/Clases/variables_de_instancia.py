'''Variables de instancia y clase'''


print('-- Variables de clase, que no tienen inconvenientes')


# Creamos la clase:
class Cal(object):
    # Pi es una variable de clase
    pi = 3.142

    def __init__(self, radio):
        # self.radio es una variable de instancia
        self.radio = radio

    def area(self):
        return self.pi * (self.radio ** 2)


# Instanciamos la clase, le pasamos un parametro y creamoa el objeto
a = Cal(32)
# Imprimimos el calculo del radio
print(f'El radio del Circulo es: {a.area()}')
# Imprimimos pi
print(f'Imprimos pi: {a.pi}')
# Calculamos el area
b = Cal(44)
print(f'El area de B es: {b.area()}')
# Imprimomos pi
print(f'Imprimos pi con b: {b.pi}')


print('-- Aca veremos como las variables de')
print('clase e instancias pueden causar problemas --')


# Creamos la clase
class SuperClass(object):
    superpowers = []

    # Creamos el constructor
    def __init__(self, name):
        self.name = name

    # Creamos el metodo
    def add_superpower(self, power):
        self.superpowers.append(power)


# Creamos la clase y le pasamos un parametro
foo = SuperClass('foo')
bar = SuperClass('Bar')
print(f'Foo: {foo.name}')
print(f'Bar: {bar.name}')

'''Nota: Aca las variables de clase, cambian por echo de que
echo de que es una lista, dado que'''
foo.add_superpower('Fly')
print(f'Usamos instancia bar: {bar.superpowers}')
print(f'Usammos instancia foo: {foo.superpowers}')
