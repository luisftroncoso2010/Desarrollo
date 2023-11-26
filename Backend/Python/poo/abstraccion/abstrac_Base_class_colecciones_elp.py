'''Abstract Base Clases y colecciones'''
from collections import abc


#Creamos la clase 
class MiSet(abc.Set):
    def __init__(self, iterable):
        self.elements = []
        for value in iterable:
            if value not in self.elements:
                self.elements.append(value)
    
    #Creamoe le metodo especial __iter__
    def __iter__(self):
        return iter(self.elements)
    
    #Metodo contains
    def __contains__(self, value):
        return value in self.elements
    
    #creamos el metodo len
    def __len__(self):
        return len(self.elements)
    
    #Creamos el metodo Strging
    def __str__(self):
        return "".join(str(i) for i in self.elements)
    
# Creamos una instancia de MiSet
mi_set = MiSet([1, 2, 3, 1, 2, 4])

# Imprimimos la longitud del conjunto
print("Longitud del conjunto:", len(mi_set))

# Verificamos si un elemento está presente en el conjunto
print("¿El elemento 3 está en el conjunto?", 3 in mi_set)

# Imprimimos la representación de cadena del conjunto
print("Conjunto como cadena:", str(mi_set))

# Iteramos sobre el conjunto
print("Elementos del conjunto:")
for elemento in mi_set:
    print(elemento)

    

        
        
    
        
    
    