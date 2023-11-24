'''Metodos estaticos. @staticmethod Estos 
metodos nos tienen acceso implicito a las
instacias de la clase. Dado que no resiven
de manera automatica lar eferencia self de la instancia, 
ni cls de la clase'''
#Creamos la clase
class MethodoStatic:
    #Creamos atributos de clase
    __empresa = 'Globant'
    __cargo = 'Developer'   

    #Definimos el constructor de la clase
    def __init__(self, nombre, edad, area, salario, diasTrabajados):
        self.__nombre = nombre
        self.__edad = edad
        self.__area = area    
        self.__diasTrabajados = diasTrabajados
        self.__salario = salario        
    
    def calculo_salario(self):
        if self.__diasTrabajados == 30:
            print(f'Su salario es: {self.__salario}')
            return self.__salario
        else:
            pago = (self.__salario / 30) * self.__diasTrabajados
            print(f'Su salario es: {pago}')
            return pago
    
    #Creamos el emtodo statico
    @staticmethod
    def metodo_estatico():
       return f'Se ha cualculado el salario del empleado'
    #Se crea el metodo str
    def __str__(self):
        salario = self.calculo_salario()
        metodo_estatico = self.metodo_estatico()
        print(metodo_estatico)
        return f'Datos empleado..\n\tNombre: {self.__nombre}\tEdad: {self.__edad}\tArea: {self.__area}\tSalario en Dolares: {self.__salario} Dias Trabajados: {self.__diasTrabajados}\n\tTotal a apagar por dias trabajados es: {salario}'
    
    

trabajadorUno = MethodoStatic('Luis', 26, 'Ux', 2000, 30)
print(trabajadorUno)
