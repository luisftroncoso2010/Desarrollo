'''
Cramos un nuevo modulo con una funcion matematica
'''
frase = 'Hola luis, tienes la funcion calcular_factorial'
def calcular_factorial(numero):
    factorial =1
    for n in range(1, (numero + 1)):
        factorial +=n
    return factorial