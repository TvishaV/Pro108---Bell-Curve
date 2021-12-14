import pandas as pd 
import csv
import plotly.figure_factory as ff

df = pd.read_csv("mobileRating.csv")
figure = ff.create_distplot([df["Avg Rating"].tolist()] , ["Mobile Brand"])
figure.show()