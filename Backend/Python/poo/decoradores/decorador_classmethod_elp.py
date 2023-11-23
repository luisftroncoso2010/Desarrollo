'''
ClassMethod
'''
#Creamos la clase
class Clase:
    #Creamos una variable de clase
    __variable = 'Luis'
    #Creamos su constructor
    def __init__(self, sexo, edad):
        #Atributos privados
        self.__sexo = sexo
        self.__edad = edad

    #Creamos el metodo clamethod, tipo get
    @classmethod #Se puede acceder desde afuera sin instaciar la clase o crear el bojeto
    def getAtributodeClase(cls):
       return cls.__variable
    
    '''NOTA: Siempre que se vaya a hacer un cambio o agregar un 
    atributo de clase se debe indicar el decorador @classmethod
    para que python pueda saber que hace referencia a una atributo
    de clase y no una instancia de ella (Objeto). '''
    #Creamosel methodo tipo set 
    @classmethod   
    def setAtributodeClase(cls, nuevoValor):
        cls.__variable = nuevoValor
    
    #Creamos el metodo str
    def __str__(self):
       return f'Los datos recibidos son:\n\tSexo: {self.__sexo}\n\tEdad: {self.__edad}\n\t'

#Creamos la instacia y objeto
clase = Clase('Masculino', 26)
print(clase)

#Con classmethod se puede acceder directamente sin instanciar la clase
print(f'El atributo de clase sin cambiar es: {clase.getAtributodeClase()}')
#Cambiamos el valor atributo de clase
clase.setAtributodeClase('Ana')
print(f'El atributo de clase su nuevo valor es: {clase.getAtributodeClase()}')

