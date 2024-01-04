''' Decoradores: Son funciones que modifican la
funcionalidad de otras funciones y ayudan a hacer
el codigo mas corto '''


print('-- Todo es un objeto en python')


def hola(nombre='Covadonga'):
    return 'Hola ' + nombre


# Imrpmios hola
print(hola())
# Podemos asignar una funcion a una variable
saluda = hola  # No usamos los parantesis por queno la estamos
# llamando solo asignarla a una varaible

# Deboemos colocarlo los parentesis
# para que entienda que es una variable de funcion asignada
print(saluda())
# Eliminar la funcion asginada
del hola  # Eliminara la funcion asignada a la variable con el del
# print(hola()) # Salida: NameError.. (Esta eliminada)


print('-- Definir funciones dentro de funciones (Funciones anidadas)')


def hi(nombre='Covadonga'):
    print('Estas dentro de la función hola()')

    def saluda():
        return 'Estas dentro de la funcion saluda()'

    def bienvenida():
        return 'Estas dentro de la función bienvenida()'

    print(saluda())
    print(bienvenida())
    print('De vuelta a la función hi()')


hi()


print('-- Devolviendo funciones dentro de funciones')


# Creamos la funcion
def hii(nombre='Covadonga'):
    # Creamo bfunciones dentro de otras funciones
    def saluda():
        return 'EStas dentro de la funcion saluda()'

    def bienvenida():
        return 'Estás dentro de la función bienvenida'

    # Si el nombre es igual al que esta definido en la funcion prinmcipal
    if nombre == 'Covadnga':
        # Rotrna
        return saluda
    else:
        return bienvenida


a = hii()
print(a())  # Aca de debe colocar los parentesis a la variable
# que contiene la funcion para que la entienda como funcion en si


print('-- Usando funciones como funciones de otras')


# Creamoa la funcion que se le pasará por parametro a la otra
def saludar():
    return 'Hola luis. Funcion saludar'


def hasEstoAntesDeSaludar(func):
    print('Hacer algo abeste de llama a func')
    print(func())


# Llamamos a la funcion
hasEstoAntesDeSaludar(saludar)
