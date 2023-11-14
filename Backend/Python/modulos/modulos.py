'''
Aca importamos los mododulos que hayamos creado
o modulos propios de python.
Usando es "as" podemos darle el nombre al modulo.
Por ejemplo si es muy largo
'''
#Aca importamos el modulo saludar
#Se importa todo el modulo
import moduloSaludar
#Aca se importa el modulo, y solo se escoge los metodos que se quieran de ese modulo
from moduloOperaciones import suma, resta #solamente importamos el metodo suma
#Vamos a importar otro modulo desde una carpeta, de esta manera modulo de carpeta. NombreCaperta.NombreModulo
import archivos.moduloCarpeta as modCarpeta
print('--Trabajamos con el metodo saludar--')
saludo = moduloSaludar.saludar('Ana')
print(saludo)
print(type(moduloSaludar))

print('--Trabajamos con el modulo Operaciones--')
suma = suma(4, 2)
print(f'Modulo Operaciones. Metoda Suma: {suma}')
resta = resta(4, 2)
print(f'Modulo Operaciones. Metodo Resta: {resta}')
print(f'Para ver la porpiedades y metodos del name Space {dir(moduloSaludar)}')
print(f'Muestea el modulo que se esta usando: {moduloSaludar.__name__}')
#Declaramos una variable para instaciar la carpeta
text = modCarpeta.saludarNombre('Luis', 'Troncoso')
print(f'Mostramos el modulo que usaremos con la linea de carpeta {text}')