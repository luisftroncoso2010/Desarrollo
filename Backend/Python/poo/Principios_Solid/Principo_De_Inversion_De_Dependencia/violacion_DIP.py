''' Principio De Inversion de Dependencias '''
print('--Colocamos un principio donde se viole--')
#Clase de alto nivel que depende de una clase de bajo nivel directamente
class Usuario:
    #Se crea el constructor 
    def __init__(self):
        #Creamos una variable de instancia, para que entre
        self.servicio_correo.ServicioCorreoElectronico()
    
    def enviar_mensaje(self, mensaje):
        self.servicio_correo.enviar_correo(mensaje)
    
#Clase de bajo nivel concreta 
class ServicioCorreoElectronico:
    def enviar_correo(self, mensaje):
        print(f'Envian correo electronico: {mensaje}')

if __name__ == "__main__":
    usuario = Usuario()
    usuario.enviar_mensaje('Hola, ¿Cómo estas?')
    