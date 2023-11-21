'''
Polimorfismo de clase
'''
#Creamos clase 
class Car:
    #Creamos el contructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    #Se crea el metodo que se va a hacer polimorfismo
    def move(self):
        print('Drive!')


#Creamos clase
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    #Se crea el metodo que se va a hacer polimorfismo
    def move(self):
        print('Sail!') 

        
#Creamos clase
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    #Se crea el metodo que se va a hacer polimorfismo
    def move(self):
        print('Fly!')

car1 = Car('Ford', 'Mustang')
boat1 = Boat('Ibiza', 'Touring 20')
plane1 = Plane('Boeing', '747')
#El ciclo iterara 
for x in(car1, boat1, plane1):
    #Podemos ejecutar el mismo metodo para las 3 clases, con los objetos creados
    x.move()

        
    
    
    
        
        