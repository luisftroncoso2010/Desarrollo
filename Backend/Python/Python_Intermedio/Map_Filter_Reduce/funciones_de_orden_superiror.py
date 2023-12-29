from functools import reduce


# Creamoas las funciones de orden superior a drede
def operation(x, fun):
    return fun(x)


def sqtr(x):
    return x ** 0.5


def squared(x):
    return x ** 2


# Escogemos la funcion operation y le pasamos las
# otras funciones creadas a drede
result = operation(16, sqtr)
print(f'La raiz cuadrada es: {result}')

result_ = operation(16, squared)
print(f'El exponente es: {result_}')


print('-- Usamos la funcion filter')
integer = [4, 5, 6, 9, 10, 50, 10]
even = list(filter(lambda x: x % 2 == 0, integer))
print(even)


print('-- Usamos la funcion map')
# Elevamos cada elemento de la lista al cubo
cubeb = list(map(lambda x: x ** 3, integer))
print(cubeb)


print('-- Usamos la funcion reduce')
# Suma de elementos de una lista
suma_lista = reduce(lambda a, b: a + b, integer)
print(f'La suma de la lista integer es: {suma_lista}')


print('-- Usamos la funcion sorted')
estudiantes = [
    ('Juana', 22, 95, '3106752010'),
    ('Pedro', 18, 89, '3102451020'),
    ('Juan', 25, 94, '3201457895')
    ]


# Creamos la funcion que nos ayudara a ordenar
# por valores e indice especificado
def ordenar_lista(estudiante):
    return estudiante[1]


# Ordenamos la lista atraves de un un indice especificado
lista_estudiante = sorted(estudiantes, key=lambda x: x[2], reverse=True)
print(lista_estudiante)
