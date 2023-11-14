'''
Modulo sys
'''
import sys
sys.path.append("d:\\Desarrollo\\Backend\\Python\\modulos\\")#Se agrega el modulo a final
print(sys.path)#Aca mostramos nuevamenta para ver que em lugar se almaceno el modulo
import moduloOperaciones
#Me muestra el tipo de modulo. Pro ejemplo este es un modulo tipo built-in
print(sys)
print('Mostramos toodos los nombres de todos los modulos de python')
print(sys.builtin_module_names)#Devuelve una tupla
print('Mostramos la ruta de los modulos')
print(sys.path)#Muestra la ruta de donde estan los modulos
print(f'ModuloOperacion.multiplicacion: {moduloOperaciones.multiplicacion(4, 5)}')
print(f'Modulo principial: {__name__}')#Arroja __main__ por que python sobreescribe el nombre del fichero po la clase main que esl a que inicia
print(sys.builtin_module_names)
print(f'Esto es dir(): {dir()}')
print(f'Fichero .py: {__file__}')#trae la rutas de donde esta ese archivo
print(f'Informacion de lo que contiene ese modulo: {dir(moduloOperaciones)}')

