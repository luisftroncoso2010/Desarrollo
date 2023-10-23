#Creando un diccionario con dict()
''''
No se usan las {} para crear una diccionario. 
Se usan los paretecis () por el metodo dict()
'''
diccionario = dict(nombre = 'Lucas', apellido ='dalto')
print(diccionario)

'''
Las listas no pueden ser claves y usamomos frozenset()
para poder meter conjuntos al diccionario
'''
diccionario2 = {frozenset(['Dalto', 'Rancio']), 'Risas'}
print(diccionario2)

'''
Creando un diccionario con fronkeys(). Crea el diccionario
con fronkeys() con valores vacios (None).
Si los corchetes no se colocan el primer valor sera 
la llave y el segundo el valor de la llave
'''
diccionario3 = dict.fromkeys('ABCDE', 'none') #Sin corchetes
print(diccionario3)
diccionario4 = dict.fromkeys(['Nombre', 'Apellido'])
print(diccionario4)
