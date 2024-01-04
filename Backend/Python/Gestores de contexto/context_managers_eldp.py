'''Gestores de contexto: Son bjetos que permites la asinacion
y liberación de recuersos dentro de un bloque 'with'.
Estos obejetos deben implementar métodos espaciales '__enter__'
y '__exist__'''


# creamoa la clase de los gestores de contexto
print('--Creamos un gestor de contexto--')


class GestorContextoEjemplo:
    def __enter__(self):
        print('Entrada a al bloque with')
        # Puedes devolver cualquier objeto que quieras utilizar
        # dentro de bloque with
        return self

    # exc_type: Este parámetro contiene el tipo de
    # la excepción que se ha producido.
    # exc_value: Contiene la instancia de la
    # excepción que se ha producido nuevamente,
    # si no se produce us valor es none
    # traceback: Contiene el objeto asociado con el excepcion
    def __exit__(self, exc_type, exc_value, traceback):
        print('Saliendo del bloque with')
        # Se pueden realizar acciones de limpieza aca si es necesario


# Uso del gestor de contexto
try:
    with GestorContextoEjemplo() as contexto:
        print('Dentro del bloque with')
except TypeError as e:
    print(f'Se produjo un TypeError: {e}')


print('--Gestores de contexto--')


# Creamoa la clase para abrir y cerrar el gestor
class GestorContextNombre:
    def __enter__(self):
        # Se puede devolver cualquier objeto que
        # queiras utilizar dentro de bloque with
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Saliendo del bloque with')

        if exc_type is not None:
            # Se produjo una excepción, puede acceder a los parámetros
            print(f'Se produjo una excepción de tipo {exc_type}: {exc_value}')

        # Aca se pueden realizar acciones de limpieza si es necesario


# Uso del gestor de contexto
try:
    with GestorContextNombre() as contexto:
        print('Dentro del bloque with')
    # Simulamos una excepción
    raise ValueError('Excepción de ejemplo')
except ValueError as e:
    print(f'Excepción caturada: {e}')

print('--Haciendo uso de los context managers--')


# Haciendo uso de los context managers
with open('Fichero.txt', 'w') as fichero:
    # La variable fichero no sera accedida desde afuera,
    # una mentes desde el bloque
    # with
    fichero.write('Hola')
    # La funcion close() se ejecueta autmomaticamente cuando salfa del bloque
    # with
print('--SIN USAR context managers--')
fichero = open('Fichero.txt', 'w')
try:
    fichero.write('Hola!')
finally:
    fichero.close()


print('--Implementacion con clases--')


class Gestor:

    # No se crea el init ya que se invoca automaticamente el
    # metodo __init__ al entrar al bloque with
    def __enter__(self):
        print('Entrar en __enter__')

    # Este metodo es llamado al salir del with.
    # Es equivalente por lo tanto al bloque except
    def __exit__(self, exc_type, exc_value, traceback):
        print('Entre en el __exit__')


with Gestor() as f:
    print('Hola gestor')

print('--Implementacion con clases con excepcíon--')


class MiGestor:

    # No se crea el init ya que se invoca automaticamente el
    # metodo __init__ al entrar al bloque with
    def __enter__(self):
        print('Entrar en __enter__')
    # Este metodo es llamado al salir del with.
    # Es equivalente por lo tanto al bloque except

    '''NOTA:
    exc_type: Tipo de excepción que fue lanzada. En el ejemplo
    seria <class 'Exception'>
    exc_value: Valor de la excepción en el caso de que fuera
    proporcionado
    traceback: Objeto traceback con mas información aceca de la
    excepción'''
    def __exit__(self, exc_type, exc_value, traceback):
        print('Entre en el __exit__')


'''with MiGestor() as f:
    raise Exception'''

print('--Fiechero con un gestor de contexto--')


class MiClaseFichero:

    # Creamos el contructor que resibirá el
    # gestor y el fichero que queremos crear
    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def __enter__(self):
        self.fichero = open(self.nombre_fichero, 'w')
        return self.fichero

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fichero:
            self.fichero.close()


# Le pasamos el fichero
with MiClaseFichero('Fichero.txt') as ficheroa:
    ficheroa.write('hola!')
