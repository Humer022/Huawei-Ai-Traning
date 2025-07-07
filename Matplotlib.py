import matplotlib.pyplot as plt
import numpy as np
#plot graph using arrays
'''xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()'''

#plot graph on x axix and y axis
'''xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)
plt.show()'''

#use marker
'''ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints, marker= "o")
plt.show()'''

#uese marker with marker size and marker face color
'''ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mfc='r')
plt.show()'''

#change line color
'''ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dotted', color='r')
plt.show()'''

#using linewidth
'''ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = '20.5')
plt.show()'''

#Adding more plot
'''y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)
plt.show()'''

#create labels and title for plot
'''x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.title("sport watch data")
plt.show()'''

#using grid function
'''x = np.array(['atif','babar azam','shoaib malik','shaheen shah','ch zohan'])
y = np.array([50,70,60,30,90])
plt.plot(x , y)
plt.xlabel("crickter name")
plt.ylabel("score")
plt.title("Match results")
plt.grid(axis="y",color='g',linestyle='--',linewidth=0.5)
plt.show()'''

#Display Multiple Plots (cont) with Title & Super Title
'''x = np.array([4,5,7,3,8,2])
y = np.array([5,10,20,15,30,25])
plt.subplot(1,2,1)
plt.plot(x ,y)
plt.title('sales')
#plot # 2
x = np.array([2,8,4,6,9,1])
y = np.array([12,22,33,66,44,88])
plt.subplot(1,2,2)
plt.plot(x ,y)
plt.title('income')

plt.suptitle('Meta sales')
plt.show()'''

#Matplotlib Scatter
'''x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y, color='r')

plt.show()'''

#Creating Bar Graphs
'''x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y, color='r',width=0.5,linestyle='--' )
plt.show()'''

#creating histogram graphs
'''x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()'''

#Creating Pie Charts
'''y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()'''

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()





