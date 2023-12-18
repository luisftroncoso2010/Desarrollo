''' Python PEP8: Escribiendo Código facil de Leer '''


def mi_funcion_suma(a, b, c, imprime=True):
    resultado = a + b + c
    if imprime:
        print(resultado)
    return resultado


a = 4
variable_b = 5
var_c = 10

mi_funcion_suma(a, variable_b, var_c)

''' Organización del código '''


class ClaseA:
    def metodo_a(self):
        pass

    def metodo_b(self):
        pass


class ClaseB:
    def metodo_a(self):
        pass

    def metodo_b(self):
        pass


def funcion():
    pass


''' Separar con una linea diferentes funcionalidades '''


def calcular_media_mediana(valores):
    '''Calcular la media'''
    suma_valores = 0
    for valor in valores:
        suma_valores += valor
    media = suma_valores / len(valores)

    '''Calculamos la media'''
    valores_ordenados = sorted(valores)
    indice = len(valores) // 2
    if len(valores) % 2:
        mediana = valores_ordenados[indice]
    else:
        mediana = (valores_ordenados[indice]
                   + valores_ordenados[indice + 1]) / 2

    return media, mediana


''' Uso de espacios en blanco: Operadores de asignacion '''


x = 5
if x == 5:
    pass


'''Con funciones con argumentos por defecto no, debemos dejar espacios'''


def mi_funcion(parametro_por_defecto=5):
    print(parametro_por_defecto)


'''NO dejar espacios dentro del paréntesis y tampoco dentro de ()'''


def duplica(*a):
    return a * 2


duplica(2)
lista = (1, 2, 3)


'''Los espacios resulta util cuando se combina varios operaderes y variables.
Por orden de mayor prioridad'''


y = x**2 + 1
z = (x-y) * (x+y)
if x > 0 and x % 2 == 0:
    print('...')


'''NO usar espacios antes del índice o entre el ídice y los []'''
lista[0]
lista[1]


''' También se puede identar el código para evitar tener líneas muy largas.
Resultan difíciles de leer. PEP8 limita los caracteres a 79 '''


def mi_funcion_dos(primer_parametro, segundo_parametro, tercer_parametro,
                   cuarto_parametro, quinto_parametro):
    print('Python')


''' Operaciones largas '''
variable_a = 0
variable_c = 0
variable_d = 0
variable_e = 0
variable_f = 0
income = (variable_a
          + variable_b
          + (variable_c - variable_d)
          + variable_d
          + variable_e
          + variable_f)


''' Todo un codigo bien estructurado con variables '''


'# mi_script.py'
CONSTANTE_GLOBAL = 10


class MiClase():
    def mi_primer_metodo(self, variable_a, variable_b):
        return (variable_a + variable_b) / CONSTANTE_GLOBAL


mi_objeto = MiClase()
print(mi_objeto.mi_primer_metodo(5, 5))


'''Los Modulos:
* Deben ir al pricipio del fichero
* Después de comentarios del módulo docstrgings
* Antes de los global y las constantes
'''
'# Importando paquetes, siempre se colocan en el inicio del archivo SIEMPRE'
import os

'''Orden de modulos/Librerias:
* Primeor las Estándar.
* Segundo las librerías Externas
* Tercero las librerías Locales
'''
'# Imprtando paquetes de una misma libreria'
from subprocess import Popen, PIPE


'# Comas al final de lal inea. se usa en tuplas cuando es de un solo valor'
tupla = (1,)  # Aca la coma es opcional
print(tupla[0])


'''La coma es indiespensable por ejemplo en una lista o diccionario
ya que esto ayuda al contro de versiones de git al final'''
FICHEROS = [
    'ficheros1.txt',
    'ficheros.txt',
]
