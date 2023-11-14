'''
Si se queire colocar un subpaquete, ese sub
paquete debe tener el archivo __init__.py
'''
import paquete.moduloSaludar
print(paquete.moduloSaludar.saludar('Luis'))
print(paquete.__path__)