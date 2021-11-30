import numpy as np
import matplotlib.pyplot as plt


i=0 #initial iteration number
x=-3    #initial point at x
y=0.0024    #initial point at y
h=0.1   #how many space between iterations

ex=[]
yei=[]

fig, ax = plt.subplots()
plt.title("Newton - 0.1 Interval")
ax.set_xlabel("X", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_ylabel("Y", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
ax.set_xlim([-3,2.5])

while(x<2.6):
    newton=[i,round(x,2),round(y,4)]
    ex.append(x)
    f=(y*x**2)-y
    
    yei.append(y)
    newton.append(round(f,4))
    x=x+h
    y=y+(h*f)
    print(newton)

ax.scatter(ex, yei)
plt.show()