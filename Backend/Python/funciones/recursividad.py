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

print('--Imprimir del 5 a 0--')
def motrarNumeros(num):    
    if num == 0: 
        print(num)
    else:
        print(num)
        motrarNumeros(num - 1)
motrarNumeros(5)
print('--Factorial Nomrla')
def factorial_normal(n):
    r = 1
    i = 2
    while i <= n:
        r += i
        i += 1
    return r
print(factorial_normal(5))

print('--Suma recursiba--')
def suma_0(n):
    if n ==0:
        resultado=0
    else:
        resultado = n + suma_0(n -1)
    return resultado
resul_suma_0 = suma_0(5)
print(resul_suma_0)

print('--palabra al reves--')
def alreves(palabra, n):
    if 0 ==n:
        resultado = palabra[n]
    else:
        resultado = palabra[n] + alreves(palabra, n -1)
    return resultado
palabra = 'perro'
print(alreves(palabra, len(palabra)-1))

print('--Fatorial Rerusivo--')
def fact(n, a=1):
    if(n == 1):
        return a
    return fact(n-1, n * a)
print(fact(5))