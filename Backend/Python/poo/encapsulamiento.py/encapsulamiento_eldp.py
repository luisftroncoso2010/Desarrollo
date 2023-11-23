''' Encapsulamiento '''
#Creamos la clase
class Clase:
    #Creamos un atributo de clase
    atributo_clase = 'Hola'
    
    #Creamos el constructor de clase con su atributo de instacia
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia
        
#Intanaciamos la clase (Creamos el objeto)
mi_clase = Clase('Que tal')
'''NOTA: Este atributos son accedidos desde fuera de la clase
ya que NO son privados'''
print(mi_clase.atributo_clase)
print(mi_clase.atributo_instancia)

print('Segundo ejemplo. Clase Dos')
#Creamos una clase con metodos y atributos privados
class Clase2:
    #Creamoa un atributo de clase publico y uno privado
    atributo_clase2 = 'Hola Clase dos'
    __atributo_clase2 = 'Hola atributo de Clase 2 privado'
    
    #Creamos un metodo NO accesible desde el exterior
    def __mi_metodo(self):
        #NOTA: Este metodo no se puede acceder desde fuera, enviara una ecepsion
        print('Soy un metodo privado. Has algo!')
        self.__variable = 0
        
    #Creamos un metodo accesidble desde el exterior
    def metodo_normal(self):
        #Este metodo si se usa como "get" para mostrar lo que tiene le metodo privado y que se pueda acceder des afuera
        #El método si es accesible desde el interior
        self.__mi_metodo()
        
    #Creamo un metodo publico para acceder a la varible de clase privada. Funciona como get
    def atributo_privado(self):
        return Clase2.__atributo_clase2

#Creamos la instancia de la clase
mi_clase2 = Clase2()   
mi_clase2.metodo_normal()#Manda un error
#Mostramos el atributo de clase con el metodo get
mi_clase2.atributo_privado()
    
print('--Segundo ejemplo. Clase Dos--')
#Creamos la clase
class Wall:    
    #Metodo de instancia y parametros
    def __init__(self, height):
        #Variables de instancia
        self.__height = height
        
    #Metodo get, accede a las variable de instancia
    def get_height(self):
        return self.__height
    
#Instanciamos la clase y pasamos parametros
wall = Wall('20')
#Creamos el objeto
print(wall.get_height())
        
