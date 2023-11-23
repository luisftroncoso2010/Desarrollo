'''
Metodos en python:
* Intancia * De clase * Estaticos
'''
#Creamos una clase donde definimos los diferentes tres tipos de metodos
class Clase:
    #Metodo normal
    def metodo(self):
        return 'metodo normal', self
    #Metodo de clase
    @classmethod
    def metodoClase(cls):
        return 'Metodo de clase', cls
    
    #Metodo estatico
    def metodoEstatico():
        return 'Metodo estático'

print('--Metodo de instancia--')   
class ClaseInstancia:
    def metodo_instancia(self, argumentoOne, argumentoTwo):
        return 'Metodo normal', self    
    
#Cramos el objeto atraves del metodo de instancia
miClase = ClaseInstancia()
miClase.metodo_instancia('a', 'b')
print(miClase)
