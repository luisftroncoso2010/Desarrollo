'''
Decoradores: Reciben una funcion para decorar.
Es una funcion que decora a otra, es decir
la funcion toma otra funcion (o método) como 
argumento y devuelve una nueva función con algún
 comportamiento adicional
'''
print('---Decorador---')
#Creamos la funcion decoradora
def Decorador(funcion):
    def funcion_modificada():
        print('Antes de llamar la funcion')
        funcion()
        print('Despues de llamar a la funcion')
    #Si colocamos los parentesis funcion_modificada() aca al retornarlo no habra necesidad dellamarlo debajo   
    return funcion_modificada()

@Decorador
def saludo():
    return print('Esta es mi funcion por fuera')

print('---Decorador para aritmeticos. Otra manera de mostrarla---')
def decoradorAritmetico(funcion):
    def funcionDecoradora():
        print('----Calculos----')
        funcion()
    return funcionDecoradora

#Funcion decorada
def suma(a = 10, b = 20):
    print(a + b)

#Esta es otra manera para mostar la funcion decorada
sumaObjeto = decoradorAritmetico(suma)
sumaObjeto()

print('--Codigo optimo para decorar--')
#Creamos la funcion decoradora. Esta la manera optima y elegante
def decoradorAmor(funcion):
    def funcionDecoradora():
        print('↓↓↓↓')
        funcion()#aca se mostrara la funcion decoradora
        print('↑↑↑↑')
    return funcionDecoradora

@decoradorAmor
def mi_funcion():
    #Aca pasaremos la funcion a decorar
    print('Hola decorame')
#Mostramos la funcion decorada
mi_funcion()