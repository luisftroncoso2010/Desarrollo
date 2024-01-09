'''__slots__: Son una caracteristicas que permite
optimizar el uso de memoria para instacias de clases
dinamicamente restringir el uso de atributos en un
instancia puede tener'''


# Creamos la clase
class Persona:
    # Creamos la restricciones de clase
    __slots__ = ('nombre', 'edad', 'altura')

    # Creamos el contructor con los atributos
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def __str__(self):
        return f'Nombre {self.nombre}\tEdad {self.edad}\tAltura: {self.altura}'


persona_uno = Persona('Luis', 26, 1.50)
print(str(persona_uno))
