frase = input('Decime una frase y te cualculo cunato te tardarias si tu tuvieras que decirlas: ')
cantidad_separadas = frase.split(" ")
cantidad_de_palabras = len(cantidad_separadas)

print(f'Dijistes {cantidad_separadas} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 * 1.8 /10} sefundos')