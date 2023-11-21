'''
Iteradores de python.
Un iterador es un objeto que se puede iterar, lo que
significa que se puede rocorrer todos los valores.
Las listas, tuplas, diccionarios y conjuntos son todos
objetos iterables. Son contenedores iterables de los que
puede obtener un iterador.
'''
#Creamos una tupla 
myTuple = ('apple', 'banana', 'cherry')
myit = iter(myTuple)
#Iteramos uno por uno los elementos de la tupla
print(f'Primer elemento: {next(myit)}')
print(f'Segundo elemento: {next(myit)}')
print(f'Tercer elemento: {next(myit)}')

#Creamos una cadena. Iteramos uan cadena
mystr = 'Banana'
myiter = iter(mystr)
#Recorremos cada uno de los iterables con el metodo next() 
print(f'Primer caracter: {next(myiter)}')
print(f'Segundo caracter: {next(myiter)}')
print(f'Tercer caracter: {next(myiter)}')
print(f'Cuarto caracter: {next(myiter)}')
print(f'Quinto caracter: {next(myiter)}')
print(f'Sexto caracter: {next(myiter)}')

'''
Tambien se puede usar un ciclo for() para recorrer un iterable 
'''
print('Iterar con un ciclo una Tupla')
for i in myTuple:
    print(i)

print('Iterar sobre un String')
for i in mystr:
    print(i)
