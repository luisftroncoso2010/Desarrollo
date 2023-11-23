'''
Decorador property. Getter, Setters y Deletters
'''
#Creamos la clase
class Persona:
    #Definimos el constructor
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    #Cremoa el metodo get de nombre
    @property #Lo que hace esto es pasar elmetodo como si fuera un propiedad
    def get_Nombre(self):
        return self.__nombre
    
    #Aca pasamos el nombre de la propiedad get_Nombre
    @get_Nombre.setter
    def setNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
    
    #Eliminar el valor de la propiedad
    @get_Nombre.deleter
    def delNombre(self):
        del self.__nombre
        
     #Creamos un metodo __str__
    def __str__(self):
        return f'El nombre: {self.__nombre} Edad: {self.__edad}'  
        

#Creamos el objeto
personaOne = Persona('Luis', 22)
personaTwo = Persona('Ana', 24 )
#Imprimimos los Objeto
print(personaOne)
print(personaTwo)

print(personaOne.get_Nombre)#Mostramos el nombre del objeto, atraves de la propiedad y no como un metodo
#Ahora mostramos la propiedad para setear.
personaOne.setNombre = 'Leo'#Aca ya no se paso por parametro, no se le asigna un valor
print(personaOne.get_Nombre)
#Aca usamor del, para eliminar propiedad
del personaOne.delNombre 
'''NOTA: No se podra hacer uso de la propiedad, dado de que no existe '''


         