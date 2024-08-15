"""Funcion range genera números en el enteros antre el final y
el entero final"""

# Genera una lista de numéros a partir de una lista
print(list(range(0, 7)))

# Mostrar numéros del 0 a 7
for i in range(0, 7):
    print(i, end=', ')

# Imprimir con saltos
print('\n')
for i in range(2, 10, 2):
    print(i, end=', ')

# Colocar con numeros
print('\n')
for i in range(2, 10, 2):
    print('El valor de i es: ', i)

# Generar un triangulo
for num in range(10):
    for i in range(num):
        print(num, end=' ')
    print()

# Invertir un rango
for i in reversed(range(0, 10)):
    print(i, end=', ')

# Generar lista con range
print('\n')
generarLista = list(range(1, 8))
print('Lista: ', generarLista)
