import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"

data = {
    "dia": [1,2,3,4],
    "ventas": [100,150,120,200],
    
}

df = pd.DataFrame(data)

fig = px.scatter(
    df,
    x="dia",
    y="ventas",
    trendline="ols"
    )

# convertir puntos a línea + puntos
fig.update_traces(mode="lines+markers")
fig.show()