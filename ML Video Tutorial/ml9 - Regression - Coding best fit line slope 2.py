import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6], dtype=np.float64)
ys = np.array([5,4,6,5,6,7],dtype=np.float64)

##plt.scatter(xs,ys)
##plt.show()

def best_fit_slope_and_intercept(xs,ys):
    m = ( ((mean(xs) * mean(ys)) - mean(xs*ys)) /
          ((mean(xs) * mean(xs)) - mean(xs*xs)))
    c = mean(ys) - m*mean(xs)
    return m,c

m,c = best_fit_slope_and_intercept(xs,ys)
##print(m,c)

regression_line = [(m*x)+c for x in xs]
## above expression is short version for
## for x in xs:
##      regression_line.append = ((m*x)+c)

predict_x = 9
predict_y = (m*predict_x) + c

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y, color = 'r')
plt.plot(xs,regression_line)
plt.show()
