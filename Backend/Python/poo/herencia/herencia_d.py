'''
Herencia simple
'''
#Creamos la primera clase (Padre)
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    #Creamos un nuevo metodo
    def hablar(self):
        print(f'Hola soy {self.nombre}, estoy hablando un poco..')

#Creamos nuestra segunda clase, pasandole por parametro la clase padre    
class Empleado(Persona):
    #Creamos el constructor de esta clase (Hija) herednado de los atributos de la clase padre
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):        
        #Colocamos los atributos a heredar
        super().__init__(nombre, edad, nacionalidad)        
        #Pasamos la identidad de la clase de los atributos
        self.trabajo = trabajo
        self.salario = salario        
    #Definimos el metodo __str__ para mostrar todo lo que le pasamos y armar una estructura
    def __str__(self) :
        return f'El nombre es: {self.nombre}\nLa edad es: {self.edad}\nLa nacionalidad es: {self.nacionalidad}\nSu trabajo es: {self.trabajo}\nSu salario es: {self.salario}'
    
#Mostramos el tipo de elemento que es    
print(type(Empleado))        
#Mostramos y es hija o no, usamos un metodo especial
print(f'Esto muestra las clases hijas: {Persona.__subclasses__()}')
print(f'Esto muestra la clase principal: {Empleado.__bases__}')
roberto = Empleado('Roberto', 45, 'Argentino', ' Profesor', '1000 USD')
roberto.hablar()
print(roberto)
'''
Herencia jerarquica. Cuando varias clases hijas comparten
una clase base (Padre) y comportamientos
'''
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidade = universidad





