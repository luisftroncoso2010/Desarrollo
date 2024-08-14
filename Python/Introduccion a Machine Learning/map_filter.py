"""Ejecuta una funcion especifica para cada elemento iterable"""


def mult(numero):
    return numero * 5


lista = [1, 2, 3, 4, 5, 6, 7]
lista_map = list(map(mult, lista))
print(lista_map)


# Otra funcion
def cursos(c):
    return c.upper()  # Convierte todo en mayúsculas


tupla = ('php', 'python', 'java', 'dart', 'css')
tupla_actualizada = tuple(map(cursos, tupla))
print(tupla_actualizada)


"""Crear un elemento iterador apartir de un elemento existente"""


def impares(numero):
    if (numero % 2 == 1):
        return numero


listaDos = [1, 2, 3, 4, 5, 6]
listaImpares = list(filter(impares, lista))
print(listaImpares)
