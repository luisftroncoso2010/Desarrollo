import inspect
import modulo_inspect


''' NOTA: El metodo especial __doc__ muestra los metodos
de una cadena en la clase '''
print('-- Metodo especial __doc__\n\tB.__doc__: ')
print(' ')
print(modulo_inspect.B.__doc__)
print(' ')
print('get_name(B):')
print(inspect.getdoc(modulo_inspect.B.get_name))
print(' ')
print(inspect.getdoc(modulo_inspect.B.do_something))
print(' ')
print(inspect.getcomments(modulo_inspect.B.get_name))
print(' ')
# Esto retorna el primer comentario del modulo
print(inspect.getcomments(modulo_inspect))
print(' ')
print('-- Recuperar codigo fuente. getsource()')

# Muestra el codigo de la clase. # Si esta en
# un archivo compilado pyc, enviara una exception OSError
print(inspect.getsource(modulo_inspect.A))
print('-- Mostrar el modulo linea por linea')
# Muestra el codigo linea por linea en una lista
print(inspect.getsourcelines(modulo_inspect))
print('-- Msotrar solo una clase del modulo')
print(inspect.getsource(modulo_inspect.A))
print('-- Mostar un metodo de una clase: ')
print(inspect.getsource(modulo_inspect.A.get_name))
