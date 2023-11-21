'''
Cohesion: Hace referecia a la alta relacion de un medulo entre si
Acopamiento: Hace referencia en la medida de las clases depende unas de otras
'''
print('Cohesion debil')
#Cohesión debil 
def suma():
    num1 = float(input('Dame primer: '))
    num2 = float(input('Dame segundo número: '))
    suma = num1 + num2
    print(suma)
'''
NOTA: Es una BAJA, ya que Si una persona quiere sumar dos numeros
que ya tiene, no podria ya que se los pdie por consola
'''
suma()

print('Cohesion alta')
#Se considera cohesion alta en el sentido de que se 
def sumaNumeros(numeros):
    total = 0
    for i in numeros:
        #Se coloca i en ves 1 uno ya que se quieren sumar es el itereable pasado y no contar los elementos
        total +=i
    return total
suma = sumaNumeros([2, 5])#Aca se le pasa el iterable
print(suma)