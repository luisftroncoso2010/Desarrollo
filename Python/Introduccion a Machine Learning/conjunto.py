"""Los cunjuntos en python son una colección de eleméntos
de forma desordenada y no acepta duplicados."""

# Conjunto
conjunto = {1, 23, 5, 4, 5}
print(conjunto)

# Conjuto con palabra propia. Mezclado con tupla
set = {1, 2, 3, 4, 5, 5, ('w', 't'), 'python'}
print(set)

# Conjunto
setDos = {1, 2, 3, 4}
set.add(5)
print(setDos)

# Limpiar un conjuto por completo
setTres = {1, 2, 3, 4}
setTres.clear()
print(setTres)

# Descaertar uno de los elementos del conjunto
setCuatro = {1, 2, 3, 4}
setCuatro.discard(2)  # No lo elimina, solo lo descarta
print(setCuatro)

# Eliminar un dato en especifico
setCinco = {1, 2, 3, 4}
setCinco.remove(2)
print(setCinco)

# Uso del join en el conjunto
setA = {1, 2, 3, 4, 5}
setB = {5, 4, 6, 7, 8, 2}
print(setA | setB)  # Union de conjuntos
print(setA & setB)  # Elemento que se comparte en conjuntos
print(setA - setB)  # Solo se dejan las diferencias
print(setA ^ setB)  # Se van los que se repiten
