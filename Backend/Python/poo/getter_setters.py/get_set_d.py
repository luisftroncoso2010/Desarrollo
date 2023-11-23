'''
Get y Set
'''
#Creamos una clase
class Persona:
    def __init__(self, nombre, edad):
        #Dos guiones bajos para los atributos de la clase y colocarlos privados
        self.__nombre = nombre
        self.__edad = edad
        
    #Para obtener los nombres y edades desde fuera de la clase
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad    
    
    #Creamos el metodo set, para setear para nombre y edad
    '''def setNombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
    def setEdad(self, nuevaEdad):
        self.__edad = nuevaEdad'''
        
    def setNombreEdad(self, nuevoNombre, nuevaEdad):
        self.__nombre = nuevoNombre
        self.__edad = nuevaEdad

#Instanciamos la clase con parametos
personaUno = Persona('Luis', 26)
print(f'Datos en primera instancia:\nNombre: {personaUno.getNombre()}\nEdad: {personaUno.getEdad}')
print('Luego de setearlos')
#Seteamos el nombre y la edad pasamos 
personaUno.setNombreEdad('Ana', 30)

print(f'Ahora estos son los nuevos datos:\nNombre:{personaUno.getNombre()}\nEdad: {personaUno.getEdad()}')  
  
    
    
    