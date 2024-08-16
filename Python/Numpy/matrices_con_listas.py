import numpy as np

matriz = np.array([1, 2, 3, 4, 5, 6])
print(matriz)


# Creamos una matriz
m2d = np.array([[1, 2, 3], [4, 5, 6]])
print(m2d)


# Creamos una array con base a una lista
lista = [1, 2, 3, 4, 5]
matrizDos = np.array(lista)
print(matrizDos)

# Matriz 3 por 3
listaDos = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrizTres = np.array(listaDos)
print(matrizTres)

# Estrcturar matriz
m = np.arange(20).reshape(4, 5)  # Creamos una matriz 4 * 5
print(m)
""" Funciones en matricez """
print(m.shape)  # Me muestra las filas y las columnas
print(m.ndim)  # Dos dimansiones de la matriz
print(m.size)  # Numero de elementos en la matriz

# 
mDos = np.zeros((3, 4))
print(mDos.size)  # Muestra numero de elementos en la matriz
print(mDos)

# Matriz de una sola dimensión con arange
mTres = np.arange(10)
print(mTres.size)
print(mTres)

# Matriz de una sola dimensión con linspace
mCuatro = np.linspace(99, 88)  # Es una rango para matrices rapidas
print(mCuatro.size)
print(mCuatro)


# Matriz de tres dimenciones
mCinco = np.arange(27).reshape(3, 3, 3)
print(mCinco)
print(mCinco)