import pandas as pd

df = pd.read_csv('data_file.csv')
print(df.to_string())

#**Remplazar celdas vacias en lugar de eliminar 

new_df2 = df.fillna(0)

print("------------remplazo celdas vacias por 0 --- -----")
print(new_df2.to_string())  

#**Remplazar columnas especificas 

new_df3 = df.fillna({"Calories":13000})

print("------------remplazo celdas vacias en columna calorias por 13000 --------")
print(new_df3.to_string()) 


#** Remplazo de columnas usando media, media o moda mean(), median() y mode()


x = round(df["Calories"].mean(),1)
new_df4 = df.fillna({"Calories": x})

print("------------remplazo celdas vacias en columna calorias por media --------")
print(new_df4.to_string()) 


#** Remplazo de filas donde la duracion sea mayor a 120

new_df5 = df.copy()
for x in new_df5.index:
    if new_df5.loc[x, "Duration"] > 120:
        new_df5.loc[x, "Duration"] = 120


print("------------Remplazo de filas donde la duracion sea mayor a 120 --------")
print(new_df5.to_string()) 

#limpieza de campos vacios sin afectar el dataframe original

print("------------remplazo en nuevo dataframe --------")

new_df = df .dropna()

print(new_df.to_string())   

#**limpieza de datos remplazando en el dataframe original

df.dropna(inplace=True)
print("------------remplazo en original --------")
print(df.to_string())   

# imprimir duplicados mostrara false 
print("------------registros duplicados  --------")
print (df.duplicated())

# con esta sentencia se eliminan los duplicados:  df.drop_duplicates(inplace = True)


# correlacion 
print(df.corr())




