'''
Acoplamiento: Se refiere en la medida que unas clases dependen de otras.
'''
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




