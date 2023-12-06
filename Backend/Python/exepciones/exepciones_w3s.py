'''
Exepciones.
El try: Bloque le permite probar un bloque de codigo en 
busca de errores
El except: Permite manejar el error
El else: Se esecuta cuando no hay ningun error
Finally: Permite ejecutar el codigo, independiente si hay error o no.
'''
print('--Creamos el primer ejemplo--')
try:
    print(x)#x no esra definida. Aca busca el error
except: 
    #Si hay error muestra eso
    print("An exeption ocurred")
    
print('--Muchos bloques de codigo. Varias exepciones--')
try:
    print(x)#aca se coloca el error a propisito    
except NameError:
    #Con el NameError se ejecutara aprnas encuentere el primer error que encuentre
    print("Variable x is no defined")
except:
    #Este se ejecutara con el segundo error contrado
    print('Somethig else went wrong')
    
print('--Si no se generan errores--')
try:
    print('Hello')#Se busca el codigo en busca de errores
except:
    print('Something went wrong')#Se maneja el error aca
else: 
    #Solo se ejecutara si hay error o no
    print('Nothing went wrong')

print('--Este bloque se ejecutra si hay error o no--')
#Error
try: 
    print(x)
#Se mostrara el mesjae ya que hay eror
except:
    #Se mostrara si hay error 
    print("Something went wrong")
finally: 
    #se muestra si hay error o no
    print('The try except is finished')