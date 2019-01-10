import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression


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
print(forecast_out)

X = np.array(df.drop(['label'],1))
y = np.array(df['label'])
X = preprocessing.scale(X)
#X = X[:-forecast_out+1]
df.dropna(inplace=True)
#y = np.array(df['label'])

print(len(X),len(y))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
clf = LinearRegression()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print(confidence)











