''' Metodos especiales '''
#Creamos la clase
class Persona:
    #Creamos  
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    #Cuando se llama solo albojeto, esto se mostrara en pantala   
    def __str__(self):
        return f'Nombre: {self.nombre}\tEdad: {self.edad}\tSexo: {self.sexo}'
    
    #Hace lo mismo que el metodo str. Cuando str y repr estan en la misma clase<
    #Amso trabajan en conjunto, es decir, str toma lo de repr y lo muestra
    def __repr__(self) -> str:
        #Aca los strings se deden de colocar entre comillas
        return f'Persona("{self.nombre}", {self.edad}, "{self.sexo}")'
    
    #Cremoa el metodo add. Sumaremos la edades del objeto
    def __add__(self, objeto): 
        nombre = self.nombre + ', '  + objeto.nombre
        edad = self.edad + objeto.edad    
        sexo = self.sexo + ', '  + objeto.sexo    
        return  Persona(nombre, edad, sexo)
#Instanciamos la clase (Creamos el objeto)
dalto = Persona('Lucas', 21, 'Masculino')
pedro = Persona('Pedro', 50, 'Masculino')
luis = Persona('Luis', 26, 'Masculino')
#Sumamos las edades de los objetos
sumaObjetoEdad = dalto + pedro + luis
print(sumaObjetoEdad)
#Instanciamos la representacion con el objeto. 
# Se obtiene la instacia de la cadena usando repr
repre = repr(dalto)
#Se usa eval para recrear la instanciade la clase desde la cadena
resultado = eval(repre)
print(resultado)
#Validamos que la instancia de la cadena sea del mismo tipo
print(isinstance(resultado, Persona))
#Aca podemos acceder a los datos del objeto
print(resultado.nombre)#De esta manera accedemos a los atributos de instancia
print(resultado.edad)
print(resultado.sexo)