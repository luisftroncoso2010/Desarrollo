'''
Acoplamiento: Se refiere en la medida que un modulo de clases dependen de otras.
'''
print('Acoplamiento fuerte. Ejemplo 1')
#Creamos la clase Pila (Pila de la calculadora)
class Pila:
    #Creamos el constructor
    def __init__(self):
        self.items = []
    #Creamos metodo de pila vacia, poder validar la pila
    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, x):
        self.items.append(x)
        
    def desapilar(self):
        if self.esta_vacia():
            raise ValueError('La pila esta vacia')
        return self.items.pop()

#Creamos la funcion calculadora
class Calculadora:
    def __init__(self):
        self.pila = Pila()

    def sumar(self):
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        self.pila.apilar(a + b)
    
    def restar(self):
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        self.pila.apilar(a - b)
        
    def multiplicar(self):
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        self.pila.apilar(a * b)
        
    def dividir(self):
        a = self.pila.desapilar()
        b = self.pila.desapilar()
        self.pila.apilar(a / b)
    
# Crear una instancia de la calculadora
mi_calculadora = Calculadora()

# Apilar algunos números
mi_calculadora.pila.apilar(5)
mi_calculadora.pila.apilar(3)
mi_calculadora.pila.apilar
# Realizar operaciones
mi_calculadora.restar()
print(mi_calculadora.pila.items)  

print('Acoplamiento fuerte. Ejemplo 2')
#Creamos la clase 
class clase1:
    x = True#Si lo cambiamos a False, mandara una exepcion
    pass
#Creamos la segunda clase
class clase2:
    def mi_metodo(self, valor):
        if clase1.x:
            self.valor = valor

mi_clase = clase2()
mi_clase.mi_metodo('Hola')
print(mi_clase.valor)
print(clase2.__mro__)#No mostrara una secuencia ya que no hay herencia



