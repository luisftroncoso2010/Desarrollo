import random as rnd

#Cramos la funcion
def jugar():
    #Pedimos al usuario que desea   
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel y 'ti' para tijera:\n ").lower()
    
    #random.choice devulve un valor de una lista
    pc = rnd.choice(['pi', 'pa', 'ti'])#Esto retorna un valor al aza de una listas
    print(f'Seleccion del usuario: {usuario}\tSeleccion del Computador: {pc}')
    
    #Creamoa la condiciones. S ised iguala es igual al pc
    if usuario == pc:        
        return '¡Empate!'

    #Se llama la funcion para comparar los datos del usuario y pc
    if gano_el_jugador(usuario, pc):
        return '¡Gansaste!'    
    return '¡Perdiste!.\tGano La maquina!'

def gano_el_jugador(jugador, oponente):
    #Retornar el valor de True, si gana o gano´el jugador
    #Piedra gana a Tijera (pi > ti)
    #Tijera gana a Papel (ti > pa)
    #Papel gana a Pidra (pa > pi) 
    
    if ((jugador == 'pi' and oponente == 'ti')
        or (jugador == 'ti' and oponente == 'pa')
        or (jugador == 'pa' and oponente == 'pi')):
        return True
    else: 
        return False   

print(jugar())
    
