from abc import ABC, abstractmethod
''' Principio de inversion de dependencias, de manera correcta  '''
#Creamos la clase de abstraccion de notificacion
class ServicioNotificacion:
    @abstractmethod
    def enviar_notificacion(self, mensaje):
        pass

#Implementacion correcta del servicio de notificíon por correo electronico
class ServicioCorreoElectronico(ServicioNotificacion):
    def enviar_notificacion(self, mensaje):
        print(f'Enviado desde correo electronico: {mensaje}')

#Implementacion concreta del servicio de notificacion por texto
class ServicioMensajeTexto(ServicioNotificacion):
    def enviar_notificacion(self, mensaje):
        print(f'Enviando mensaje de texto: {mensaje}')
        
#Clase usuario que depende de la abstraccion (ServicioNotificacion)
class Usuario:
    def __init__(self, servicio_notificacion):
        self.servicio_notificacion = servicio_notificacion
    
    def enviar_mensaje(self, mensaje):
        self.servicio_notificacion.enviar_notificacion(mensaje)
        
        
#Uso de las clases desde el main
if __name__ == '__main__':
    #Crear instancias de los servicios de notificación
    servicio_correo = ServicioCorreoElectronico()
    servicio_texto = ServicioMensajeTexto()
    
    #Crea instancia de usuario con inyección de dependencia
    usuario_correo =  Usuario(servicio_correo)
    usuario_texto = Usuario(servicio_texto)  
    
    #enviar mensaje a diferentes servicios
    usuario_correo.enviar_mensaje('Hola, ¿Como estás?')
    usuario_texto.enviar_mensaje('!Recordatorio importante!')