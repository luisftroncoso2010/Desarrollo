import random as rn


print('-- Generar una lista de numeros con el el modulo randim')
numeros = [rn.randint(1, 10) for _ in range(10)]
print(numeros)


print('-- Crear una lista con la funcion range()')
numeros_dos = list(range(1, 10))
print(numeros_dos)


print('-- Creamos una tabla de multiplicar con la funcion range()')

for i in range(1, 11):
    print(f'Tabla de multiplicar {i}')
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')
