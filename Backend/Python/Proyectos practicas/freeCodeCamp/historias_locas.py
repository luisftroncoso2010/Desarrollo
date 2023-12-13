''' Concatenar caracteres.
Supongamos que queremos crear una cadena que diga:
Aprende a programar con ________________________
'''
organizacion = 'FreecodeCamp'
#concatenamos ocn el signo mas
print('Apredne a programa con ' + organizacion)
#concatenamos con el metodo format sin llaves. fstrings
print(f'Aprende a programar con {organizacion}')
#Usando las llaves de tipo format con llaves
print('Apredne a programar con {}'.format(organizacion))

#Mad Libs (Historias Locas)
print('--Aprende a programa con historias locas--')
adg = input('Adjetivo: ')
verboUno = input('Verbo: ')
verboDos = input('Verbo: ')
sustantivo_prural = input('Sustantivo (Prural): ')
madlib = f'Programar es tan {adg}! Siempre me emociona por que me encanta {verboUno} problemas. ¡Aprende a {verboDos} con FreeCodeCamp y alcanza tus {sustantivo_prural}!'
print(madlib)