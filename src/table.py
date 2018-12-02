import plotly.plotly as py
import plotly.graph_objs as go

from data_writer import mostRecentColors
import plotly
plotly.tools.set_credentials_file(username='JohnPolich', api_key='Q833pymOHavNzWGFDruA')
filename = "data.csv"

colors = mostRecentColors(filename)
trace = go.Table(
    header=dict(values=["Colors"]),
    cells=dict(values=[mostRecentColors(filename)]))
data = [trace]
py.plot(data, filename = 'Most Recent Colors Chosen')