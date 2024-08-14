# Las tuplas luego de ser creadas nos pueden ser modificadas
tupla = (0, 2, 5, 4, 9, 5, 5)
print(tupla)

# Otra tuplas. Concatenar tuplas
tuplaA = (0, 1, 2, 3, 4)
tuplaB = ('uno', 'dos', 'tres')
print(tuplaA + tuplaB)

# Replicar un dato de la tupla
tuplaC = ('python ') * 4
print(tuplaC)

# Contar datos repetidos
repetido = tupla.count(5)
print(repetido)

# Buscamos el primer elemento. Arroja el segundo elemento
primero = tupla.index(5)
print(primero)


# Pasar de tupla a lista y visiversa
x = ('rojo', 'amarillo', 'verde')
y = list(x)
print(y)
y[1] = 'negro'
x = tuple(y)
print(x)
