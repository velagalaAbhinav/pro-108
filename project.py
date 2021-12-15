import plotly.figure_factory as ff 
import random
import pandas as pd 
import csv

df = pd.read_csv('data.csv')
AvgRatingData = df['Avg Rating'].tolist()
fig = ff.create_distplot([AvgRatingData],['AvgRating'],show_hist = False)
fig.show()