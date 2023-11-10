'''
Funciones de libro
'''
print('--Primer ejemplo--')
def miFuncionUno(uno, dos):
    #Esto se le llama DOCSTRING (Cadena de documentacion)
    '''
    Esta funcion imprime todos los valores por separado
    '''
    print(uno)
    print(dos)
miFuncionUno('Luis', 26)
#Modificar el valor de los parametros, es decir pasarselo por ASIGNACION
miFuncionUno(dos= 'Ana', uno='juan')

print('--Sengudo ejemplo--')
def imprimir(texto, veces=1):
    print(veces * texto)#Se imprime el texto dos veces de seguido con un numero de veces determinado por parametro
imprimir(' Hola luis', 3)#Aca podemos cambiar el valor que tiene la funcion por parametro, es decir modificarla.
#Se imprimira el mismo texto pero 3 veces, dado que se le cambio el valor. 

print('--Varios valores pasado por parametros *ARGS--')
def varios(uno, dos, *varios):    
    return uno, dos, varios
valores = varios(1, 2, 3, 4, 5, 6)       
vA, vB, vC = valores
print(vA)
print(vB)
print(vC)

print('--Varios valores por parametros **KWARS')
def kwars(uno, dos, **varios):
    return uno, dos , varios
valoresKwars = kwars(1, 2, tres=3, cuatro=4, cinco=5, seis= 6, siete=7)
vKwarsA, vKwarsB, vKwarsC = valoresKwars
print(vKwarsA)
print(vKwarsB)
print(vKwarsC)

print('--Añadiento elementos a una lista--')
def f(x,y):
    x = x + 3 #el valor de x pasado por parametro es 22 y de y es [22] en una lista
    y.append(23)
    print(x,y)
x=22#Cuando se salen de la funcion los enteros no conservan el valor, ya que los enteros son inmutables
y=[22]#
f(x, y)
print(x, y)