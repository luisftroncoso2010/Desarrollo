from functools import reduce
# Funciones de orden superrior map, filtter reduce
print(' * map: ')


def cuadrado(n):
    return n ** 2


lista = [1, 2, 3]
listaCopia = map(cuadrado, lista)
print(f'La lista es: {list(listaCopia)}')  # Crea una nueva lista

print(' * Reduce: ')


def es_par(n):
    return (n % 2.0 == 0)


listaNumeros = [1, 2, 3, 4]
listaPares = filter(es_par, listaNumeros)
print(f'Lista numeros parees: {list(listaPares)}')

print(' * Reduce: ')


def operacion(x, y):
    return x - y


listaSuma = [1, 3, 5]
reduce_ = reduce(operacion, listaSuma)
print(f'La operacion es: {reduce_}')


# Funciones lambada
print('     * lambda: ')
listaLambda = [1, 2, 4]
lambda_ = filter(lambda n: n % 2 == 0, listaLambda)
print(f'filter lambda: {list(lambda_)}')

print(' * Compresion de lista: ')  # Genera una lista apartir de una lista
listaCompresion = [1, 2, 3]
compresionLista = [n ** 2 for n in listaCompresion]
print(f'Comrpasion de lista, exponencial: {compresionLista}')
compresionListaDos = [n for n in listaCompresion if n % 2 == 0]
print(f'Compresion de lista con condicional: {compresionListaDos}')
