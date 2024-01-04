from functools import wraps


print('-- Primer decorador')


# Creamos la funcion decoradora
def nuevo_decorador(a_func):
    # Colocamos la funcion envolvente
    def envuelveLaFuncion():
        print('Antes de llamar a la funcion()')

        a_func()

        print('Haciendo algo luego de llamar a la funcion()')
    return envuelveLaFuncion


# Funcion que necesita ser decorada
def funcion_a_decorar():
    print('Soy la funcion que necesita ser decorada')


funcion_decorada = nuevo_decorador(funcion_a_decorar)
funcion_decorada()


print(' ----------------- ')


# Creaomos un decorador usando arroba(El docorador ya esta creado)
# Con el aroba declaramos la ufncion como decoradora
@nuevo_decorador
def decorame():
    print('Me acaban de decorar!')


# Esto sobre escribe el nombre y el docsString de la misma
# print(decorame.__name__)


print('-- Uso del functols')


def nuevo_decorado(a_fun):
    @wraps(a_fun)  # Se le debe pasar a wraps por parametro la funcion
    def envuelveLafuncion():
        print('Haciendo algo antes de llama a a_func()')
        a_fun()
        print('Haciendo algo después de llamar a a_func()')
    return envuelveLafuncion


@nuevo_decorado  # aca se coloca la funcion decoradora
def funcion_a_decorar():
    print('Funcion que necesita ser decorada')


funcion_a_decorar()
# Esto imprime el nombre de la funcion decorada
print(funcion_a_decorar.__name__)


print('-- ejemplos de funtools con wraps')


# Creamos la funcion. Resive de parametro f
def nombre_decorador(f):
    # A @wraps le pasamos el parametro f, que resibira
    # la funcion para decorarla
    @wraps(f)
    def decorada(*args, **kwargs):
        if not can_run:
            return 'La funcion no se ejecutará'
        return f(*args, **kwargs)
    return decorada


@nombre_decorador
def func():
    return ('La funcion se esta ejecuntando')


can_run = True
print(func())


can_run = False
print(func())


print('-- Autorizacion como flask o Django')

'''
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated'''


print('-- Ejemplo Iniciar seccion')


# Creamos la funcion que simula el inicio de seccion
def logit(func):
    # Creamos la funcion que decoradora.
    @wraps(func)
    def with_logging(*args, **kwargs):
        # Añade la funcion que va a llamar el doc string
        print(func.__name__ + ' was called')
        return func(*args, **kwargs)
    return with_logging


@logit
def addition_func(x):
    '''Funcion suma'''
    return x + x


result = addition_func(4)


print('-- Aninando un decorador dentro de una funcion')


# Creamos la funcion. Lelaginamos un valor por defecto
def logitt(logfile='out.log'):
    # Creamoas la funcion decoradora
    def logging_decorador(func):
        # Colocamos en wrapps que decrara
        @wraps(func)
        def wrapped_function(*args, **kwards):
            log_string = func.__name__ + ' Fue llamada'
            print(log_string)
            # Abrimos el fichero y abrimos el contenido
            with open(logfile, 'a') as open_file:
                # Escribimos en el fichero el contenido
                open_file.write(log_string + '\n')
            return func(*args, **kwards)
        return wrapped_function
    return logging_decorador


@logitt(logfile='func2.log')
def my_fun_uno():
    pass


my_fun_uno()


print('-- Clase decoradas')


class loogit(object):

    _logfile = 'out.log'

    # Constructor de la clase. Le acreamos un atriburo para pasarle la funcion
    def __init__(self, func):
        self.func = func

    # Con este metodo podemos crear instancias de la clase
    # y usarlas como si fuesen una funcion
    def __call__(self, *args):
        log_string = self.func.__name__ + ' fue llamada'
        print(log_string)

        # Abre el fichero de log y escribe
        with open(self._logfile, 'a') as open_file:
            # Escribimos el contenido
            open_file.write(log_string + '\n')
        # Enviamos una notificacion
        self.notify()

        # Devuelve la funcion base
        return self.func(*args)

    def notify(self):
        # Esta clase se escribe el log mas nada
        print(f'Estas en la funcion, desde la clase: {loogit.__name__}')


loogit._logfile = 'out2.log'  # Si queremos usar otro nombre


@loogit
def myfun1():
    pass


myfun1()


print('-- Subclase de loogit (Herencia)')


class email_logit(loogit):
    '''
    Implementacion de loggit con envio de email
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwards):
        self.email = email
        super(email_logit, self).__init__(func, *args, **kwards)

    def notify(self):
        print(f'Esta en la clase: {email_logit.__name__}')
        print('Enviaste el correo')


@loogit
def myfun11():
    pass


myfun11()


@email_logit
def myfun2():
    pass


myfun2()
