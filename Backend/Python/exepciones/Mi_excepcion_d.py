''' Creamos excepcion'''
#esto hera de excepcion
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f'Impresionante, cometiste el siguiente error: {err}')

#Raise lanza la excepsion  
try: 
    raise MiExcepcion("\nCometiste el siguiente error") 
except:
    print('Cometiste el error')  
#raise ZeroDivisionError('No se puede dividir por cero')
 