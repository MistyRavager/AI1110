#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)

#randvar = np.loadtxt('../dat_files/gau.dat',dtype='double')


#--------------theoritical for U ------------------
#randvar = np.loadtxt('../dat_files/uni.dat',dtype='double')
# theo = []
# a = np.linspace(-4,4,simlen)
# for i in a.tolist():
# 	if i<=0: theo.append(0)
# 	elif i<1 and i>0 : theo.append(i)
# 	else : theo.append(1)

# plt.plot(a.T,theo)
# plt.plot(x.T,err,"bo")#plotting the CDF
# plt.grid() #creating the grid
# plt.xlabel('$x$')
# plt.ylabel('$F_U(x)$')
# plt.legend(["Theory","Numerical"])
#----------------------------------------------

#---------------theoritical for V-----------------------
randvar = np.loadtxt('../dat_files/V.dat',dtype='double')
theo = []
a = np.linspace(-4,4,simlen)
for i in a.tolist():
	if i<=0: theo.append(0)
	elif i>0: theo.append(1-np.exp(-i/2))

plt.plot(a.T,theo)
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_U(x)$')


#----------------------------------------------

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
plt.plot(x.T,err,"bo")#plotting the CDF
plt.legend(["Theory","Numerical"])
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
