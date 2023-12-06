'''Principio de responsabilidad unica: Una clase debe tener una 
y unica razon para cambiar. Es decir una sola clase debe tener 
una unica tarea '''
#Creamos la clase para llenar el tanque
class TanqueCombustible:
    def __init__(self):
        #Todos los autos tendran 100 de combustible
        self.combustible = 100
    
    #Creamos el metodo agregar combustible
    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    #Con este metodo obtenemos la cantidad de combustible que hay
    def obtener_combustible(self):
        return self.combustible
    
    #Este metodo resta la cantidad que se le pasa. Por ejemplo de 100 - cantidad(20)
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

#Creamos una clase. auto para usar combustible y llenar el tanque
# Esta clase solo es para mover el auto,
# que nos pide un objeto de tipo tanque
class Auto:
    #Creamos el constructor
    def __init__(self, tanque):
        #Atributos estaticos
        self.posicion = 0   
        #Atributos de isntancia. Este resibe el objeto tanque      
        self.tanque = tanque      
    
    #Creamos el metodo mover el auto.
    #Le decimos la cantidad de distancia que lo queremos mover
    def mover(self, distancia):
        #Si cada qeu ves que     
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2) 
            print('Has movido el auto exitosamente')      
        else:
            print('No hay suficiente combustible')
    #Metodo para obtenr la poscion del auto
    def obterner_pocision(self):
        return self.posicion

#Creamos el objeto tanque de combustible   
tanque = TanqueCombustible()
auto = Auto(tanque)

print(auto.obterner_pocision())
print(auto.mover(10))





            
        
        
