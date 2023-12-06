''' Python tiene varias secciones incorporadas que se
pueden usar con bloques "try-except" '''
import pandas as pd
print('--ZeroDivisionError--')
#ZeroDivisionError: Se ejecunata ucnado se intenta dividir un numero por cero.
a = 12
b = 2
resultado = a/b #Esdto arrojara una division entre 0

print('--TypeError--')
#TypeError: Si se hace una operacion con un dato que no es el apropiado
datoUno = int(input('Dato Uno: '))#Escribe de tipo string, arrojara la excepsion
datoDos = int(input('Dato Dos: '))
datoInpropiado = (datoUno / datoDos)

print('--ValueError--')
#ValueError: Cuando una funcion recibe un argumento del tipo correcto pero con un valor incorrecto
try:
    int('asvsvac')#Esto generara la excepsion, ya que el tipo de dato que almanena la duncion es String y no int 
except ValueError as e:
    print(f'Este es el error: {e}')
else: 
    print('Se ejecuto correctamente')

print('--IndexError--')
#IndexError: Cuando se intenta acceder a un indice que esta fuera del rango de una lista o secuencia
lista = [1, 2, 3, 4, 5]
print(lista[4]) #Si se coloca un indice fuera de la secuencia lo arrojará 

print('--KeyError--')
#KeyError: Cuando una clase que no exite en un diccionario
diccionario = {'Nombre': 'Luis', 'Edad': 26}
for clave, valor in diccionario.items():#Mostramos clves y valor
    print(clave, valor)
diccionario['Edad']#aca arroja el error ya que no se puede, por que no existe dicha clase

print('--FileNotFoundError--')
#FileNotFoundError: Cuando se intenta abrir un archivo que no existe
#read = pd.read_csv('luis/2020')#Como esta archivo no existe se generara una excepsion

print('--NameError--')
#NameError: Cuando intenta acceder a una variable o funcion que no esta definida
#print(y)#si colocamos aca una funcion o variable sin definir aparecerá la excepsion

print('--AtributeError--')
#AtributeError: Cuando intentas acceder a un atributo que no existe en un objeto.
class Prueba:
    mi_variable = 1
    def prueba():
        print('Esto es una preuba')
prueba = Prueba()
#print(prueba.ana())#Generará la excepsion. Ya que el metodo no exite

print('--IOError--')
#IOError: Cuando intentas abrir un archivo que no existe. Aqui tienes un ejemplo
try:
    #Intenta abrir un archivo que no existe
    with open("archivo_inexistente.txt", 'r') as archivo:
        contenido = archivo.read()
except IOError as e:
    #Manejo especifico para la excepción IOError
    print(f'Error de operaciones de entrada/salida: {e}')
else:
    #Este bloque se ejecutará si no hay excepciones
    print(f'Contenido del archivo: {contenido}')
finally:
    #Este bloqeuse ejecutará siempre haya o no haya errores
    print('Finalizando el lboque try-except')

print('---ImportError---')
#ImportError: Se levanta cunado un error al importar un modulo
import pan

        

    


