'''
Creacion de personajes
'''
#Creamos la clase
class Personaje:
    #Creo el contructor de la clase para ser instanciado y crear los objetos
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
    
    #Creamos el metodo repr
    def __repr__(self) -> str:
        return f'Fucion: {self.nombre}\tFuerza: {self.fuerza}\tVelocidad: {self.velocidad}'
    
    #Creammos el metodo de suma de objetos
    def __add__(self, addObjeto):
        nuevoNombre = self.nombre + '/' + addObjeto.nombre
        nuevaFuerza = round(((self.fuerza + addObjeto.fuerza)/2)**1.34)
        nuevaVelocidad = round(((self.velocidad + addObjeto.velocidad)/1.34)**1.5)
        return Personaje(nuevoNombre, nuevaFuerza, nuevaVelocidad)
        
goku = Personaje('Goku', 100, 100)
vegueta = Personaje('Vegueta', 99, 99)
gojan = Personaje('Gojan', 80, 80)
gogueta = goku + vegueta + gojan
print(gogueta)
print(goku)
print(vegueta)
print(gojan)

        