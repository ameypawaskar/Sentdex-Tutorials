import matplotlib.pyplot as plt

'''x = [2,4,6,8,10]
y = [4,6,9,2,5]

x2 = [1,3,5,7,9]
y2 = [7,5,6,1,3]

plt.bar(x,y, label='Bars1', color='blue')
plt.bar(x2,y2, label='Bars2', color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intresting Graph\nCheck it out')
plt.legend()
plt.show()'''

population_ages = [70,65,89,6,45,5,48,2,12,45,63,85,45,12,65,47,45,48,42,87,45,25,1,65,85,32,36,95,51,14,5,125,130,69,109,111,15,65]

#ids = [x for x in range(len(population_ages))]
#plt.bar(ids, population_ages)

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.5 )

plt.xlabel('x')
plt.ylabel('y')
plt.title('Intresting Graph\nCheck it out')
plt.legend()
plt.show()
