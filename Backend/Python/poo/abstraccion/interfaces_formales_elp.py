from abc import ABC, abstractclassmethod, ABCMeta
print('---interfaces formales---')
'''Interfaces Formales: Es una manera de crear interfaces'''
#Ejemplo Sencillo
class MandoDos(ABC):
    pass
#Esta otra sintaxis tambien valida
class MandoTres(metaclass=ABCMeta):
    pass

#Uno ejemplo en concreto
#Creamos la clase
class MandoCuatro(ABC):
    #Creamos metodos abstracto
    @abstractclassmethod
    def siguiente_canal(self):
        pass    
    #NOTA: Los metodos que se creen aca ABSTRACTOS debeb ser herados por las sub clases
    @abstractclassmethod
    def canal_anterior(self):
        pass
    @abstractclassmethod
    def subir_volumen(self):
        pass
    @abstractclassmethod
    def bajar_volumen(self):
        pass
'''NOTA: LAs clases abstractar NO se pueden instancias'''    
class MandoSamsungDos(MandoCuatro):    
    #Metodos
    def siguiente_canal(self):
        print('Samsung -> Siguiente')        
    def canal_anterior(self):
        print('Samsung -> Anterior')       
    def subir_volumen(self):
        print('Samsung -> Subir')        
    def bajar_volumen(self):
        print('Samsung -> Bajar') 
        
class MandoLGDos(MandoCuatro):
    #Metodos    
    def siguiente_canal(self):
        print('LG -> Siguiente')        
    def canal_anterior(self):
        print('LG -> Anterior')       
    def subir_volumen(self):
        print('LG -> Subir')        
    def bajar_volumen(self):
        print('LG -> Bajar')

#Instanciar mando Samsumg
mando_samsumg_dos = MandoSamsungDos()
mando_samsumg_dos.bajar_volumen()
#Instanciar mando LG
mando_lg_dos = MandoLGDos()
mando_lg_dos.bajar_volumen()

