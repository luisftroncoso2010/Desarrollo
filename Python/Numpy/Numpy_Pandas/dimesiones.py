import numpy as np

"""Definir un tension, sumar la dimension, sumar una
dimesion en cualquiera de sus ejes."""

# Tensor
tensor = np.array([[[1, 2, 3], [4, 5, 6],  [7, 8, 9],  [10, 11, 12]],
                   [[1, 2, 3], [4, 5, 6],  [7, 8, 9],  [10, 11, 12]],
                   [[20, 21, 22], [23, 24, 25], [26, 27, 28], [29, 30, 31]],
                   [[20, 21, 22], [23, 24, 25], [26, 27, 28], [29, 30, 31]]
                   ])
print(tensor)
print(tensor.ndim)


# Agregar una unica dimension en sus ejes.
expand = np.expand_dims(tensor, axis=0)
print(expand)
print(expand.ndim)
print(expand.shape)
print(expand.size)


# Eliminamos las dimesiones que no se estan usando o sobran
print('-- Eliminamos la dimensiones sobrantes: ')
eliminarDimesniones = np.squeeze(expand)
print("Dimensiones: ", expand.ndim)
