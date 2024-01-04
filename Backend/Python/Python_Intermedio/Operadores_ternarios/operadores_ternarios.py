''' Los operadores ternarios se usan para expresar
condicionales de manera mas concisa en comparación con
las estructuras de control de flujo más extensas'''

print('-- Operadores ternarios --')
print('-- Ejemplo belleza')
es_bonito = True  # Creamoa la variable con un valor
# Comparamos la variable con dos valores bajo su condicion
estado = 'Es bonito' if es_bonito else 'No es bonito'
print(estado)  # Imprimimos el estado(Resultado)


print('-- Ejemplo belleza con una lista')
_es_bonito = True
# Aca dependiendo la comparacion el primer valor de la tupla es False
# y el segundo es True. Se comprara que el de la lista
apariencia = ('Feo', 'Bonito')[_es_bonito]
print(f"El gato es {apariencia}")


print('-- Divicion con Operadores Ternarios')
condicion = False
# Este oeprador tenario es evaluado. Es decir:
# Aca nmo se evaluan los resultados
# print(2 if condicion else 1/0)
# Ente tipo de operaicon es aca se se evaluan los reultados
# print((1/0, 2)[condicion])


print('-- Numeros para con operadores ternarios')
numero = 3
print(f'Numeros pares : {"Par" if numero % 2 == 0 else "Es impar"}')
print('-- Asginacion abasa en una condicion')
puntuacion = 75
resultado = 'Aprobado' if puntuacion >= 70 else 'Reprobado'
print(resultado)


print('-- Usando expresiones aritmeticas')


a = 5
b = 3
maximo = a if a > b else b
print(f'El maximo valor es : {maximo}')
