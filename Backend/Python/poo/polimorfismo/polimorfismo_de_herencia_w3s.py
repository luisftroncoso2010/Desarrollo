'''
Polimorfismo de clase de herencia
'''
#Se crea una clase Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print('Move!')

#Se crea otra clase llamada Car
class Car(Vehicle):
    pass

#Se crea otra clase llamada Plane
class Boat(Vehicle):
    def move(self):
        print('Sail!')

#Class plane
class Plane(Vehicle):
    def move(self):
        print('Fly!')
        
#Creamos los objetos de cada clase
car1 = Car('Ford', 'Mustang')#Create a car object
boat1 = Boat('Ibiza', 'Touring 20')
plane1 = Plane('Boeing', '747')

#Creamos un ciclo para iterar los objetos y mostrar las variables que se heredan
for x in(car1, boat1, plane1):
    #Se muestran estas dos variables del objeto por que cada metodo, las muestra
    print(x.brand)
    print(x.model)
    #Se muestra el metodo heredado de la clase principal
    x.move()


        
    
        