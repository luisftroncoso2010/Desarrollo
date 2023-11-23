'''
Polimorfismo...
'''
print('Polimorfismo de clase....')
class Gato():
    def sonido(self):
        return 'Miauu!'

class Perro():
    def sonido(self):
        return 'Guau'
    
def hacer_sonido(animal):
    print(animal.sonido())
    
#Instanciamos la variable y se crea el objeto. 
gato = Gato()
perro = Perro()
hacer_sonido(gato)
print(gato.sonido())
print(perro.sonido())

print('Polimorfismo de funcion....')
#Pasamos la instancia de la clase por parametro
hacer_sonido(gato)
hacer_sonido(perro)

print('Iteramos lo objetos y mostramos el mismo metodo():')
for i in (gato, perro):
   print(i.sonido())

print('Polimofismo de tipo. (Type())')
numberOne = 3 #Tipo de dato int
numberTwo = 4.3#Tipo de dato float
suma = numberOne + numberTwo
print(f'La suma es: {suma}')
'''
NOTA: Aca python para sumar dos numeros, unos de tipo
int y otro se tipo float, aplica la cohecion automatica.
Pasa a tipo float el numero entero y imprime uno de tipo
float.

Poliumorfismo: Dos tipos de datos, mismo resultado
'''
print(f'El tipo de datos de la suma es: {type(suma)}')

print('Recorrer una lista de numeros, listas datos, un string')
def recorrer(elemento):
    for item in elemento:        
        print(f'El elemento actual es: {item}')
'''
Aca se aplica el polimorfismo, dado que es la MISMA FUNCION 
diferente dato y funciona igual
'''           
lista = [1,2,3,4]
lista2 = ['Maquina', 'Como', 'Andas']
string = 'Hola luis'
#Recorremos la lista[]
recorrer(lista)
#Recorremos lista2[]
recorrer(lista2)
#Recorremos un string
recorrer(string)

#Duck typing
'''Se basa en la idea de qeu la idoneidad de un objeto 
para una tarea no se determina por su tipo, si no por que 
tiene ciertos métodos o atributos uniformes '''
''' La idoneidad de un objeto se evalua en funcion si tiene metodos,
atributos o comportamientos necesarios para cumplir con ciertos propositos '''
#Enlaces dinamicos y Estaticos
'''Enlaces dinamicos: Aqui los modulos o bibliotecas se cargan en tiempo
de ejecucion del codigo. Esto significa que puede importar modulos desde
cualquier parte de tu codigo y ejecutar funciones de eso modulos sin la
necesidad de recompilar el codigo, mientras que en los enlaces dinamicos 
la idea es importar lo modulos en la primera parte del archivo, antes de
ejecutar cualquier codigo, para mejorar la legibilidad y para indicar 
claramente las dependencias. 
'''
#Tipo real y declarado
'''
Por ejemplo en clases, el tipo real es la clase (Clase padre en herencia) y 
declarado es la instancia de esa clase que se crea 
'''