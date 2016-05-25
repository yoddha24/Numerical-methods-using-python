import numpy as np

def function(x):
	return x**2-1

def bisection(f,x1,x2,tolerance):
	f1=f(x1)
	f2=f(x2)
	if f1*f2 > 0.0:
		print '(x1,x2) is not a valid interval'
		return
	N=np.ceil(np.log(abs(x2 - x1)/tolerance)/np.log(2.0))
	n=int(N)	
	for i in range(n):
		x3 = 0.5*(x2+x1)
		f3=f(x3)
		if f3 ==0.0:
			return x3
		if f2*f3 <0.0:
			x1=x3
			f1=f3
			print "Iteration %d yields the answer %f"%(i,x3)
		else:
			x2=x3
			f2=f3
			print "Iteration %d yields the answer %f"%(i,x3)
	return (x1+x2)/2.0

answer=bisection(function,-1,1,1.0e-6)
print '\nThe final answer is: %f'%answer

#Checking the answer
error=function(answer)
print '\nerror in approximation is: %f'%error

if error == 0.0:
	print '\nBisection got exact root as %f\n'%answer
else:
	print '\nBisection got approximate root as %f\n'%answer
