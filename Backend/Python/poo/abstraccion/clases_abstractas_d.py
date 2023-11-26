''' Clases abstractas: NO SE PUEDEN INSTANCIAR '''
from abc import ABC, abstractmethod, ABCMeta
#creamos la clase
class Personaje(ABC):#Creamos la clase abstracta
    #Creamos el constructor
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = list()
        self.vida = 100
    
    #Creamos el metodo atacar. Se deja vacio, lo van a 
    # sobre escribir las subclases
    @abstractmethod    
    def atacar(self, obejetivo):
        pass
    
    #Creamos el metodo para mostrar los datos
    @abstractmethod
    def getStatus(self):
        print(f'Nombre: {self.nombre}\tNivel: {self.nivel}')
    
    #Subir de nivel. No se va a sobre escrbiir   
    def subirDeNivel(self):
        self.nivel +=1
     
    #Informara lo objetos que tenga cada personaje  
    def verInventario(self):
        print(f'Inventtario de {self.nombre}')
        for objeto in self.inventario:
            print(objeto)
            
#Cramos clase de personaje
class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 180
        self.inteligencia = 95
        self.inventario = ['Pocipón de maria', "Grimorio"]
    
    def getStatus(self):
        print(f'{self.nombre} es de la clase Mago') 
        super().getStatus()#Extendemos el medoto de la clase padre
        
    def atacar(self, obejetivo):
        obejetivo.vida -= self.inteligencia
        print(f'La vida actual de objetivo es: {obejetivo.vida}')
        
    def saludar (self):
        print('Hola soy un mago!')
        
        
#clase guerrero
class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 60
        self.inventario = ['Poción de vida', 'Escudo', 'Espada']
    
    def getStatus(self):
        print(f'Clase guerrero')
        super().getStatus()
        
    def atacar(self, obejetivo):#El objetivo es el objeto que se le pasa
        #Al momento de pasa le objeto creado (Este objeto es el objetivo)
        obejetivo.vida -= self.fuerza
        print(f'El objetivo se quedado con {obejetivo.vida} puntos de vida')
        
guerrero = Guerrero('Kaladin')
mago = Mago('Yuno')

guerrero.getStatus()
mago.getStatus()

mago.atacar(guerrero)
guerrero.atacar(mago)
          
print('---Clases abstractas dalto---')
#Creamos la clase 
class Persona(ABC):
    #Creamos el constructos de la clase abstracto
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    #Creamos un metodo abstracto    
    @abstractmethod
    def hacer_actividad():
        #Este metodo se deja vacio, por que cada persona puede trabajar de una manera diferente
        pass 
    
    def Presentarse(self):
        print(f'Hola, me llamo: {self.nombre} y tengo {self.edad}')
 
#Creamos la clase estudiante    
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    #Actividad del estudiante
    def hacer_actividad(self):
        print(f'Estoy estudiando: {self.actividad}')


#Creamos la clase Trabajador
class Trabajador(Persona):
    #Creamos el contructor que hereda de Persona
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f'Actualmente estoy trabajando en el curso de: {self.actividad}')

pedrito = Estudiante('Pedrito', 26, 'Masculino', 'Programacion')        
dalto = Trabajador('Luis', 26, 'Masculino', 'Python Avanzado')  

pedrito.Presentarse()
pedrito.hacer_actividad()
dalto.Presentarse()
dalto.hacer_actividad()
      
    
