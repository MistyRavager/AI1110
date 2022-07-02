#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if


maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
# randvar = np.loadtxt('../dat_files/gau.dat',dtype='double')
randvar = np.loadtxt('../dat_files/tri.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def tri(i):
	if i > 0 and i < 1:
		return i
	elif i > 1 and i < 2:
		return 2 - i
	else:
		return 0

def gauss_pdf(x):
	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)
	
vec_gauss_pdf = scipy.vectorize(gauss_pdf)
vect2 = np.vectorize(tri, otypes=[np.float])

plt.plot(x[0:(maxrange-1)].T,pdf,"bo")
# plt.plot(x,vec_gauss_pdf(x))#plotting the PDF
a = np.linspace(-4,4,100)
plt.plot(a.T,vect2(a))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$p_T(x)$')

plt.legend(["Numerical","Theory"])

#if using termux
#plt.savefig('../figs/uni_pdf.pdf')
#plt.savefig('../figs/uni_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_pdf.pdf')
#plt.savefig('../figs/gauss_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
#else
plt.show() #opening the plot window
