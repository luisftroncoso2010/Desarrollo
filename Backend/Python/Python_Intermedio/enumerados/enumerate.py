'''Enumerate: Es una funcion que se utiliza para agregar
un contador a un iterable'''

print('-- Enumerate con indice')


# Declaramos la lista
frutas = ['Manzana', 'Banana', 'Cereza']
# Usar enumerate para obtener tanto el indice como el valor
for indice, valor in enumerate(frutas):
    print(valor)


print('-- Enumerate star 5(Inicio)')


# Creamos el ciclo con indice de inicio 5 (start 5)
print('Frutas: ')
for indice, valor in enumerate(frutas, start=5):
    print(f'Indice: {indice}, Valor: {valor}')


print('-- el indice y la lista, tupo tupla')


lista_frutas = list(enumerate(frutas, start=10))
print(f'{lista_frutas}')


print('-- enumeratre con cadenas')


cadena = 'geeks'
print(tuple(cadena))
print(list(enumerate(cadena)))


print('-- Uso de la funcion next()')


enum_fruits = enumerate(frutas)
print(f'Next Element: {next(enum_fruits)}')
print(f'Next Element: {next(enum_fruits)}')
