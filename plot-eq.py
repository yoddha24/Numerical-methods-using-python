import numpy as np
from matplotlib import pylab as pl

#Defining x and y axis for plotting
x=np.linspace(-2,2,100) # linearly space points on x-axis
y=x**3+x**2+x+1 # equation computer on x-axis points

# Plotting
pl.figure(1)
pl.plot(x,y) #plotting x versus y
pl.grid() # showing grid
pl.title('Plot for the equation: $x^{3}+x^{2}+x+1$')
pl.xlabel('$x$')
pl.ylabel('$y=x^{3}+x^{2}+x+1$')
pl.show()
