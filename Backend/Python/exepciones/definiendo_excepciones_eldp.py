''' Definiendo excepciones: A pesar de qeu python define un conjunto
de excepciones por defecto, podrian no ser suficientes para nuestro programa.
En esos caso podriamos definirlas'''
print('--Creando excepciones--')
#Creamos una exepcion personalizada
class MiExcepcionPersonalizada(Exception):
    #PAra lanzarar podriamos lanzar raise
    pass

#Creamo nuestra propia excepción heredando de la clase Exception
class MiExcepcionPersonalizada(Exception):
    #Creamos el constructor
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
#Lanzamos la excepción con raise
try:
    raise MiExcepcionPersonalizada('ValoPar1', "ValorPar2")#Pasamos loa parametros a la excepsion
except MiExcepcionPersonalizada as ex:
    p1, p2 = ex.args#Se coloca el .args para indicar que lso parametros se pasaron por tuplas
    print(type(ex))
    print("parametro1 = ", p1)
    print("parametro2 = ", p2)
    
print('--Pasar una excepcion enforma de diccionario--')
#Se define la excepción 
class Miexcepcion(Exception):
    pass

#Se lanza la excepción
try:
    raise Miexcepcion({'Mensaje': "Mi mensaje", "Informacion" : "Mi informacion"})
#Se captura
except Miexcepcion as e: #Se le da un as al diccionario
    detalles = e.args[0]
    print(detalles)
    print(detalles['Mensaje'])
    print(detalles['Informacion'])
    
print('--Pasar informacion de maenra mas larga--')
class mi_excepcion(Exception):
    def __init__(self, mensaje, informacion):
        self.mensaje = mensaje
        self.informacion = informacion
        
#Creamos el bloque
try:
    raise mi_excepcion('Mi mensaje', 'Mi información')
except mi_excepcion as e:
    print(e.mensaje)
    print(e.informacion)
    
print("--Ejemplo de como hacer excepsiones personalizadas--")
class SaldoInsificiente(Exception):
    #creamos la clase Excepcion
    """Excepción personalizada para manejar saldos insuficientes en una cuenta"""
    def __init__(self, saldo_actual, cantidad_a_retirar):
        #Creamos el super para el mensaje de error Excepcion
        super().__init__(f'Saldo insuficiente. Saldo actual: {saldo_actual}, Cantidad a retirar: {cantidad_a_retirar}')
        self.saldo_actual = saldo_actual
        self.cantidad_a_retirar = cantidad_a_retirar

#Creamos un metodo fuera. PAra pasar el saldo y la cantidad
def realizar_retiro(saldo, cantidad):
    #
    if saldo < cantidad:
        raise SaldoInsificiente(saldo, cantidad)
    else:
        print(f'Retiro exitoso. Nuevo saldo: {saldo - cantidad}')

#Creamoa la excepcion para realizar los retiros
try:
    realizar_retiro(100, 200)
except SaldoInsificiente as e:
    print(f'Error: {e}')

print('--Ejemplo de Exception--')
#Creamos la clase que hera de Exception
class MiExceptionPersonalizada(Exception):
    #Definimos el contructor de la clase
    def __init__(self, mensaje):
        #Aca llamamos al contructor de la clase base Exception
        #aca se garantiza que el mensaje se almacene correctamente 
        # de y cualquier lógica de inicialización adicional en la clase 
        # base se ejecute        
        super().__init__(mensaje)

#Hacemos uso de la excepcion personalizadá
try:
    raise MiExceptionPersonalizada('Este es un mensaje personalizado')
except MiExceptionPersonalizada as ex:
    print(f'Se capturó la excepcion: {ex}')
'''Nota: '''        