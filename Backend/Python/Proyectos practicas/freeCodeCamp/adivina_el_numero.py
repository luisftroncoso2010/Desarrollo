''' Adivina el numero'''
import random as rnd#Importamos el modulo random
def adivina_el_numero(x):
    print('===================')
    print('¡Bienvenid@ al juego!')
    print('===================')
    print('Tu meta es adivinar el numero generado por la ocmputadora')
    #Esto me dice que generaremos numero enteros, ente 1 y x(Es el pasado por parametro a la funcion)
    numero_aleatorio = rnd.randint(1, x)
    
    prediccion = 0#Se coloca inicial en 0, para que no inicie de esa manera
    while prediccion != numero_aleatorio:
        #El usuario ingresa un numero, se convierte a int ya que siempre el input es de tipo string y se convierte a int
        prediccion = int(input(f'Adivina un numero entre 1 y {x}: '))
        if prediccion < numero_aleatorio:
            print('Inteta otra ves estre numero es pequeño')
        elif prediccion > numero_aleatorio:
            print('Intenta otra ves este numero es muy grande')
    
    print(f'¡Felicitaicones adivinaste el numero {numero_aleatorio} correctamente!')

#Le pasamos el numero como parametro para que lo escoja 
adivina_el_numero(20)
            




        
            
    