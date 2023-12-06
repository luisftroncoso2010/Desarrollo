''' modulo Math, apmplia la lista de funciones matematicas '''
import math
#Sacamos la raiz cuadrada
raiz_caudrada = math.sqrt(12)
print(f'La raiz cuadrada es: {raiz_caudrada}')
#Elevamos el resultado de la raiz cuadrada a la 2
print(pow(raiz_caudrada, 2))

#Redondearemos numeros
#Redonde amos le numero siempre lade mas arriba
numeroUno = math.ceil(1.4)
print(f'El numero mas cercano hacia arriba es: {numeroUno}')
#Redondeamos el numero al de mas abajo
numeroDos = math.floor(1.2)
print(f'El numero mas cercano hacia abajo es: {numeroDos}')

#Imprimimos PI
pi = math.pi
print(f'Pi es: {pi}')
#Imprimimos el euler
euler = math.e
print(f'El euler es: {euler}')

#Logaritmo natural 
log_natural = math.log(10)
print(f'Logaritmo natural: {log_natural}')