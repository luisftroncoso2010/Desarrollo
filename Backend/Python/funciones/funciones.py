''' Funciones '''


def myFunction(name, lasname):
    print(f'Hola {name} {lasname}')


namesOne = myFunction('Luis', 'Troncoso')
# Manda un error argumantando que falta un parametro
namesTwo = myFunction('Andres', 'Troncoso')


'''
Argumentos arbitrarios
'''
print('--Argumentos arbitrarios--')


def myFuntionTwo(*arbitrary):  # Recibir los argumentos como tupla
    print(f'Hola Luis Fernando Tu eres {arbitrary}')


# Se pasan los parametros y los resive como tuplas
myFuntionTwo('Id', 'Cedula', 'Name')


print('--Argumentos arbitrarios por pocicion--')


def myFuntionTree(*arbitrary):
    # Escoge la pocicion de la tupla
    print(f'Hola Luis Fernando Tu eres {arbitrary[2]}')


# Se pasan los parametros y los resive como tuplas
myFuntionTree('Id', 'Cedula', 'Name')


print('--Argumentos palabra clave--')


def muyFuntionFour(child3, child2, child1):
    print(f'The youngest child is {child3}')


# Se pasan argumentos clave valor
muyFuntionFour(child1='Luis', child2='Maria', child3='Marcos')


print('--Argumentos palabras claves, llave valor--')


def myFuntionFive(**kid):
    print(f'His last name is {kid["lname"]} and his name is {kid["fname"]}')


myFuntionFive(fname='Tobias', lname='Montes')

print('--Valor por parametro predeterminado--')


# valor pro parametro predeterminado
def myFunctionSix(country='Norway'):
    print(f'I am from {country}')


# Si se pasa uno nuevo lo actualiza
myFunctionSix(country='Colombia')


print('--Pasar una lista como argumento--')


def myFunctionSeven(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
myFunctionSeven(fruits)

print('--Valores de retorno--')


def myFunctionEight(x):
    return 5 * x


print(myFunctionEight(5))


print('--Recursibidad--')


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\nRecursion Example Results")
tri_recursion(4)


print('--Recursibidad Fibonacci--')


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


resultado = fibonacci(7)
print("El séptimo número de la serie de Fibonacci es:", resultado)

print('--Factorial Normal--')


def factorial_normal(n):
    r = 1
    i = 2
    while i <= n:
        r *= i
        i += 1
    return r


factorioalNormal = factorial_normal(5)
print(factorioalNormal)


print('--Factorial recursivo--')


def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)


print(factorial_recursivo(5))  # 120


print('--Fibonacci recursivo--')


def fibonacciRecuersivo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecuersivo(n - 1) + fibonacciRecuersivo(n-2)


resultadoFibonacci = fibonacciRecuersivo(3)
print(resultadoFibonacci)
