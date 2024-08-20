import numpy as np
""" Ejes: Yaxis y Xaxis"""
" Axis 1 filas y Axis 0 columnas"


# Suma numérica con el eje en 0
m = np.array([[0, 1, 2], [4, 2, 3]])
mDos = np.array([[8, 8, 8], [8, 8, 8]])
print(m)
print("")
# Generamos una matriz de una osla dimension. Sumamos las columnas
print(np.sum(m, axis=0))
# Generamos una matriz de una osla dimension. Sumamos las filas
print(np.sum(m, axis=1))
print("")
print(m)
print("")
print(mDos)
print("")
print(np.concatenate([m, mDos], axis=1))
print('     * Matriz en una sola dimensión: ')
dimensionUno = np.array([1, 1])
dimensionDos = np.array([8, 8])
# Aca solo concatena en una sola dimensión
print(np.concatenate([dimensionUno, dimensionDos], axis=0))