import plotly.plotly as py
import plotly.graph_objs as go
import plotly

from data_writer import numOfEachColor

plotly.tools.set_credentials_file(username='JohnPolich', api_key='Q833pymOHavNzWGFDruA')
filename = "data.csv"
colorsDict = numOfEachColor(filename)
labels = list(colorsDict.keys())

values = list(colorsDict.values())
for i in labels:
    print(i )
for i in values:
    print(i)

trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='basic_pie_chart')



