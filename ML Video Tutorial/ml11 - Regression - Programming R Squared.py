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

def squared_error(ys_orig, ys_line):
    return sum((ys_line-ys_orig)**2)

def coefficient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean) 

m,c = best_fit_slope_and_intercept(xs,ys)
##print(m,c)

regression_line = [(m*x)+c for x in xs]
## above expression is short version for
## for x in xs:
##      regression_line.append = ((m*x)+c)

predict_x = 9
predict_y = (m*predict_x) + c

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y, color = 'r')
plt.plot(xs,regression_line)
plt.show()
