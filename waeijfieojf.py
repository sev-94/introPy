import datetime
import plotly.offline as py
import plotly.graph_objs as go
from pandas_datareader as web

start = datetime.datetime(2014,1,1)
end = datetime.datetime(2018,1,1)

FB = web.DataReader('FB', 'yahoo', start, end)
TW = web.DataReader('TWTR', 'yahoo', start, end)
APPL = web.DataReader('APPL', 'yahoo', start, end)

print(FB)