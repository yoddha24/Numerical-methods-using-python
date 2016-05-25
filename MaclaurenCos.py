#Program to compute Cos(30) using Maclauren series

#Importing useful modules
import numpy as np
import matplotlib.pylab as pl

#converting into radians
theta=(30*np.pi)/180

#PART 1: Calculating error w.r.t number of terms

#Calculating various terms of Taylor series
p1 = 1
p2 = (theta**(2))/2
p4 = (theta**(4))/np.math.factorial(4)
p6 = (theta**(6))/np.math.factorial(6)
p8 = (theta**(8))/np.math.factorial(8)
p10 = (theta**(10))/np.math.factorial(10)
p12 = (theta**(12))/np.math.factorial(12)

# various approximations
approx_1= p1-p2; # approximate values using two terms
approx_2= p1-p2+p4; # approximate values using three terms
approx_3= p1-p2+p4-p6; # approximate values using four terms
approx_4= p1-p2+p4-p6+p8; # approximate values using five terms
approx_5= p1-p2+p4-p6+p8-p10; # approximate values using six terms
approx_6 = p1-p2+p4-p6+p8-p10+p12

# Real Value
real_value = np.cos(theta)

# calculation of final errors
error_1 = abs(real_value - approx_1)
error_2 = abs(real_value - approx_2)
error_3 = abs(real_value - approx_3)
error_4 = abs(real_value - approx_4)
error_5 = abs(real_value - approx_5)
error_6 = abs(real_value - approx_6)

# making an error vector for plotting
error = [error_1, error_2, error_3, error_4, error_5,error_6]

# Plotting error versus number of terms
pl.figure(1)
pl.semilogy(error,'bo-')
pl.title('Variation of error in calculating $cos(30^{0}$) using Taylor Series')
pl.xlabel('Number of terms on Taylor Series')
pl.ylabel('log(error)')
pl.show()

#PART 2: Plotting cos(theta) w.r.t number of terms

# Plotting cos(theta) and its various approximations
t=np.linspace(0,6,20)

pl.figure(2)
y = np.cos(t)
pl.subplot(3,3,1)
pl.plot(t,y,t,np.ones(len(t)))
pl.subplot(3,3,2)
pl.plot(t,y,'r*',t,(1-t**2/2))
pl.subplot(3,3,3)
pl.plot(t,y,'r*',t,(1-t**2/2+t**4/np.math.factorial(4)))
pl.subplot(3,3,4)
pl.plot(t,y,'r*',t,(1-t**2/2+t**4/np.math.factorial(4)-t**6/np.math.factorial(6)))
pl.subplot(3,3,5)
pl.plot(t,y,'r*',t,(1-t**2/2+t**4/np.math.factorial(4)-t**6/np.math.factorial(6)+t**8/np.math.factorial(8)))
pl.subplot(3,3,6)
pl.plot(t,y,'r*',t,(1-t**2/2+t**4/np.math.factorial(4)-t**6/np.math.factorial(6)+t**8/np.math.factorial(8)-t**10/np.math.factorial(10)))
pl.subplot(3,3,7)
pl.plot(t,y,'r*',t,(1-t**2/2+t**4/np.math.factorial(4)-t**6/np.math.factorial(6)+t**8/np.math.factorial(8)-t**10/np.math.factorial(10)+t**12/np.math.factorial(12)))
pl.subplot(3,3,8)
pl.plot(t,y,'r*',t,(1-t**2/2+t**4/np.math.factorial(4)-t**6/np.math.factorial(6)+t**8/np.math.factorial(8)-t**10/np.math.factorial(10)+t**12/np.math.factorial(12)-t**14/np.math.factorial(14)))
pl.subplot(3,3,9)
pl.plot(t,y,'r*',t,(1-t**2/2+t**4/np.math.factorial(4)-t**6/np.math.factorial(6)+t**8/np.math.factorial(8)-t**10/np.math.factorial(10)+t**12/np.math.factorial(12)-t**14/np.math.factorial(14)+t**16/np.math.factorial(16)))
pl.show()
