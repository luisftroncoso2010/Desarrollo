'''
Implementacion de gestores de contexto con decoradores
'''
from contextlib import contextmanager
@contextmanager
def gestor_fichero(nombre_fichero):
    try:
        fichero = open(nombre_fichero, 'w')
        yield fichero
    finally:
        fichero.close()

with gestor_fichero('Fichero.txt') as fichero:
    fichero.write('Hola!')

print('--Anidando diferentes with--')
#Se crea la clase Indice para generadores de indices. 
class Indice:
    #Creamo es constructor
    def __init__(self):
        self.level = -1 #Iniciamos los niveles
        self.numeracion = [0]#Iniciamos la numeracion de cada nivel y se almacena en una lista

    #Creamos el método __enter__ por cada llamada del with
    def __enter__(self):
        self.level +=1#En cada llamada del metodo, el nivel se aumenta en 1
        self.numeracion.append(0)#Se crea la numeracion luego del level
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.numeracion[self.level] = 0#Se sale del with, se reinicia la numeracion
        self.numeracion.pop()#Se elimina la ultima numeracion
        self.level -=1 #Y se elimina la numeracion del elemento actual decrementa en 1, 
        #Ya que en ese momento con otro with va arrancar con el ultimo que quedó
    
    #Se crea el metodo print para programar los niveles y mostrarlos con indices    
    def print(self, text):
        self.numeracion[self.level] += 1#Arrancamos el primet nivel en 1.
        #↓↓Creamos una comprecion de lista, del primer Apartado
        numer = [str(i) for i in self.numeracion[:self.level + 1]]#Creamos una compresion de lista. Va desde la ultima numeracion
        #Creamos el mensaje propio para el SUBNIVEL. Cogemos el iterable (numer) y los concatenamos con el texto(text)
        print(f"{' '*self.level}{'.'.join(numer)} {text}")


#Creamoa las instancias del metodo with. Para que se creen los niveles del indice       
with Indice() as indice:
    indice.print('Apartado')
    #Cada bloque with presenta una seccion o subseccion
    with indice:
        indice.print('Apartado')
        indice.print('Apartado')        
        with indice:
            indice.print('Apartado')
            indice.print('Apartado')
            with indice:
                indice.print('Apartado')
                indice.print('Apartado')
    indice.print('Apartado')
    with indice:
        indice.print('Apartado') 
    
    indice.print('Apartado')
    with indice:
        indice.print('Apartado') 
        indice.print('Apartado') 
        indice.print('Apartado') 
        with indice:
            indice.print('Apartado') 
            indice.print('Apartado') 
            indice.print('Apartado') 
            
    

    