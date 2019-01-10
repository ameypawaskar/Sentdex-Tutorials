import pandas as pd
import quandl

df = quandl.get('NSE/TRIDENT')

df = df[['Open','High','Low','Close','Total Trade Quantity']]

df['HL_PCT'] = (df['High'] - df['Low'])/df['Close'] * 100.0
df['PCT_Change'] = (df['Close'] - df['Open'])/df['Open'] * 100.0

df = df [['Close','HL_PCT','PCT_Change','Total Trade Quantity']]

print(df.head())

