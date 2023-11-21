''' Clases objetos '''
class Celular:
    #Atributos estaticos. Se pueden modificar fuera de la clase
    marca = 'Samsumg'
    modelo = 'S23'
    camara = '48MP'
    #Creamos el contructor de la clase
    def __init__(self, marca, modelo, camara):
        ''' En Python, «self» es una convención que se utiliza 
        como nombre para el primer parámetro de un método en una clase.
        El objetivo de «self» es hacer referencia al objeto que se 
        está manipulando cuando se llama al método. '''
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    #Creamos el metodo String para mostrar
    def __str__(self):
        return f'La marca es: {self.marca}\nEl modelo es: {self.modelo}\nLa camara es: {self.camara}'    
    
    #Creamos metodos
    def llamar(self):
        print(f'Es haciendo un llamado desde un: {self.modelo}')
    #Otro metodo
    def cortar(self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')    
    
#Objetos
phoneOne = Celular#Instanciar la clase. (Los objetos son instancias de una clase)
#De esta manera se acceder a los metodos de 
print(phoneOne.marca)
print(phoneOne.modelo)
print(phoneOne.camara)
phoneTwo = Celular('Apple', 'Iphone 14Pro', '48MP')
print(phoneTwo)