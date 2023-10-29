'''
Dicionarios se puden crear con el metodo dict()
NOTA: No se puede crear diccionarios VACIOS 
a no ser que sea con el identificador de su
coleccion ejemplo: Los diccioanarios dict(), 
tuplas: tuple(), lista: list(), conjunsto: set()
'''
#creando diccionarios con dict()
print('--Creando diccionario con dict()--')
diccionario = dict(nombre = 'lucas', apellido = 'dalto')
print(diccionario)

'''
Las lista NO pueden ser CLAVES por que SON MUTABLES, 
las tuplas si, por que son elemntos hasheables
'''
print('--Tuplas como llaves de diccionarios--')
diccionarioDos = {('Lucas', 'Dalto'): 100000}
print(diccionarioDos)

'''
Usamos el metodo frozenset() para colocar una lista como hasheables
'''
print('--Vonvertimos una llave a hasheable--')
frozensetDict = {frozenset({'nombre', 'apellido'}): 'Lucas'}
print(frozensetDict)

#creando diccionarios con fronkeis, los valores son vacios
print('--Creando diccionarios con valores NONE')
fronKeysDict = dict.fromkeys(['Nombre', 'Apellido', 'Email'])
print(fronKeysDict)
#O por ejmplo asi, para que sea de A a la D, las llaves
fronKeysDictDos = dict.fromkeys('ABCD')
print(fronKeysDictDos)

print(type(fronKeysDictDos))