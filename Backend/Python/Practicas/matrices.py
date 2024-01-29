import random as rd
'''Matrices generar una matriz'''
print('-- Matriz dada')
matriz_dada = [
    [1, 2, 3, 4],
    [4, 5, 6, 4],
    [7, 8, 9, 4]
]

for fila in matriz_dada:
    for elemento in fila:
        print(elemento, end=' ')
    print()


print('-- Matriz con valores generados (randit)')


matriz_randit = [list(rd.randint(1, 10)
                 for columnas in range(5))
                 for filas in range(4)]

for fila in matriz_randit:
    for elemento in fila:
        print(elemento, end=' ')
    print()


print('-- Valores generados aleatorios')


numeros_aleatorio = rd.sample(range(1, 100), 50)
print(numeros_aleatorio)
c = [list(rd.choice(numeros_aleatorio)
     for columnas in range(5))
     for filas in range(4)]

print('-- Matriz rellenada con numeros aleatorios de una lista')
for fila in c:
    for elemento in fila:
        print(elemento, end=' ')
    print()


print('-- Range')
lista = list()
x = range(0, 10, 2)
for i in x:
    lista.append(i)

print(lista)
compresion = [i for i in range(1, 10) if i % 2 == 0]
print(f'Compresion de lista: {compresion}')
