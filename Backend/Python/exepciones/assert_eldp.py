''' Assert: Permite realizar ocmprobaciones. Si la expression 
contenida dentro del misom es fase, se lanzará un excepción'''
#creamos un valor paraenvier el error assert. AssertionError
assert(1 == 1)#Cuando la condicion es true no envia nada
assert True, "El assert falló"#Esto me enviara le segundo mensaje

print('--Asser en comparacion de texto--')
cadena_string = 'Luis Fernando Troncoso'
assert cadena_string == 'Luis Fernando Troncoso'#si el texto NO es igual envia la excepsion

#assert en testing 
print('--Assert en testing--')
#Creamos la funcion
def calcular_media(lista):
    return sum(lista)/len(lista)
#hacemos la ocmprobaciones ocn el assert
assert(calcular_media([5, 10, 7.5]) == 7.5)#si colocamos un valores que no es mandará la excepsion
assert(calcular_media([4, 8]) == 6)#No madnara la excepsion ya que el valro es correcto

print('--Assert en funciones--')
#Funcion suma de variables enteras
def suma(a, b):
    assert(type(a) == int)
    assert(type(b) == int)
    return a + b
#Pasamos valores que NO son de tipo int
#suma(3.0, 5.0) #Esto genera la excepsion

#Pasamos valores que SON de tipo int
suma(3, 5)# como son valores aceptados, no mostrará nada

print('--Asser con clases--')
#Creamoa las clases
class Miclase():
    pass

class MiOtraClase():
    pass

mi_objeto = Miclase()
mi_otro_objeto = MiOtraClase()
#Assert para medir objetos
assert(isinstance(mi_objeto, Miclase))#OK. No muestra nada
assert(isinstance(mi_otro_objeto, MiOtraClase))#OK. No mostrara nada

#Errores, mi_objeto no pertenece a MiOtraClase
#assert(isinstance(mi_objeto, MiOtraClase))

#Error, mi_otro_objeto no pertenece a Miclase
assert(isinstance(mi_otro_objeto, Miclase))
    