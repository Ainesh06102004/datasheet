import pandas as pd
import plotly.express as px

data = pd.read_csv("data.csv")

figure = px.bar(data, x = "Country", y = "Per capita", color="Country")
figure.show()