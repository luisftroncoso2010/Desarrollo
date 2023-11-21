'''
Ejercicio __mro__ y herecia
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def motrar_datos(self):
        print(f'Nombre: {self.nombre}')
        print(f'Edad: {self.edad}')

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        #Aca no se usa la palabra resebada self, ya que la funcion super() trae todo lo heredado
        #Usamos la palabra reserbada self solo si llamamos la clase directamente
        super().__init__(nombre, edad)
        self.grado = grado
    
    def motrar_grado(self):
        print(f'Grado: {self.grado}')
        
estudiante = Estudiante('Juan', '24', '10mo')
estudiante.motrar_datos()
estudiante.motrar_grado()