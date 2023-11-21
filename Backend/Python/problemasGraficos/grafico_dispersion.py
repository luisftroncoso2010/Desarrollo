import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Backend//Python//problemasGraficos//dispersion.csv")
print(df)

#Creando grafico (graficos de dispercion)
'''
Nos mostrara que entre mas tiempo trabajemos,
mas dinero habra
'''
sns.scatterplot(x='tiempo', y='dinero', data=df)

#Mostramos el grafico
plt.show()