import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter

style.use('fivethirtyeight')

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [5,7]

##for i in dataset:
##    for ii in dataset[i]:
##        plt.scatter(ii[0],ii[1], s=100, color=i)
##        plt.show()

[[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0],new_features[1], s=100, color='y')
plt.show()

#euclidean_distance = sqrt((plot1[0]-plot2[0])**2 + (plot1[1]-plot2[1])**2 )
#print(euclidean_distance)

def k_nearest_neighbors(data, predict, k=3):
    if len(data) >=k:
        warnings.warn('k is set to a value less than total voting groups!')

    knnalogs
    return vote_result
