
'''
Ejercicio __mro__. Averiguar patrones
'''
class Animal:
    def Comer(self):
        print('El animal es perfecto')

class Ave(Animal):
    def Volar(self):
        print('El esta volando')
        
class Mamifero(Animal):
    def Amantar(self):
        print('El animal esta amamantando')

class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()
murcielago.Comer()
murcielago.Amantar()
murcielago.Volar()