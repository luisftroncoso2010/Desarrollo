from abc import ABC, abstractmethod
''' Principio de Segregación de Interfaces 
(Interface Segregation Principle - ISP) 
Establece que una clase no de debe estar forzada a 
insterfaces que no utiliza
''' 
#Creamos la clase 
class Trabajador(ABC):
    #Creamos los metodos
    @abstractmethod
    def trabajar(self):
        pass
    
        
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass
    
class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass

#Se crea la clase humano
class Humano(Trabajador, Durmiente, Comedor):
    #Creamos los metodos
    def comer(self):
        print('El humano esta comiendo')
    
    def trabajar(self):
        print('El humano esta trabajando')
        
    def dormir(self):
        print('El humano esta dormido')
        
#Se crea la clase Robot
class Robot(Trabajador):
    #Creamos los metodos     
    def trabajar(self):
        print('El Robot esta trabajando')
  
#Instanciamos la clase y imprimimos el objeto       
robot = Robot()
robot.trabajar()

#Instanciamos la clase Humano y imprimimos el objeto
humano = Humano()
humano.comer()
humano.trabajar()
humano.dormir()

        
   
    

