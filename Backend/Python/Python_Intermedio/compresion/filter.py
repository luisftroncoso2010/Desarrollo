'''Funcion filter en pcompresion de listas'''


# Funcion para validar si un numero es multiplo de 5
def multiple(numero):
    if numero % 5 == 0:
        return True


# Lista para validar
numeros = [2, 5, 10, 23, 50, 33]
# Filtramos la lista
print(f'Multiplos de 5 (Funcion Nomral): {list(filter(multiple, numeros))}')
# Podemos usar la funcion lambda
multiplosDeCindo = list(filter(lambda numero: numero % 5 == 0, numeros))

print(f'Multiplos de 5 (lambda):{multiplosDeCindo}')


print('-- Filtrando objetos')


# Creamos la clase
class Persona:
    # Cremoas el contructor de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Metodo especial para imprimir
    def __str__(self) -> str:
        return f'{self.nombre} de {self.edad} años'


# Creamos la lista para enviar a imprimir atraves del metodo especial
personas = [
    Persona('Juan', 35),
    Persona('Marta', 16),
    Persona('Manuel', 78),
    Persona('Eduardo', 12)
]


# Validamos los que son menores de edad
menores = filter(lambda Persona: Persona.edad < 18, personas)
# Recorremoso la lista
for menores in menores:
    print(menores)
