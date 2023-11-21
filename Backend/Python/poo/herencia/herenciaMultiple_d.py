'''
Herencia multiple 
'''
#Herencia multiple. Clase principal (Padre)
class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print(f'Soy {self.nombre}, estoy hablando un poco')
 
#Otra clase padre        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
                
    def MostrarHabilidad(self):
        print(f'Mi habilidad es: {self.habilidad}') 

#Clase hija
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    #Creamos un metodo PROPIO DE LA CLASE
    def MostrarHabilidad(self):
        return 'No tengo habilidad'    
    '''
    NOTA: Usando la palabra reserbada self, se llama el motodo propio de
    la clase, mientra que usando el metodo super() llamamos el metodo de la
    clase padre
    '''
    #Creamos un metodo presentarse
    def presentarse(self):
        print(f'Hola soy {self.nombre} y Mi habilidas es: {self.MostrarHabilidad()} y trabajo en {self.empresa}') 

roberto = EmpleadoArtista('Roberto', 26, 'Brazil', 'Actor porno', 15000, 'Pornhub')
roberto.presentarse()

#Para saber si es una subclase (Hija) de una clase (Padre)
herencia = issubclass(EmpleadoArtista, Artista)#Devolvera True si lo es Y False si no lo es
print(herencia)

#Para saber si es instancia de una clase (Obejto de clase)
instacia = isinstance(roberto, Artista)#Devuelve true
print(instacia)

    