import pandas as pd 
df = pd.read_csv('dataset_ventas_pandas.csv')
print (df.dtypes)
print (df.info())
print(df.to_string())
#print(df.head())   devuelve los encabezados y las primeras 5 filas
# print(df.tail())  devuelve las ultimas 5 filas de la tabla 