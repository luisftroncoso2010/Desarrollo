''' La pc adivina el numero que le pasemos '''
import random as rnd


#Creamoa la funcion. X es el numero valido para el random, limite superior
def adivina_el_numero_pc(x):
    print('  =====================   ')
    print(' ¡Bienvenido(a) al juego!    ')
    print(' ==================  ')
    #F Strgin son tipos de cadenas de cadenas decaracteres usando llaves
    print(f'Seleciona un número entre 1 y {x} para que la computadora intente adivinarlo...')
    
    limite_inferior = 1 #Lo mas bajo
    limite_superior = x #Lo mas alto
    respuesta = ""
    
    while respuesta !="C":#mientras que la respuesta no se correcta, se seguira generando una prediccion
        #Generar una prediccion
        if limite_inferior != limite_superior: #[1, 10] Se crea la diferencia ya uqe lo qeu se quiere es que este no sea igual y genere el numero
            prediccion = rnd.randint(limite_inferior, limite_superior)
        else: 
           prediccion =  limite_inferior #Tambien Podria ser el limite superior
            
        #Obtener un respuesta del usuario
        respuesta = input(f'Mi prediccion es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ').lower()
        if respuesta == "c":
            print(f'SI!. La computadora adivina tu numero correctamente {prediccion}')
            break        
        elif respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    
    
   
   
    

adivina_el_numero_pc(10)


        
            
    