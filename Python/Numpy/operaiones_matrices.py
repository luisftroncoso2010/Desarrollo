import numpy as np


# Filtrar elementos en una sola dimensión
m = np.arange(24).reshape(4,6)
print(m [3, 4])
print(m)


# Organizar elemntos de manera ascendente 
mUno = np.array([90, 7, 9, 4, 2, 1])
print(np.sort(mUno))


#  Elevarlos al cuadrado los elementos de array
mDos = np.array([2, 3])
print(np.power(mDos, 2))
print(np.array(mDos ** 2))


# Filtrar con base a una condición
mTres = np.array([2, 3, 4, 5, 6, 7])
print(np.array(mTres >= 4))
print(np.array(mTres.max()))  # valor maximo dela matriz
print(np.array(mTres.min()))  # valor minímo dela matriz


# Concatenar dos matrices 
mCuatro = np.array([2, 3, 4, 5, 6, 7])
mCinco = np.array([11, 34, 67, 99])
print(np.concatenate((mCuatro, mCinco)))


# Matrices de dos dimensiones sumar
mSeis = np.array([[1, 2], [3, 4]])
mSiete = np.array([[5, 6], [7, 8]])
print(mSeis + mSiete)


# Sumar datos a las matrices. De dos dimensiones
print(mSeis + 2)
print(np.add(mSeis, mSiete))  # Suma de matrices
print(np.subtract(mSeis, mSiete))  # restar matrices
print(np.multiply(mSeis, mSiete))  # Multiplicar elementos
print(np.divide(mSeis, mSiete))  # Restar elementos
print(mSeis.dot(mSiete))  # 
print(mSeis)
print(mSiete)