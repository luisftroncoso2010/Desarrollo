'''
Decoradores
'''
print('--Primer decorador--')
def myDecorador(funcion):
    def nuevaFuncion(a, b):
        print('Se va a llamar la funcion')
        c = funcion(a, b)
        print('Se ha llamado')
        return c
    return nuevaFuncion

@myDecorador
def suma(a, b):
    print('Entra la funacion suma')
    return a + b

print(suma(2, 7))

print('--Segunda funcion decoradora RESTA--')
@myDecorador
def resta(a , b):
    print('Entra en funcion resta')
    resta = a - b
    print(f'La resta es: {resta}')
    return resta
resta(5,3)

print('--Defiendo decoradores--')
def operaciones(op):
    def suma(a, b):        
        return a + b
    def resta(a , b):
        return a - b
    
    if op == 'suma':
        return suma
    elif op == 'resta':
        return resta
    
funcionSuma = operaciones('suma')
print(funcionSuma(5, 7))#Muestral a suma
funcionResta = operaciones('resta')
print(funcionResta(5, 4))

print('--Funcion decoradora sin @--')
def decorador(func):
    def envoltorio_func(a, b):
        print('Decorador antes de llamar a la funcion')
        c = func(a, b)
        print('Decorador despues de llamar a la funcion')
        return c
    return envoltorio_func

def suma(a, b):    
    resultado = a + b    
    print(f'Estas dentro la SUMA: La suma es: {resultado}')
    return resultado

'''
Entonces, haciendo uso de decorador y pasando 
como entrada suma, recibimos una nueva función 
decorada con una funcionalidad nueva, lista para 
ser usada. Sería el equivalente al uso de @.
'''
#Pasamos parametetros a la funcion 
funcionDecoradora = decorador(suma)
funcionDecoradora(5, 5)

print('--Decoradores con parametros--')
'''
def miDecoradorr(arg):
    def decorador_real(funcion):
        def nueva_funcion(a, b):
            print(arg)
            c = funcion(a, b)
            print(arg)
            return c
        return nueva_funcion
    return decorador_real

@miDecoradorr
def suma2(a, b=5):
    print('Entra en una funcion suma')
    return a + b
print(suma2(5))
'''
print('--Funcion dentro de otra funcion--')
def funcion_externa():
    print('Codifo de la funcion_externa()')
    def funcion_interna():
        print('Codigo de la funcion interna()')
    funcion_interna()
funcion_externa()

print('--Retornando funciones--')
def funcion_externaTwo():
    print('Codigo de la funcion externa dos()')
    def funcion_internaTwo():
        print('Codigo de la funcion interna dos()')
    return funcion_internaTwo #como solo hay una funcion se retorna solo una funcion, si hay mas se pueden retornar mas
mi_funcion = funcion_externaTwo()
mi_funcion()#Se puede llamar a la funcion INTERNA desde cualquier parte del codigo ya que se le asgino a una variable

print('--Desempaquetando funciones para poder mostrar--')
def funcion_Padre():
    print('Esta es la funcion padre')
    def funcionInternaUno():
        print('Esta es la funcion interna Uno')
    
    def funcionInternaDos():
        print('Esta es la funcion interna Dos')
    
    def funcionInternaTres():
        print('Esta esla funcion interna Tres')
        
    def funcionInternaCuatro():
        print('Funcion interna Cuatro')
    return funcionInternaUno, funcionInternaDos, funcionInternaTres, funcionInternaCuatro

funOne, funTwo, funTree, funFour = funcion_Padre()
funOne()
funTwo()
funTree()
funFour()

'''
El funcionamiento de los decoradores se basa en tres 
ideas que vamos a desarrollar a continuación y 
que son las siguientes:

* Dentro de una función se pueden crear más funciones
* Las funciones pueden retornar funciones
* Las funciones se pueden pasar como argumentos a otras funciones
'''
print('--Estructura de un Decorador--')
def mi_Decorador(funcion_Original):
    def funcionEnvolvente():
        print('Codigo antes de que se ejecuta la funcion original')
        funcion_Original()
        print('Codigo despues de la funcion')
    return funcionEnvolvente
#Se define la funcion que se le va a pasar al decorador.
@mi_Decorador#Aca se coloca el decorador
def funcionNecesariaDecorador():
    print('¡Quiero que me decores!')   
funcionNecesariaDecorador()#Se muestra la funcion decorada

#Aca podemos instanciar la funcion decoradora sin colocar el @
#funcionDecorada = mi_Decorador(funcionNecesariaDecorador)
#funcionDecorada()

print('--Decoradores con parametros--')

def  myFunDecoradora(funcion_original):
    def funcion_envolvente(*args, **kwars):
        print('Codigo antes de la funcion original()')
        funcion_original(*args, **kwars)
        print('Codigo despues de la funcion original')
    return funcion_envolvente

@myFunDecoradora        
def mostrar_info(nombre, edad):
    print(f'{nombre} tiene {edad} años')    
mostrar_info('Luis', 26)

print(type(mostrar_info))

