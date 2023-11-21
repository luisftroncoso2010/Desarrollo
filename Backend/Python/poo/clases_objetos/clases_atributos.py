'''
Vamos a crear una clase con un atributo de instancia
'''
class Perro:
    #Variable de clase
    especie = 'Mamifero'
    
    #El metodo __init__ es llmado al crear el objeto
    def __init__(self, nombre, raza):
        
    #Ahora creamos los atributos de instancia
        self.nombre = nombre
        self.raza = raza
    #Esta fucnion nos crea de como se va a mostrar el objeto de la clase
    def __str__(self):
        return(f' Creando perro {self.nombre}, {self.raza} ')
    
#Creamos el objeto
dogOne = Perro('Toby', 'Bulldog')
#Imprimimos las variables de la clase
print(dogOne.nombre)
print(dogOne.raza)
#Podemos mostrar la variable de clase dado que no es un atributo de la clase
print(Perro.especie)
#Imprimimos el metodo de desde dodne se ejecuta 
print(type(dogOne))
