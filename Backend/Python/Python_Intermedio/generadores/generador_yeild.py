print('-- Generador simple')


def generador_simple():
    yield 1
    yield 2
    yield 3


# Creamos el genereador simple usando next y mostramos uno por uno
print(f'Primer: {next(generador_simple())}')
generador = generador_simple()
for i in generador:
    print(f'Numeros del Generador: {i}')


print('-- Generador con For')


def generador_ciclo(n):
    for i in range(10, n):
        yield i


# Mostramos el generador
generador_ciclo = generador_ciclo(15)
print(next(generador_ciclo))
print(next(generador_ciclo))


print('-- Creamos funcion generadora')


# Creamos la funcion generadora
def funcion_generadora():
    for i in range(10):
        yield i


for item in funcion_generadora():
    print(item)


print('-- Serie Fibonacci usando generadores')


def fibonacci(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


# Le damos un valor a la serie y lo almacenamos en una variable
fibonacci = fibonacci(6)
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

# Pasamos el valor de la serie fibonacci
'''for x in fibonacci:
    print(x)'''


print('-- Generadores pasando una lista')


def fibon(n):
    a = b = 1
    resultado = []
    for i in range(n):
        resultado.append(a)
        a, b = b, a + b
    return resultado


# Me genera una lista de la serie fibonaccie
print(fibon(10))


print('-- Iteramos una cadena')


my_strgin = 'Pelayo'  # Creamos la cadena (String)
my_iter = iter(my_strgin)  # Creamoa el objeto iterable con la funcion iter()
print(next(my_iter))
print(next(my_iter))