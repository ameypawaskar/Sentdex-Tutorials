import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = quandl.get('NSE/ONGC')
#quandl.get("NSE/WIPRO") In Stock split option it is tough.

df = df[['Open','High','Low','Close','Total Trade Quantity']]

df['HL_PCT'] = (df['High'] - df['Low'])/df['Close'] * 100.0
df['PCT_Change'] = (df['Close'] - df['Open'])/df['Open'] * 100.0

#           price    X           X             X
df = df [['Close','HL_PCT','PCT_Change','Total Trade Quantity']]
 
forecast_col = 'Close'
df.fillna(-99999, inplace=True)

forecast_out  = int(math.ceil(0.1*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(axis=0)###IMP df.dropna(axis = 0) inplace of (inplace=True)
#print(forecast_out)

X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)
y = np.array(df['label'])

#print(len(X),len(y))

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
#print(accuracy)

forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)

df['forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 84600
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

print(df.tail())

df['Close'].plot()
df['forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()










































