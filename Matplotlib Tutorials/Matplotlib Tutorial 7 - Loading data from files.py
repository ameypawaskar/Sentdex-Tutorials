import matplotlib.pyplot as plt

## PART 1
'''import csv

x = []
y = []

with open('example.txt','r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label='Loaded from File!')
'''

## PART 2 - Using Numpy
import numpy as np

x,y = np.loadtxt('example.txt', delimiter=',', unpack=True)

plt.plot(x,y, label='Loaded from File!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intresting Graph\nCheck it out')
plt.legend()
plt.show()
