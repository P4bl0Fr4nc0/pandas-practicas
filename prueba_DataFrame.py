import pandas as pd

data = {
  "calories": ["1280","530","720"],
  "duration":["75","40","55"]
    }

df = pd.DataFrame(data, index = ["dia 1", "dia 2", "dia 3"])

'''imprime todas las calorias'''
print (df["calories"])

print("--------------------")
'''imprime las calorias de la posicion 0'''
print(df.loc["dia 1"]["calories"])
print("--------------------")
'''imprime la duraicon de la posicion 0'''
print(df.loc["dia 1"]["duration"])
print("--------------------")
'''imprime la fila 0'''
print(df.loc["dia 1"])
print("--------------------")
'''filas 0 y 1'''
print(df.loc[["dia 1","dia 2"]])