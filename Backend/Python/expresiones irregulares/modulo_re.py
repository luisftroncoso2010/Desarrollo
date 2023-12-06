'''
'''
import re

# Buscar una cadena en otra
cadena = "Hola, mi número de teléfono es 123-456-7890."
patron = r'\d{3}-\d{3}-\d{4}'  # Patrón para buscar un número de teléfono en formato XXX-XXX-XXXX

resultado = re.search(patron, cadena)
if resultado:
    print("Número de teléfono encontrado:", resultado.group())
else:
    print("Número de teléfono no encontrado.")
