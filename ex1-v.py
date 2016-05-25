# Importing useful Modules

import matplotlib.pyplot as plt

# Defining data on axes

x=[0,1,2,3]
y=[0,1,4,10]
v=[0,1,3,6]

#Defining plotting guidelines
fig=plt.figure()
ay1=fig.add_subplot(111)
ay2=ay1.twinx() # setting two similar x-axes for two dis-similar y-axis data

ay1.plot(x,y,'bo-')
ay2.plot(x,v,'r*-')
plt.title('Plotting distance and velocity versus time')
ay1.set_ylabel('$y$ (distance in $Km$)')
ay2.set_ylabel('$v$ (velocity in $Km/Hr$)')
plt.show()
