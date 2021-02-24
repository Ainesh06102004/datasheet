import pandas as pd
import plotly.express as px

data = pd.read_csv("data.csv")

figure = px.scatter(data, x = "Population", y = "Per capita", size = "Population", color = "Country")
figure.show()