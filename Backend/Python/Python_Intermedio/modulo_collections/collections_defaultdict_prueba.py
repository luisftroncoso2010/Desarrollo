from collections import defaultdict
import json
'''Prueba del modulo collections'''

print('-- Creamos un diccionarios')
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print('Dictionary: ')
print(Dict)
print(Dict[1])
try:
    print(Dict[8])
except KeyError:
    print('La llave especificada no exciste')


print('-- Uso del defaultdict')


# Creamos una funcion que valide si esta o no un dato o llave
def def_value():
    return 'Not present'


d = defaultdict(def_value)
d['a'] = 1
d['b'] = 2


print(d['a'])
print(d['b'])
print(d['d'])


print('-- Escogiendo un valor __missing__')
dict_ = defaultdict(lambda: 'Not Present')
dict_['a'] = 1
dict_['b'] = 4
'''Nota: cuando el metodo missing es llamado, solo se
usará la clve no aparezca, es decir cuando la clave
llamada no esteen el dicciononario'''
# Aca se muestra musssin pero siempre el valor el valor
# devuelto o almacenado en la funcion tomada por default
# dificult
print(dict_.__missing__('b'))


print('-- Uso del getitem')


''' Cuando la llave no está, la filtrada se muestra este
mensaje que esta en la funcion '''
diccionario = defaultdict(lambda: 'Not present')
diccionario['b'] = 4
diccionario['f'] = 5
diccionario['h'] = 10
print(diccionario.__getitem__('f'))
print(json.dumps(diccionario))
