import numpy as np


# Numeros aleatorios entre 0 y 10
m = np.random.randint(10)
print(m)


# Numeros aleatorios entre 0 y 10- 5 numeros
mUno = np.random.randint(10, size= 5)
print(mUno)


# Numeros aleatorios entre 0 y 10 y generamos una matria 3* 3
mDos = np.random.randint(10, size= (3,3))
print(mDos)


# Numeros aleatorios 5 elementos de manera decimal
mTress = np.random.randn(5)
print(mTress)


# Numeros generar una matriz de numeros aleatorios 2 * 2
mTres = np.random.randn(2, 2)
print(mTres)


# Devolver un solo valor de una matriz
mCuatro = np.random.choice([3, 5, 9, 5, 1])
print(mCuatro)


# Escoger un numero de una matriz bidimensional o una matris Trdimensional
mCinco = np.random.choice([3, 5, 9, 5, 1], size=(2, 3))
print(mCinco)


"""Distribución Aleatorias:
    Algo que no se puede predecir lógicamente. Es un conjunto de números aleatorios
    que siguen una determinada función de densidad de probabilidad
"""


# Probabilidad: 
mSeis = np.random.choice([2, 4, 6], p = [0.5, 0.5, 0.0], size=(6))
print(mSeis)


# Matriz con 50 valores con elementos permitidos
mSiete = np.random.choice([2, 4, 8, 10], p=[0.3, 0.5, 0.1, 0.1], size=[50])
print(mSiete)