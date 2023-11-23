''' Encapsulamiento '''
#Cramos una clase
class Miclase:
    def __init__(self) :        
        ''' NOTA: Los atributos privados en python con un solo guion
        bajo en python, NO EXISTEN, solo se manejan por convencion.
        Es decir, tener para el guion bajo _ uno solo para que tener
        cuidado con eso 
        '''
        self._atributo_privado = 'Valor'
        
    #Esto es un metodo privado
    def __hablar(self):
        return 'Hola Luis'

objeto = Miclase()
print(objeto._atributo_privado)
objeto.__hablar()#Es objeto no dejara acceder ya que es un atributo privado