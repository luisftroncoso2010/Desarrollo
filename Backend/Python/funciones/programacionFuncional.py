'''
Programacion funcional
'''
print('--Programacion funcional metodo map()--')
lista = [1, 2, 3, 4, 5]
def por_dos(x):
    return x * 2 
#Map() resive un funcion y un iterable como entrada
listaPordos = map(por_dos, lista)
print(f'Lista por dos funcion normal. map(): {list(listaPordos)}')
#Ahora escojamos la lista por 2 con lambda
listaPordosLambda = map(lambda x: 2*x, lista)
print(f'Lista por Dos con map() y lambda: {list(listaPordosLambda)}')

print('--Filter--')
listaDos = [7, 4, 16, 3, 8]

def es_par(num):
    return num % 2 == 0
#Se usa filter se le pasa la funcion y la lista
pares = filter(es_par, listaDos)
print(f'Lista pares. Funcion normal. filter() {list(pares)}') 

#Ietra la lista y crea una nuea solo si los resultados son True
pares = filter(lambda x: x %2 == 0, listaDos)
print(f'Lista pares, filter y lambda: {list(pares)}')

print('--Reduce--')
from functools import reduce
from operator import add, mul
listaTres = [1, 2, 3, 4, 5]
#Sumar todos los elementos de la lista. Reduce todos los elementos de la entrada a una unico valor
sumaReduce = reduce(lambda acc, val: acc + val, listaTres)
print(f'La suma con reduce es {sumaReduce}')
#Reduce devuelve la suma de dos valores
sumaAdd = reduce(add, listaTres)
print(f'La suma con add es {sumaAdd}')
'''
Nota: Es importante que la funcion resive DOS ARGUMENTOS:
El acumulador y la lista (cada uno de los valores de la lista)
'''
#Multiplicacion de todos los elementos de la lista. Reduce todos los elementos de la entrada a una unico valor
multiplicacionReduce = reduce(lambda acc, val: acc * val, listaTres)
print(f'La multiplicacion de la lista con reduce es {multiplicacionReduce}')
multiplicacionMul = reduce(mul, listaTres)
print(multiplicacionMul)

#Reduce es especialmente cuando tenemouna listas de diccionarios
print('--Reduce en listas de diccionarios--')
listDictPersonas = [
    {'Nombre': 'Alicia', 'Edad': 22},
    {'Nombre': 'Bob', 'Edad': 29},
    {'Nombre': 'Charlie', 'Edad': 33}  
]
#Escogemos el reduce para sumar la edad de las persona
sumaEdad = reduce(lambda total, p: total + p['Edad'], listDictPersonas, 0)
print(sumaEdad/len(listDictPersonas))# Promedio de las edades

print('--Ejemplos de programacion funcional--')
personas = [
    {'Nombre': 'Luis', 'Edad': 22, 'Sexo': 'F'},
    {'Nombre': 'Bob', 'Edad': 25, 'Sexo': 'M'},
    {'Nombre': 'Charlie', 'Edad': 33, 'Sexo': 'M'},
    {'Nombre': 'Diana', 'Edad': 15, 'Sexo': 'F'},
    {'Nombre': 'Esteban', 'Edad': 30, 'Sexo': 'M'},
    {'Nombre': 'Federico', 'Edad': 44, 'Sexo': 'M'}
]
Hombres = list(filter(lambda x: x['Sexo'] == 'M', personas))
sumaEdades = reduce(lambda suma, p: suma + p['Edad'], Hombres, 0)
mediaEdad = sumaEdades/(len(Hombres))
print(mediaEdad)
print('↓↓↓ Todo en un mismo codigo ↓↓↓')
mediaEdades = reduce(lambda suma, p: suma + p['Edad'], filter(lambda x: x['Sexo'] == 'M', personas), 0 )/ len(list(filter(lambda x: x['Sexo'] == 'M', personas)))
print(f'Media Edades: {mediaEdades}')
