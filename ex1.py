# Importing useful Modules

import matplotlib.pylab as pl

# Defining data on axes

x=[0,1,2,3]
y=[0,1,2,3]

#Defining plotting guidelines
pl.plot(x,y)
pl.title('Plotting distance versus time')
pl.xlabel('x (time in hours)')
pl.ylabel('y (distance in Km)')
pl.show()
