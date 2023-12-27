print('-- Numero naturales usando For con una Clase')


'''ANOTACION: Esta clase(objeto) es una un objeto iterador
dado que trabaja con los metodos __iter__ y __next__
'''


# Se crea la clase
class NumerosNaturales:
    # Creamos el constructor y su parametro
    def __init__(self, n):
        # Se usa el parametro
        self.n = n
        self.actual = 0

    # Este metodo devuelve el propio objeto iterador
    def __iter__(self):
        return self

    # Este metodo debe devolver el siguiente elemento de la secuencia
    def __next__(self):
        # Inicio de la secuencia y fin de ella
        if self.actual < self.n:
            # En la variable resultado se almacena el actual
            resultado = self.actual
            # Se incremente la en 1 el actual
            self.actual += 1
            return resultado
        else:
            # Cuando llegue a self.n detendrá la ultima iteracion con excepcion
            raise StopIteration


# Uso del iterador
iterador = NumerosNaturales(5)
print(next(iterador))
print(next(iterador))


'''NOTA: Se podria recorrer con un ciclo for pero iteraria
demasido rapido las secuencia'''

print('-- Numero naturales usando While')


def numeros_naturales(n):
    i = 0
    while i < n:
        yield i
        i += 1


generador = numeros_naturales(10)
print(next(generador))  # El cilo For imprimira desde el 1. Aca se muestra 0
for i in generador:
    print(f'Numero natural: {i}')
