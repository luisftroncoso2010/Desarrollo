'''
Encapsulamiento
'''
class Miclase:
    def __init__(self) :
        self.__atributo_privado = 'Valor'

objeto = Miclase()
print(objeto._atributo_privado)