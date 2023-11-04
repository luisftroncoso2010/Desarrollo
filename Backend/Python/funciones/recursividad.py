'''
Funcines recursivas
'''
print('--Suma recursiva--')
def sumaRec(numero):
    if numero == 1:
        return 1
    else:
        return numero + sumaRec( numero - 1)
    #El 'Itera' desde el numero 5 hasta 1, sin hacer ninguna operacion
    #De vueltra si hace las operaciones    
resultado = sumaRec(5)
print(resultado)

print('--Factorial recursivo--')
def factorialRec(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorialRec( numero - 1)
    #El 'Itera' desde el numero 5 hasta 1, sin hacer ninguna operacion
    #De vueltra si hace las operaciones    
resultadoFac = factorialRec(5)
print(resultadoFac)

print('--Serie fibonacci--')
def fibonacciRecursivo(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacciRecursivo(numero - 1) + fibonacciRecursivo(numero - 2)
print(fibonacciRecursivo(5))

print('--Mostrar lista con recursibidad--')
def motrarListRec(lista, index):
    if index!= len(lista):
        print(lista[index])
        motrarListRec(lista, index + 1)
lista = [1, 2, 3, 4, 5]
motrarListRec(lista, 0)
