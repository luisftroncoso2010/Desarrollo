''' Filter: Filtra los elementos de una lista usando un
determinado criterio, es decir, crea una lista bajo una condicion'''


print('-- Uso del filter')


# Creamos una lista
lista = list(range(-5, 5))
# print(lista)
# Filtramos la lisa con la funcion. creará una lista aparte
menor_cero = list(filter(lambda x: x < 1, lista))
# Imprimimos la lista con los valores menores a cero
print(menor_cero)
# Lista con numeros pares
numeros_pares = list(filter(lambda x: x % 2 == 0 and x > 0, lista))
# Imprimimos la lista menores que cero
print(numeros_pares)
