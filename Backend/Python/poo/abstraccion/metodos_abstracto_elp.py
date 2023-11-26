#improtamos el modulo abc
from abc import ABC, abstractmethod, abstractproperty
''' Metodos abtractos '''
#Creamos la clase ABC
class Clase(ABC):
    #Creamos el emtodo abstracto
    @abstractmethod
    def metodo_abstracto(self):
        pass

'''
NOTA: Tambien podemos combinar el decordor @abstractmethod
con los decoradores @classmethod y @staticmethod, a parte
crear metodos de propiedad
'''
class ClaseDos():
    #Creamos el metodo abstracto de clase. 
    # Para poder trabajar con atributors de clase abstractos
    @classmethod#Este va de primero
    @abstractmethod
    def metodo_abstracto_de_clase(cls):
        pass

    #Creamos un metodo statico de clase abstracto
    @staticmethod#Este metodo no permite relizar modificaciones, ni de clase. Ni del objeto
    @abstractmethod
    def metodo_abstracto_estatico():
        pass
    
    #Creamos un metodo de propiedad abstracto o importando la clase del modulo ABC
    @property    
    @abstractmethod
    def metodo_abstracto_propiedad(self):
        pass
    #Creamos un metodo abstracto como propiedad
    @abstractproperty
    def metodo_abstracto_propiedad(self):
        pass
    
    
