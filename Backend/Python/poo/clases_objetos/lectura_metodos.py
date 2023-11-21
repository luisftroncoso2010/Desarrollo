'''
Lectura de metodos de una clase
'''
class Perro:
    #Atributo de clase
    especie = 'Mamifero'    
    #El metodo __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza, pasos):        
        #Atributos de instancia
        self.nombre = nombre
        self.raza = raza
        self.pasos = pasos
    #Metodos    
    def ladra(self):
        print('Guau')
    
    def camina(self):
        print(f'Caminando {self.pasos} pasos')

mi_perro = Perro('Toby', 'Bulldog', 10)
mi_perro.ladra()
mi_perro.camina()

