''' Polimorfismo de python '''
#Creamos la clase point:
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    #Creamos el metodo add
    def __add__(self, objeto):
        #Aca se van "almacenando" el primer parametro de la instancia del objeto (Es decir x)
        x = self.x + objeto.x
        #Aca se van "almacenando" el segundo parametro de la instancia del objeto (Es decir y)
        y = self.y + objeto.y
        #Aca se van "almacenando" el tercer parametro de la instancia del objeto (Es decir z)
        z = self.z + objeto.z
        
        return Point(x, y, z)
    
    def __str__(self) -> str:
        return f'Point:\nX = {self.x}\nY = {self.y}\nZ = {self.z}'
        
#Suma point, con dos objetos
objeto1 = Point(10, 5, 2)
objeto2 = Point(2, 3, 2)
objeto3 = Point(2, 3, 1)
#Hacemos la suma de los objetos ya almacenados
resultado_suma_objetos = objeto1 + objeto2 + objeto3
print(resultado_suma_objetos)

