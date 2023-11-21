'''
Metodo MRO, metodo de resolucion de orden
'''
#Ejemplo #1. Primera clase
class ClaseUno:
    pass
#Segunda clase
class ClaseDos:
    pass
#Tercera clase que hereda de las anteriores
class ClaseTres(ClaseUno, ClaseDos):
    pass
#Genera una tupla con el orden de busqueda de los metodos. Tambien tiene encuenta el orden en que se le pasa por parametro
print(ClaseTres.__mro__)
'''
Herencia multiple profunda
'''

class Clase1:
    pass

class Clase2(Clase1):
    pass

class Clase3(Clase2):
    pass
print(Clase3.__mro__)

'''
Otro ejemplo __mro__
'''
class A:
    def hablar(self):
        print('Hola desde A')
        
class F:
    def hablar(self):
        print('Hola desde F')
        
class B(A):
    def hablar(self):
        print('hola desde B')
        
class C(F):
    def hablar(self):
        print('Hola desde C')

class D(B, C):
    def hablar(self):
        print('hola desde D')

#Creamos el objeto
d = D()
'''NOTA: Si queremos llamar al metodo de una clase, se llama 
el metodo que comparten y luego el objeto creado'''
F.hablar(d)
print(D.__mro__)