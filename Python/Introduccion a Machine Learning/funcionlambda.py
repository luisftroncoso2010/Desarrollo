"""Es una función anónima"""


def doble(x):
    return x * 2


print(doble(4))


# Doble con funcion lambda.
# Esuna mala practica alamacenar una funcion lambda en una varialbe
dobleDos = lambda x: x * 2
print(dobleDos(2))


# Lista con funcion lambda y filter
lista = [1, 2, 44, 48, 4, 24, 12, 68, 67]
listaPares = list(filter(dobleDos, lista))
print(listaPares)

# Lambda interno
listaParesDos = list(filter(lambda x: x % 2 == 0, lista))
print(listaParesDos)

# Elementos en una lista. Duplicarlos
listaDos = [4, 8, 7, 69, 4, 20, 10, 11]
listaDoble = list(map(lambda x: x * 2, listaDos))
print(listaDoble)