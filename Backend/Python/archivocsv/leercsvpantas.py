'''
Leer archivos con padas
'''
import pandas as pd #Modulo para trabajar con pandas
#Tipo de modulo (Liberia)
print(type(pd))
'''
Los data frame son estructuras de datos bidimencionales (filas y columnas)
'''
#Con name podemos renombrar los nombres de las columnas
df = pd.read_csv("Backend//Python//archivocsv//csv.csv")
#Leemos nuevamente el archivo para poder concatenar y lo aseginamos a un nuevo valor
df2 = pd.read_csv("Backend//Python//archivocsv//csv.csv")
print(df)#Lo imprimirá modo dataFrame, con lineas por lineas autoincrementables
print(f"↓↓↓ Esta es la columna nombre del csv: ↓↓↓")
print(df['nombre'])
print('↓↓↓ Mostramos la edades ordenandas ascendente ↓↓↓')
dfShortOrdenadoAsc = df.sort_values('edad') #De esta manera los ordena de ascendente (menor a mayor)
print(dfShortOrdenadoAsc)
print('↓↓↓ Mostramos la edades ordenandas descendente ↓↓↓')
dfShortOrdenadoDesc = df.sort_values('edad', ascending=False)
print(dfShortOrdenadoDesc)
print('↓↓↓ Concatenamos dataframes↓↓↓')
dfConcatenado = pd.concat([df, df2])# Esta funcion resibe los parametos por una lista
print(dfConcatenado)
print('↓↓↓ Accediendo a la primera fila ↓↓↓')
primeraFila = df.head(1)#Dependiendo el numero que se pasa por parametro son la filas que mostrará
print(primeraFila)
print('↓↓↓ Accediendo a las 3 ultimas filas con tail()↓↓↓')
ultimaFila = df.tail(1)#Las 2 ultimas filas
print(ultimaFila)
print('↓↓↓ Accediendo a la cantidad de columnas con shape() ↓↓↓')
filaColumnasTotales = df.shape#Mostrará el numero de columnas totales. Muestra una tupla
'''
Aca lo podemos desempaquetar ya que es un iterable (Filas, columnas)
'''
print(filaColumnasTotales)
#Accedemos a las filas totales 
print(f'Cantidad de filas: {filaColumnasTotales[0]}')
#Accedemos a las columnas
print(f'Cantidad de columnas: {filaColumnasTotales[1]}')
print('Pbteneiendo data estadistica del data frame. Informacion')
df_info= df.info()
print(df_info)
print('Obteniendo promedio de df')
df_describe = df.describe()
print(df_describe)
print('Accediendo a un elemento especifico del data frame. loc')
elemento_especifico = df.loc[2, 'edad']#Se coloca la fila y la columna del elemento especifico
print(elemento_especifico)
print('Elemento especifico iloc (Por indices)')
elemento_especificoIloc = df.iloc[2, 2]#Se cuadra por indice
print(elemento_especificoIloc)
print('Accediendo a todoas las filas de una columna')
todosElementosFilas = df.iloc[:,2]#Por la edad. Es el indice 2. Todas las dilas de la edad
print(todosElementosFilas)
print('Accdeciendo a la fila 3 con loc')
filaTres = df.loc[2, :]#acdedemos a la fila 2 con todos los datos, es decir todas sus columnas
print(filaTres)
print('Accdeciendo a la fila 3 con iloc')
filatres = df.iloc[2, :]#acdedemos a la fila 2 con todos los datos, es decir todas sus columnas
print(filatres)
print('accediento a filas con edad mayor a 30')
mayor30 = df.loc[df['edad']>30, :]
print(mayor30)
print('accediento a filas con edad menor a 30')
menor30 = df.loc[df['edad']<30, :]
#el primer dato que se pide son las filas o la condicion que se le quiera pedir
print(menor30)