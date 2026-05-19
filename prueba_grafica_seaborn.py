import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "dias": [1,2,3],
    "ventas": [100,200,150]
})

sns.lineplot(data=df, x="dias", y="ventas")

plt.show()