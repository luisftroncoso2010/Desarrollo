''' sys.path '''
import sys
import modulos_eldp
print(sys.path)

print('--Names space--')
print(dir())
print(f'Nombre del modulo: {__file__}')#Esto muestra la ruta
print(f'Nombre del modulo: {modulos_eldp.__name__}')#Esto muestra el nombre del modulo
print('--Modulo que no existe--')
import moduloOperaciones as mo
try:
    import modulo_inexistente #Este modulo no existente y se capura la excepcion aca
except ModuleNotFoundError as e:
    print(f'Hubo un error de modulo: {e}')

'''NOTA: Es importante que cuando se cree el modulo NO
se ejecutens la funciones que ys que solo cuando se importe
te traerá las funciones resultas a no ser que en dicho modulo
se coloque el emtodo de inicio __main__'''
