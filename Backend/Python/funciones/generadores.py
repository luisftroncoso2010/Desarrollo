'''
Genradores.
Permites extraer valores de una funcion y almacenarlos.
De uno en uno, en objetos iterables (que se pueden recorrer)
Sin la necesidad de almacenar todo a la vez.
Fucinones usando Yeild.
'''

print('--Ejemplo de una funcion normal y un gnerador--')
def funcion():
    return 5

def generator():
    yield 5
print(f'Funcion normal {funcion()}')
print(f'Funcion generador {generator()}')#Me vuelve un objeto de la calse generator
#La funciones GENERADORAS son pausadas

print('Generadores numero')
def generadoresMultiplo7(limite):
    numero = 1
    listaDeNumeros = list()    
    while numero <= limite:
        listaDeNumeros.append(numero * 7)
        numero += 1
    return listaDeNumeros
print(generadoresMultiplo7(10))

print('--Geenrador multiplos 8')

def generadoresMultiplo8(limite):
    numero = 1    
    while numero <= limite:
        yield numero * 8#Parlabra clacve para generar objetos iterables
        numero+=1

obtieneMultiplo8 = generadoresMultiplo8(10)#Se nos imprimo el objeto
print(f'Tipo de objeto iterable {obtieneMultiplo8}')
#Recorremos el objeto iterable de la misma manera NORMAL
print(type(generadoresMultiplo8))
numero =1
for n in obtieneMultiplo8:    
    print(f'{numero} * 8 = {n}')
    numero += 1 
'''
#Obtenemos el valor uno por uno con la funcion next()
print(f'Primer elemento del objeto {next(obtieneMultiplo8)}')#Primer elemento de un objeto iterable
print(f'Segundo elemeto del objeto {next(obtieneMultiplo8)}')#Segundo elemento objeto iterable
#Si quiero mostrar el resto de los elementos iterables, solo es colocar el mensaje
'''

print('--Pasar muchos parametros como tuplas. Yield()--')
def devuelVelenguajes(*lenguajes):
    for leng in lenguajes:
        yield leng

lenguajes = devuelVelenguajes('Python', 'Java', 'Ruby', 'PHP', 'Java Script')
print(next(lenguajes))#Se muestra uno por uno
print(next(lenguajes))

print('--Recorremos letra por letra dentro de la tupla--')
#De esta manera recorreriamos las letras de una tupla, lo ideal seria con 
def devuelveLenguajesDos(*lenguajes):
    for leng in lenguajes:
        for letra in leng:
            yield letra
            
lenguajesTwo = devuelveLenguajesDos('Python', 'Java', 'Ruby', 'PHP', 'Java Script')
print(next(lenguajesTwo))#Recorremos letra por letra
print(next(lenguajesTwo))
print(next(lenguajesTwo))


print('--Recorremos letra por letra dentro de la tupla yield from()--')
#De esta manera recorreriamos las letras de una tupla, lo ideal seria con 
def devuelveLenguajesDos(*lenguajes):
    for leng in lenguajes:
        yield from leng #Permite crear un objeto iterable dentro de otro objeto iterable y asi mismo lo recorre
            
lenguajesTwo = devuelveLenguajesDos('Python', 'Java', 'Ruby', 'PHP', 'Java Script')
print(next(lenguajesTwo))#Recorremos letra por letra
print(next(lenguajesTwo))
print(next(lenguajesTwo))

print('--Iterando generadores--')
def generador():
    yield 5
generador = generador()
print(next(generador))
#print(next(generador))#Generara error por que solo tiene una llamada

print('--Creando Generadores--')

def generadorAumentando():
    n = 1
    yield n
        
    n+=1
    yield n
    
    n+=1
    yield n
generadorAumentandoOne = generadorAumentando()#Usando next

print(next(generadorAumentandoOne))#Muestra 1
print(next(generadorAumentandoOne))#Muestra 2
print(next(generadorAumentandoOne))#Muestra 3

print('--Sin uno del next()--')
def generadorAumentandoDos():
    n = 1
    yield n
        
    n+=1
    yield n
    
    n+=1
    yield n
#Instanciamos nuevamente para acceder a la funcion
generadorAumentandoTwo = generadorAumentandoDos()
for i in generadorAumentandoTwo:
    print(i)
    
print('--Generadores por compresion de listas--')
#Asi se cra una lista normal
lista = [2, 4, 6, 8, 8, 10]
listaCuadrado = [x**2 for x in lista]
print(listaCuadrado)
#Ahora creamos una lista de manera que quede tipo GENERADOR
listaGenerador = (x**2 for x in listaCuadrado)# Estos imprimirá ↓↓↓↓
#→→Lista al cuadrado (listaCuadrado): <generator object <genexpr> at 0x000002EE8FA5BB90>
print(f'Usaremos next para imprimir el primer elemento de (listaGenerador): {next(listaGenerador)}')
print(f'Usaremos next para imprimir el segundo elemento de (listaGenerador): {next(listaGenerador)}')
print('--Imprimir todos los elementos de la lista con ciclo/bucle FOR')
for i in listaCuadrado:
    print(i)