''' Abstraccion. Coloquialmente, es ocultar la complegidad
interna de un sistema. La capacidad de representar concetos
complejos y datosde manera simplificada, encapsulando los detalles 
innecesarios '''
#Creamos la clase
class Auto():
    #Creamo el constructor
    def __init__(self):
        self._estado = 'apagado'
        
    def encender(self):
        self._estado = 'Encendido'
        print('El auto esta encendio')
     
    def conducir(self):
        
        if self._estado == 'apagado':
            self.encender()
            print('Conduciendo auto..')
        
mi_auto = Auto()
mi_auto.conducir()
'''
NNOTA: No necesitas saber como funciona, si no como usarlo.
'''          
        
        
    
    
    