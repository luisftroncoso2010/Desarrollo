'''Principio de susticion de Liskov. Garantiza que las clases 
derivadas (Subtipo) debe poder ser sustituido por un objeto de su
clase base (Super tipo) sin afectar la integridad del programa'''
#Creamos la clase. (Super tipo)
class Rectangulo:
    #Cremaos el constructor
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
    
    #Creamos el metodo para calcular su area
    def calcular_area(self):
        return self.ancho * self.altura
    
#Creamos la calse derivada (Subtipo)
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
        
    #Sobre escribir el metodo para poder cumplir el principio de Liskov
    def calcular_area(self):
        return self.ancho * self.altura

#Metodo para poder calcular el area      
def imprimir_area(rectangulo):
    print(f'Área: {rectangulo.calcular_area()}')
    
#Creamoa un objeto de tipo cuadrado
cuadrado = Cuadrado(4)
#Se intenta imprimir el cuadrado donde se espera el Rectangulo
imprimir_area(cuadrado)

print('--Otro ejemplo Ave--')
#Creamos la clase ave, volar
class Ave:
    def volar(self):
        print('El ave está volando')
        
#Class pinguno, con el metodo volar        
class Pinguino(Ave):
    def volar(self):
        print('Los principios no pueden volar, pero son excelentes nadadores')

#Creamos el metodo para usar los objetos
def realizar_vuelo(TipoAve):
    ave.volar()

#Crear un objeto Pinguino
pinguino = Pinguino()
ave = Ave()

#Utilizar el pinguino en lugar de aves.
realizar_vuelo(ave)

print('--Otros ejemplo Frutas--')
#Creamoa la clase base
class Fruta:    
    def obtener_color(self):
        return "Desconocido"
    
class Manzana(Fruta):
    def obtener_color(self):
        return "Manzana Roja"
    
class Pera(Fruta):
    def obtener_color(self):
        return 'Pera Verde'

def mostrarColor(fruta):
    print(f'El color de la fruta es: {fruta.obtener_color()}')
    
#Aca creamos los objetos y los usamos de igual manera
manzana = Manzana()
pera = Pera()

#Utilizando las frutas
mostrarColor(manzana)
mostrarColor(pera)

''' IMPORTANTE: ↑↑ Aca es donde se obeserva el LSP, se sustituye
el objeto y duncionan de igual manera
'''

    
    

    
    