#importamos el modulo
import modulos1 
#Importamos todas la funcionalidades
print(modulos1.multiplicar(2, 5))
print(modulos1.restar(2, 2))
print(modulos1.dividir(2, 2))
print(modulos1.sumar(2, 2))
#Importamos una variables
PermissionError(modulos1.canal)

from mi_paquete import funcionesMatematicas
print(funcionesMatematicas.calcular_factorial(5))
print(funcionesMatematicas.frase)#Accedemos al nameespace

#importacion de un subpquete 
from mi_paquete.sub_paquete1.funcionesAvanzadas import contar_letrar
texto = 'Gracias por apoyar mi canal'
print(contar_letrar(texto))