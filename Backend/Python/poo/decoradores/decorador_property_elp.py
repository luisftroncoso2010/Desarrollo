''' Decorador Property.
Puede ser usado para modificar un método para que sea un atributo o propiedad.
'''
#Creamos la clase
class Clase:
    #Contructor de clase e instancia
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo
    
    #Creamos la propiedad
    @property
    def miAtributo(self):
        #El acceso se realiza a través de este 'metodo' y
        #podría contener un codigo extra y no un simple retorno
        return self.__mi_atributo

#Instanciamos la clase, se crea el objeto
miClase = Clase('valor')
#Imprimimos el metodo como si fuese una propiedad
print(miClase.miAtributo)
'''
NOTA: Normalmente sin las propiedades se podia imprimir el 
metodo de esta manera miAtributo(), pero con la ayuda
de las propiedas solo se accede a el como si fuera un 
atributo
'''
print('---Uso del setter como propiedad---')
class Setter:
    def __init__(self, atributo):
        self.__atributo = atributo
    
    #Colocarmos el prpoperti para que sepa que es una propiedad
    @property
    def getAtributo(self):
        return self.__atributo
    
    #A esto se el llama decorador de validacion
    @getAtributo.setter
    def setAtributo(self, nuevoValor):
        #Colocamos comprobaciones antes de asignarle un nuevo valor
        if nuevoValor != "":
            print('Modificando el valor...')
            self.__atributo = nuevoValor
        else: print('Error está vacío sigue siendo el mismo valor')
    
    @getAtributo.deleter   
    def delAtributo(self):
        del self.__atributo
        
    def __str__(self) -> str:
        return f'El valor pasado por parametor en la instacia de la clase cuando se crea el objeto es: {self.__atributo}'

#Creamos la instancia y le pasamos su valor al parametro de clase
setter = Setter('valor')
print(f'El valor del atributo es: {setter.getAtributo}')

#Ahora vamos a darle un nuevo valor al atributo
setter.setAtributo = 'Nuevo valor'
print(f'El nuevo valor del atributo es: {setter.getAtributo}')

#Imprimimos el valor del objeto
print(setter)
#Ahora vamos a elmina la propiedad
del setter.delAtributo
'''NOTA: Si la propiedad se usa luego de esto esto lo mas proble es que haya error
'''




        

        