'''Programacion Funcional: Es un paradigma de la
programacion, se centra en el uso de funciones y
expresiones inmutables para construir programas.'''


print('-- Funciones como objetos')


def cuadrado(x):
    return x ** 2


# Almacenamos la funcion en la variable f,
# para que esta la lea como funcion
f = cuadrado
print(f(2))


print('-- Funciones anonimas lambda')


# La alerta que nos arroja es pro que no es una buena practica
# asignar a una variable una  funcion lambda, en estos
# casos es mejro usar una funcion normal def
cuadrado_lambda = lambda x: x ** 2
resultado = cuadrado_lambda(5)
print(resultado)


print('-- Compresion de listas')


# Ejemplo uno
lista = list([1, 2, 3, 4])
_cuadrados = [x ** 2 for x in lista]
print(_cuadrados)


# Ejemplo Dos. Lusta de tuplas
frutas = ['manzana', 'platano', 'uva']  # Creamos la lista
# Creamos una lista, por compresion de lista.
tuplas = [(fruta, len(fruta)) for fruta in frutas]
print(tuplas)


print('-- Inmutabilidad')


# Ejemplo con tuplas
tupla_inicial = (1, 2, 3)
tupla_modificada = tupla_inicial + (4,)
print(tupla_modificada)
