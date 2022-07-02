#Importing numpy, scipy, mpmath and pyplot
from math import erfc, sqrt
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
#if using termux
#import subprocess
#import shlex
#end if

x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('../dat_files/tri.dat',dtype='double')
def Q_func(x):
	return mp.erfc(x/sqrt(2))/2

def gau(x):
	return(1-Q_func(x))
def tri(i):
	# global randvar
	# randvar = np.loadtxt('../dat_files/tri.dat',dtype='double')
	# theo = []
	# a = np.linspace(-4,4,simlen)
	
	if(i < 0):
		return 0
	elif(i > 0 and i < 1):
		return (i**2)/2
	elif(i > 1 and i < 2):
		return 2*i - (i**2)/2 - 1
	else:
		return 1
	
	# plt.plot(a.T,theo)
	# plt.xlabel('$x$')
	# plt.ylabel('$F_T(x)$')


#--------------theoritical for U ------------------
def U():
	global randvar
	randvar = np.loadtxt('../dat_files/uni.dat',dtype='double')
	theo = []
	a = np.linspace(-4,4,simlen)
	for i in a.tolist():
		if i<=0: theo.append(0)
		elif i<1 and i>0 : theo.append(i)
		else : theo.append(1)

	plt.plot(a.T,theo)
	plt.xlabel('$x$')
	plt.ylabel('$F_U(x)$')
	
#----------------------------------------------

#---------------theoritical for V-----------------------
def V():
	global randvar
	randvar = np.loadtxt('../dat_files/V.dat',dtype='double')
	theo = []
	a = np.linspace(-4,4,1000)
	for i in a.tolist():
		if i<=0: theo.append(0)
		elif i>0: theo.append(1-np.exp(-i/2))

	plt.plot(a.T,theo)
	plt.xlabel('$x$')
	plt.ylabel('$F_V(x)$')

#----------------------------------------------
# tri()

a = np.linspace(-4,4,1000)
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
# vect = np.vectorize(gau, otypes=[np.float])
vect2 = np.vectorize(tri, otypes=[np.float])
plt.plot(a,vect2(a))
# plt.plot(a, vect(a))
# plt.plot(x.T,err,"bo")#plotting the CDF
plt.grid()	
plt.legend(["Theory","Numerical"])
# plt.legend(["Theory","Numerical"])
#if using termux
#plt.savefig('../figs/uni_cdf.pdf')
#plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
