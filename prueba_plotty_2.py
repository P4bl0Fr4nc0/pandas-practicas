import pandas as pd 
import matplotlib.pyplot as plt

#Prueba grafic ade lines con ventas por mes y año 

df = pd.read_csv('dataset_ventas_pandas.csv')

df["fecha"] = pd.to_datetime(df["fecha"], dayfirst=True)

ventas_mes = df.groupby(
    df["fecha"].dt.to_period("M")
)["total_venta"].sum()

print(ventas_mes)
plt.figure(figsize=(10,5))

ventas_mes.plot()

plt.xlabel("Año-Mes")
plt.ylabel("Total Ventas")
plt.title("Ventas por Año y Mes")

plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')

plt.show()