
''' Test Manuales:
* Son test ejecutados manualmente por una persona, probando
diferente acombinaciones de viendo que le comportoamiento del
código es el esperado.
Test aAutomáticos:
* Código que testea que otro código se comporta correctamente.
'''


def calcular_media(*args):
    return sum(*args) / len(*args)


print(calcular_media([3, 5, 7]))
print(calcular_media([30, 0]))
# Esto envia un error ya que no es el resultado esperado
assert (calcular_media([3, 7, 5]) == 5.0)
