'''
Generar una excepsion. 
Como desarrollador de python, puede optar 
por generar una excepción si se cproduce una
condición. Para lazar o generar una excepción, 
use la plabra raise, palabra clave
'''
x = -1
if x < 0:
    raise Exception('Sorry, no numbers below zero')

print('Generar un error')
strign = "Hello"

if not type(strign) is int:
    #Con raise se genera un error a proposito de la mano con TypeError
    raise TypeError('La variable strign no es de tipo entero')
