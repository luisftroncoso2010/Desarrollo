"""Diferencias entre listas y arrays"""
# Las listas se alamcenan diferentes tipos de datos
# Los arrays solo se almacenas un solo tipo de dato
import array as ar
import numpy as np

# Creamos una matriz con numpy
matriz = np.array([1, 2, 3, 4])
print(type(matriz))


# Probamos con una lista
lista = [1, 3, 5]
lista.append(8)
matrizDos = np.array([2, 4 ,6])
matrizDos = matrizDos + np.array([8])  # Estos valores se suman. No los añade
print(lista)
print(matrizDos)


# Multiplicasión de matris con numpy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a * b)