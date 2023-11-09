'''
Matrices phython
'''
print('--Matriz Cars--')
cars = ['Ford', 'Volvo', 'BMW']
print(cars[0])

print('--Modificar le valor del primer elemento--')
cars[0] = 'Toyota'

print('--Contar los elementos de una matriz--')
print(len(cars))

print('--Contar elementos de una matriz--')
for x in cars:
    print(x)
    
print('--Agregar elementos a una matriz--')
cars.append('Honda')#Lo agrrega en la ultima posicion
print(cars)

print('--Eliminar elementos de una matriz por pocicion--')
cars.pop(1)
print(cars)

print('--Eliminar elementos de una matriz--')
#cars.remove('Vol')#Si no lo encuntra manda una exepcion
print(cars)

print('--Devuelve le INDICE del valor especificado--')
print(cars.index('BMW'))

print('--Inserta una elemento de en la poscion especificada--')
cars.insert(0, 'Renault')
print(cars)

print('--Ordena de manera alreves--')
cars.reverse()
print(cars)

print('--Ordena alfabeticamente--')
cars.sort()
print(cars)