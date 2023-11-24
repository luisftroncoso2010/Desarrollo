from abc import ABC, abstractmethod, ABCMeta
'''
Clases virtuales
'''
#Creamos una clase
class ClaseA():
    pass

class ClaseB(ClaseA):
    pass
#Comprabos si es ClaseB es una SubClasse de claseA
print(f'Si ClaseB es subclase de ClaseA: {issubclass(ClaseB, ClaseA)}')

print('Ejemplo de clases abstractas registrer')
#Creamos una clase abstracta
class FloatABC(ABC):
    @abstractmethod
    def saludo(self):
        pass
#Registramos la clase FloatABC como abstracta
FloatABC.register(float)
'''
NOTA: Cabe resaltar que registrar de esta manera una clase abstracta con el register()
las clases hijas NO estan obligadas a heredar los metodos abstractos.
Solo se se debe hacer de tal manera que los usar y tratar la clase como abstracta
'''
@FloatABC.register#De esta manera declaramos esta clase como subclase de FloatABC
class Mifloat():
    pass 

print(f'Validamos si Mifloat es SUBCLASE de FloatABC: {issubclass(Mifloat, FloatABC)}')#Retorna True

