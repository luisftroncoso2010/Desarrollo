'''
Parametro *args
'''
print('--Sumar dos numeros--')
def suma(a, b):
    return a + b

resultado = suma(2, 4)
print(resultado)


print('--Sumar varios numeros de una lista. MANERA NO CORRECTA--')
def sumaLista(lista):
    numerosSumados = 0
    for numeros in lista:
        numerosSumados = numerosSumados + numeros
    return numerosSumados
print(sumaLista([4, 10, 5]))

print('--Suma corrar de sumar numeros indefinidos. Parametro args--')
def sumarLista(*numeros):
    return sum(numeros)
print(sumarLista(4, 10, 5))

print('--Suma corrar de sumar numeros indefinidos. Parametro args, agregamos un parametro distinto--')
def sumarLista(nombre, *numeros):    
    return f'{nombre}, la suma de los numeros es {sum(numeros)}'
print(sumarLista('Luis', 4, 10, 5)) #Se llenan los parametros de manera normal

#Pasando una lista por parametro
def sumarLista2(nombre, numeros):
    return  f'{nombre}, la suma de los numeros es {sum([*numeros])}'
print(sumarLista2('Luis', [4, 10, 5])) #Se llenan los parametros con una lista