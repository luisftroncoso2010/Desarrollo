''' Metodos aritmeticos '''
#Creamos la clase
class Aritmeticos:
    #Creamos el constructor
    def __init__(self, nombre, edad, frutas):
        self.nombre = nombre
        self.edad = edad
        self.frutas = frutas    
    #Creamos el metodo str
    def __str__(self) -> str:
        return f'Nombre: {self.nombre}\tEdad: {self.edad}\tFrtuas: {self.frutas}'
    
    #Creamos el metodo suma de objetos
    def __add__(self, objeto):
        sumaNombres = self.nombre + '/' + objeto.nombre
        sumaEdad = self.edad + objeto.edad
        sumaCantidadFrutas = self.frutas + objeto.frutas        
        return Aritmeticos(sumaNombres, sumaEdad, sumaCantidadFrutas)
    
    #Creamos el metodo especial resta
    def __sub__(self, objeto):
        sumaNombres = self.nombre + '/' + objeto.nombre
        sumaEdad = self.edad - objeto.edad
        sumaCantidadFrutas = self.frutas - objeto.frutas        
        return Aritmeticos(sumaNombres, sumaEdad, sumaCantidadFrutas)
    
    #Creamos el metodo especial multiplicacion
    def __mul__(self, objeto):
        sumaNombres = self.nombre + '/' + objeto.nombre
        sumaEdad = self.edad * objeto.edad
        sumaCantidadFrutas = self.frutas * objeto.frutas        
        return Aritmeticos(sumaNombres, sumaEdad, sumaCantidadFrutas) 
    

#Creamos la instacia y el objeto
luis = Aritmeticos('Luis', 26, 80)
leo = Aritmeticos('Leo', 28, 80 )
juan = Aritmeticos('Juan', 40, 80)

#Hacemos la suma y muesta de del metodo add
sumaObjetos = luis + leo + juan
print(sumaObjetos)#Mostreamos los objetos
#Hacemos la resta y muestra de del metodo add
restaObjetos = luis - leo - juan
print(restaObjetos)#Mostreamos los objetos
#Hacemos la multiplicacion y muestra de del metodo add
multiplicacionObjetos = luis * leo * juan
print(multiplicacionObjetos)#Mostreamos los objetos
#Mostramos los objetos
print(luis)
print(leo)
print(juan)
        