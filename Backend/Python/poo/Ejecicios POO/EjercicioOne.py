'''
'''
class Estudiante:
    #Creamos el contructos de la clase
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    #Creamos un metodo que se llame estudiar
    def estudiar(self):
        print('Estudiando....')    
    
#Pedimos estos datos por consola        
nombre = input("Su Nombre: ")
edad = input('Su Edad: ')
grado = input('Su Grado: ')
#Instanciamos la clase y creamos el objeto
estudiante = Estudiante(nombre, edad, grado)
#Mensaje para mostrar atraves del objeto
print(f'''
      Datos del estudiante: \n\n
      Nombre: {estudiante.nombre}\n
      Edad: {estudiante.edad}\n
      Grado: {estudiante.grado}      
      '''   )

while True:
    print('¿Que estas haciendo?')
    estudiar = input()
    if(estudiar.lower() == 'estudiar'):
        estudiante.estudiar()
        break
        



