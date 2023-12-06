from abc import ABC, abstractmethod
''' Principio abierto cerrado (Open/Close Principle OCP). Se establece 
que las entidades de software (Clases, módulos, funciones etc.) deben
estar abierta para la extensión y cerradas para la modificacion. Lo que
significa  que las clases deben ser extendidadas agregar nuevas funcionalidades 
sin modificar su codigo fuente original '''
#Creamos la clase Abstracta.
#Sistema que maneja diferentes tipos de productos y se 
#necesita calcular el precio total de una lista de productos
class Producto(ABC):
    @abstractmethod
    def calcular_precio(self):
        pass

#Creamos el primer tipo de producto
class Camiseta(Producto):
    def __init__(self, precio):
        self.precio = precio
        
    #Sobre escribimos el metodo abstracto de la clase padre
    #Este metodo guarda los precios de los objetos (Preducto)
    def calcular_precio(self):
        return self.precio
    
#Creamos el segundo tipo de producto 
class Libro(Producto):
    def __init__(self, precio):
        self.precio = precio  
          
    #Sobre escribimos el metodo abstracto de la clase padre
    #Este metodo tendra lep recio de los preductos      
    def calcular_precio(self):
        return self.precio
    
#creamos un tercer tipo de producto
class Jean(Producto):
    #Creamos el constructor
    def __init__(self, precio):
        self.precio = precio        
        
    def calcular_precio(self):
        return self.precio


#creamos el metodo que va a calcular los precios de los productos       
class CalculadoraDePRecios:
    def calcular_total(self, productos):
        total = 0
        for producto in productos:
            total += producto.calcular_precio()
        return total

#Creaos el pobjeto de productos
camiseta = Camiseta(10)
sueter = Camiseta(40)
libro = Libro(30)
revista = Libro(40)
jeanSkini = Jean(10)
jeanSuperSkyni = Jean(40)

#Calculamos el proecio
calculadora = CalculadoraDePRecios()
total = calculadora.calcular_total([camiseta, sueter, libro, revista, jeanSkini, jeanSuperSkyni])
print(f'El precio total es. {total}')

    
        
        
        
         
        