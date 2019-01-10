import pandas as pd
import quandl
import math

df = quandl.get('NSE/TRIDENT')

df = df[['Open','High','Low','Close','Total Trade Quantity']]

df['HL_PCT'] = (df['High'] - df['Low'])/df['Close'] * 100.0
df['PCT_Change'] = (df['Close'] - df['Open'])/df['Open'] * 100.0

df = df [['Close','HL_PCT','PCT_Change','Total Trade Quantity']]
 
forecast_col = 'Close'
df.fillna(-99999, inplace=True)

forecast_out  = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)
print(df.tail(10))
