""" Decoradores"""

def mi_decorador(funcion):
    def nuevaFuncion(*args):
        # Se llamada al nombre del la funcion decorada
        print ("Llamada a la funcion", funcion.__name__)
        retorno = funcion(*args)
        return retorno
    return nuevaFuncion


@mi_decorador
def funcionDecoradora():
    print('Funcion para decorar')
    
    
""" Nota: Los decoradores se ejecutan de abajo hacia arriba """
funcionDecoradora()


    
    
    
