'''
Detector de pedos, que se registrados.

'''
import pandas as pd #Trabajo de csv 
import matplotlib.pyplot as plt #Visualizacion de datos
import seaborn as sns #Graficos estadadisticos
df = pd.read_csv("Backend//Python//problemasGraficos//pedos.csv")
print(df)

#Creamos el grafico. lineplot(Grafico de lineas)
sns.lineplot(x='fecha', y='pedos', data=df)

#Marcamos un punto en especifico, el mas alto (Se prodria hacer de forma dinamica, marcando el punto mas alto)
plt.plot('01-09', 17, 'o')

#Mostramos el grafico
plt.show()