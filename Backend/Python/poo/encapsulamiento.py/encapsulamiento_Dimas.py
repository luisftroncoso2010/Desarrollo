'''
Encapsulamiento.
NOTA: Los metodo protegidos son accesibles desde cualquier parte del codigo,
lo que hace la barrita es colocarlos por convencion y que el metodo o atributo
sea tratado con 'delicadesa'
'''
print('Creamos atributos protegidos')
#Creamos la clase 
class Circulo:
    def __init__(self, radio):
        #Colocamos sola un guien vajo para que sea protegido (Se puede acceder dentro y fuera de la clase)
        self._radio = radio
        self._pi = 3.1415
    
    #Creamos el metodo para calcular el perimetro
    def calculasPerimetro(self):
        return 2* self._pi * self._radio
    
    #Creamos un metodo apra calcular area
    def calcularArea(self):
        return self._pi * self._radio

#Creamos la instancia de la clase
circulo = Circulo(2.5)
print(circulo.calcularArea())
print(circulo.calculasPerimetro())
print(f'La contante pi es: {circulo._pi}')

print('Creamos atributos privados y metodos')

#Creamos la clase 2
class CirculoPrivado:
    def __init__(self, radio):
        #Colocamos dos guiones bajo para que sea protegido (Se puede acceder dentro y fuera de la clase)
        self.__radio = radio
        self.__pi = 3.1415
    
    #Creamos el metodo para calcular el perimetro
    def calculasPerimetro(self):
        return 2* self.__pi * self.__radio
    
    #Creamos un metodo apra calcular area
    def calcularArea(self):
        return self.__pi * self.__radio
    
    #Metodo privado __metodo. Aca por el color me da a entender que no se esta usando
    def __metodo_privado(self):
        return 'Esto es un metodo privado!'

#Creamos la instancia de la clase
circulo_privado = CirculoPrivado(2.5)
print(circulo_privado.calcularArea())
print(circulo_privado.calculasPerimetro())
'''NOTA: Usando esta nomenclatura python DEJA acceder a los metodos
y atributos privados. DE ESTA MANERA → instancia._clase__metodo() o __atributo'''
print(f'La constante pi es: {circulo_privado._CirculoPrivado__pi}')
#Aca mostramos al metodo privado. Sin crear el metodo GET!
print(f'El metodo privado es: {circulo_privado._CirculoPrivado__metodo_privado()}')


print('Creamos atributos privados y metodos publicos. GET')

#Creamos la clase 2
class CirculoPrivadoGet:
    def __init__(self, radio):
        #Colocamos dos guiones bajo para que sea protegido (Se puede acceder dentro y fuera de la clase)
        self.__radio = radio
        self.__pi = 3.1415
    
    #Creamos el metodo para calcular el perimetro
    def calculasPerimetro(self):
        return 2* self.__pi * self.__radio
    
    #Creamos un metodo apra calcular area
    def calcularArea(self):
        return self.__pi * self.__radio    
    
    #Metodo get de pi
    def getPi(self):
        return self.__pi
    
    #Creamos el set para modificar el radio
    def setRadio(self, nuevoRadio):
        #Nos aseguramos de que el nuevo radio sea de tipo int o float
        if type(nuevoRadio) == int or type(nuevoRadio) == float:
            #Nos aseguramos de que el radio sea mayor que cero
            if nuevoRadio > 0:
                self.__radio = nuevoRadio
                #Enviamos mensaje de cambio del radio
                print(f'El radio se ha modificado: {self.__radio}')
            #Enviamos mensaje de que le radio no puede ser menor que cero (0)    
            else: print('El radio no puede ser negativo')
        #Enviamos mensaje de que el radio tiene uqe ser un nuemero y no tipo String
        else: print('El radio tiene que ser un numero positivo')
    
    #Cramos el metodo get radio
    def getRadio(self):
        return self.__radio
        

#Creamos la instancia de la clase
circulo_privado_get = CirculoPrivadoGet(2.5)
print(circulo_privado_get.calcularArea())
print(circulo_privado_get.calculasPerimetro())
print(circulo_privado_get.getPi())#accedemos a pi
circulo_privado_get.setRadio(24)
circulo_privado_get.setRadio(-23)
circulo_privado_get.setRadio('Luis Fernando')
print(circulo_privado_get.getRadio())#Nos mostrara le ultimo valor pasado o seteado
 