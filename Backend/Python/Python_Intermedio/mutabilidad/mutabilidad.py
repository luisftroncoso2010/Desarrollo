'''Mutabilidad'''


print('-- Mutabilidad en una lista')
# Creamos una lista y la almacenamos en una variable
foo = ['Hola']  # Almacenamos un dato
print(foo)

bar = foo  # Creamos la variable bar y le damos un valor. (La lista anterior)
bar += ['adios']  # Agregamos a un valor a la variable bar (Una lista)
print(f'El nuevo valor de bar es: {bar}')  # Imprimos bar, con su nuevo valor.
print(f'El valor de la variable foo es: {foo}')


print('-- Mutabilidad con funciones (Añadiendo datos a una lista)')


# Creamos la funcion para agregar datos y que se vaya ampliando
def agrega(num, target=[]):
    target.append(num)
    return target


# Le pasamos un dato a la funcion
agrega(4)
agrega(70)
agrega(80)
# Imprimimos para mirar el valor que tiene
func_agregar = agrega(5)
'''NOTA: Siempre se agregará un valor, dado que por parametro se le creó
una lista vacia  y siempre que se ejecute dicha funcion, solo se agregará
a la lista el dato pasado por parametro, cuando se muestre mostrará todos
los valores por los cuales se agregaron'''
print(func_agregar)


print('-- Mutabilidad con funciones ()')


# Creamoa la funcion añadir. con un target vacio
def añadir(element, target=None):
    # Validamos si el target es None (Vacio)
    if target is None:
        # Si es asi(None) conviertelo en una lista
        target = []
    # Ya es una lsita, por favor añadele un elemento
    target.append(element)
    # Retornamos el target a la funcion, su valor
    return target


'''NOTA: Cada ves que se llame la funcion el target se "reiniciará",
dado que su target siempre se le dió el valor, predefinido(Vacio)'''
# Le pasamos datoa a la funcion
añadir_uno = añadir(74)
print(añadir_uno)
# Añadir un vallor a la funcion
añadir_dos = añadir(85)
print(añadir_dos)
