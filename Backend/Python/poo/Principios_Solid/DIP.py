from abc import ABC, abstractmethod
'''Principo de inversion de dependencias: Los modulos de alto
nivel NO deben depender de los de bajo nivel. Ambos deben 
depende de las abstracciones y las abstracciones no deben depender
de los detalles, si no los detalles de las abstracciones. Es decir, 
no depender de implementaciones especificas, depender de intercafes 
mas complejas'''
class Diccionario:
    def verificar_palabra(self, palabra):
        #logica para verficar palabras
        pass

#Esta clase acude al error del principo, ya que la clase hija
#Es mucho mas grande y complejas. Es decir, esta clase es mas
#importante de la clase padre.   
class CorrectorOrtografico():
    def __init__(self):
        #Esto tendra un objeto de tipo diccionario.
        #Esta variable, resibe un obejto de tipo diccionario
        self.Diccionario = Diccionario()
    
    def corregir_texto(self, texto):
        #Usammos el diccionario para corregir el texto
        pass
    
print('Se hace cumpliendo el Principio de inversion de dependencias')
class verificadorOrtografico(ABC):
    @abstractmethod
    def verificadorDePalabras(self, palabras):
        pass
    

class Diccionario(verificadorOrtografico):
    def verificadorDePalabras(self, palabras):
       #Logica para verificar palabras si esta ne el diccionario
       pass
       
class Corrector_Ortografico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self):
        #Usamos el verificador para corregir texto
        pass
    
print('--Principio de inversion de dependencias--')



        
    
    
    
    