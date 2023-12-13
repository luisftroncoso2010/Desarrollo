''' Juego del ahorcado '''
import random #Modulos Build int
import string #Sirve para trabajar con dadenas de caracteres
from lista_palabras import palabras
from ahorcado_diagrama import vidas_diccionario_visual

#Metodo para encontrar  una palabra_seleccionada en una lista sin espacion ni guiones
def obtener_palabra_valida(palabras):
    #Seleccionar una palabra_seleccionada al azar de la lista de palabras validas
    palabra_seleccionada = random.choice(palabras)    
    #Buscamos un caracter que no tienes espacion o guion
    while '-' in palabra_seleccionada or ' ' in palabra_seleccionada:
        palabra_seleccionada = random.choice(palabras)#Alamacenamos la palabra_seleccionada aca sin - ni espacios ' '
    return palabra_seleccionada.upper()#Retornamos la palabra_seleccionada encontrada en mayusculas

    
def ahorcado ():    
    print('  ¡Bienvenido(a) al juego del Ahorcado!      ') 
    palabra_seleccionada = obtener_palabra_valida(palabras)#Aca almancenamos la palabra_seleccionada que traimos de la lista   
    #Creamos un conjunto para guardar elementos NO repetidos. (Ya que una de la principales caracteristicas de los conjuntos es que no alamacenan elementos repetidos)
    letras_por_advivinar = set(palabra_seleccionada)#Se le pasa la palabra desordenada y la desordena. 
    letras_adivinadas = set()#Queda vacio este conjunto
    abecedario = set(string.ascii_uppercase)#Todas las letras en mayudculas. No contiene la ñ
    vidas = 8 #Variable vidas
    
    
    #Mientras falten letras por adivinar y tengas vidas 
    while len(letras_por_advivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vidas y te quedan estas letras: {' '.join(letras_adivinadas)}")
                
        #Mostrando el estado actual de las palabras. Por ejemplo en algun moemnto del jugo sera asi HO-A
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra_seleccionada]
                
        #Mostras estado del ahoracado
        print(vidas_diccionario_visual[vidas])
        #msotrar las letras separadas por espacio
        print(f"palabra_seleccionada: {' '.join(palabra_lista)}")
        
        #Pedir letra, la convertira a mayuscula dado que no lo esté
        letra_usuario = input("Escoge una letras: ").upper()
        #Si la letra escogida por el usuario esta en el abecedario y no esta en el conjunto de letras que ya sean ingresado, se añade la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            #Si la letras esta en la palabra_seleccionada
            if letra_usuario in letras_por_advivinar:
                letras_por_advivinar.remove(letra_usuario)#Se remueve para para no hace repeticiones y no quitar vidad                
                print('')#Se envia un mensaje en blaco
            else:
                vidas -=1#Dado que la letra no esta seleccionada se le quita una vida. Por que coloco una letra que no esta en la palabra_seleccionada
                print(f'\nTu letra, {letra_usuario} no esta ne la palabra seleccionada. ')
         #Si la letra escogioda por el usuario ya fue ingresada       
        elif letra_usuario in letras_adivinadas:
            print(f'Ya escogiste esa letra, por favor escoge otra')
        else:
            print(f'\n Esta letra no es permitido')
    
    #El juego llega esta linea cuando se adivinan todas las letras de la palabra_seleccionada o cuando se agotan las vidas del jugador
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])#Aca muestra la figura del ahoracado
        print(f'¡Ahoracado!. Perdiste. Lo lamento mucho. La palabra_seleccionada era: {palabra_seleccionada}')    
    else:
        print(f'Excelente adivinaste la palabra_seleccionada: {palabra_seleccionada}')




ahorcado()
