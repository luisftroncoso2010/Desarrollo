'''
Herencia. (el libro de python)

↓↓↓ Herencia normal ↓↓↓
'''
#Clase con su respectivo nombre
class Animal:
    #Constructor
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    #Metodo genérico pero con implementacion particular
    def hablar(self):
        #Metodo vacio
        pass
    #Metodo genérico pero con implementacion particular
    def moverse(self):
        #Metodo vacio
        pass
    #Método genérico con la misma implementación
    def describeme(self):
        print(f'Soy un animal de tipo: {type(self).__name__}')

#Creamos la nueva clase que se va a heredar de animal(Perro)
class Perro(Animal):
    def hablar(self):
        print('Guauu!')
    def moverse(self):
        print('Caminando con 4 patas')

#Creamos la nueva clase que se va a heredar de animal(Vaca)
class Vaca(Animal):
    def hablar(self):
        print('Muuuu!!')
    def moverse(self):
        print('Caminando con 4 patas')
        
#Creamos la nueva clase que se va a heredar de animal(Abeja)
class Abeja(Animal):
    def hablar(self):
        print('Bzzz!')
    def moverse(self):
        print('Volando')
    #Nuevo metodo
    def picar(self):
        print('Picar!')
        
#Creamos los objetos
mi_perro = Perro('Mamifero', 10)
mi_perro.describeme()
mi_vaca = Vaca('Mamifero', 23)
mi_vaca.describeme()
mi_abeja = Abeja('Insecto', 1)
mi_abeja.describeme()
mi_abeja.picar()

'''
Uso del super().
Nos permite acceder a los metos de la clase padre 
desde sus hijas.
'''
class Animales:
    #Creamos le constructor
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    #Creamos los metodos libres
    def hablar(self):
        pass
      
    def moverse(self):
        pass
    
    def describeme(self):
        print(f'Soy un Animal del tipo: {type(self).__name__}')
        
#Creamos la otra clase
class Perros(Animales):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        #Declaramos la varables del constructor
        self.dueño = dueño        
    #Creamos el metodo especial __str__    
    def __str__(self):
    #Cuando se cree el objeto y se imprima, esto es lo que se va a mostrar
        return f'El dueño es: {self.dueño}'
    
mi_perros = Perros('Mamifero', 7, 'Luis')
print(mi_perros)
print(mi_perros.especie)
print(mi_perros.edad)
print(mi_perros.dueño)
mi_perros.describeme()
mis_animales = Animales('Mamifero', 10)
mis_animales.describeme()