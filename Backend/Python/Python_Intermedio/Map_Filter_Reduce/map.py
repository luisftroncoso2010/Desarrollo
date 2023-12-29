'''Map: Aplica una determinada funcion a todos los elementos
de una entrada o lista '''


print('-- Uso de map')


# Forma map: map(funcion_a_aplicar, lista_de_entradas)
map_lista = [4, 5, 9, 10]  # Elevaremos esta lista al cuadrado
# Forma normal
lista_al_cuadrado = list()
for i in map_lista:
    lista_al_cuadrado.append(i ** 2)
print(f'Lista sin MAP: {lista_al_cuadrado}')
'''Uso del MAP'''
# Genera resultados de una lista al cuadrado atraves de una funcion lambda
lista_al_cuadrado_map = list(map(lambda x: x ** 2,  map_lista))
print(f'Uso del MAP: {lista_al_cuadrado_map}')


print('-- map con funciones')


# Creamos una funcion multiplicar
def multiplicar(x):
    return (x*x)


# Creamos la funcion sumar
def sumar(x):
    return (x+x)


# Creamoa una lista con dos funciones
funciones = [multiplicar, sumar]
for i in range(5):
    m, s = valor = list(map(lambda x: x(i), funciones))
    print(f'Multiplicacion: {m}\tSuma: {s}')
