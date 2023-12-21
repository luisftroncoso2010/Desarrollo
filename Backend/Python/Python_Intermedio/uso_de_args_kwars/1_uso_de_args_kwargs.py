'''Use de *args y Kwars'''


print('- Uso del *args')


# Ejemplo uso de *args
def test_var_args(f_args, *argv):
    # Aca se imprime el primer argumento
    print(f'Primer argumento normal: {f_args}')
    # El for recorre la segunda parte, se alamacena en una tupla
    for args in argv:
        print(f'Argumentos de *argv: {args}')


test_var_args('python', 'foo', 'bar')


print('- Uso de **Kwargs')


# ACa creamos la funcions y le pasamos un diccionario de listas
def saludame(**kwargs):
    # Aca iteramos sobre el diccionario de listas
    for key, value in kwargs.items():
        # Preguntamos sobre la llave "Apellidos"
        if (key == 'Apellidos'):
            # Si la llave existe, la iteramos.
            # Recuerda: ↓↓↓↓
            # (Es un diccionario DE LISTAS, solo sus valores fuera de la lista)
            for apellido in value:
                print(apellido)


kwargs = {'nombres': ['Luis', 'Fernando', 'Andres'],
          'Apellidos': ['Troncoso', 'Montes', 'Cabarcas'],
          'Ciudad_Nacimiento': ['Planeta Rica', 'Cienega De Oro', 'Sahagun']}

saludame(**kwargs)


print('- Usando *args y **Kwars')


# LA misma funcion desempaquetara lo que se le pase como tupla
def test_args_kwargs(arg1, *arg2, arg3):
    print(f'arg1: {arg1}')
    print(f'arg2: {arg2}')
    print(f'arg3: {arg3}')


# Primero con *args
args = ("dos", 3, 5)
test_args_kwargs(*args)
_kwargs = {"arg3": 3, "arg2": "dos", "arg1": 5}
test_args_kwargs(**kwargs)

''' Usando los tres tipso de funcion en el siguiente orden:
* Parametro normal
* Por tupla
* Por diccionario'''
# Ahora con **kwargs:
test_args_kwargs(45, args, arg3=_kwargs)


print('- ¿Cuando usar *args y **kwargs?')


def get_info(self, *args):
    return 'Test data'