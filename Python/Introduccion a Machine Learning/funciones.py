""" Una función es un grupo de declaraciones
relacionadas que realiza una tarea especifica.
Ayuda a dividir en partes mucho mas pequeñas"""

# Función


def miFuncion(nombre, edad):
    print(f'Hola, mi nombre es {nombre} con la edad de {edad}')


miFuncion('Luis', 26)


# Función suma
def suma(nUno, nDos):
    return nUno + nDos


print(suma(3, 8))


# Funcion sin parametros
def funcios():
    x = 50
    print('numero:', x)


funcios()


# Funcion suma de variables internas
def sumaDos():
    a = 10
    b = 20
    c = a + b
    return c


print(sumaDos())


def funcionDos():
    x = 40  # Variable local
    print(x)


x = 80  # Variable global
funcionDos()
print(x)
