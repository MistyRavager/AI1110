from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

#Number of trials, probability of success
n = 2
p = 1/4

#Binomial Random Variable
rv = binom(n, p)

#X axis
x_val = np.arange((n+1))

#CDF Values (Y axis)
cdf_val = rv.cdf(x_val)

#Plot
plt.plot(x_val, cdf_val, 'ro')
plt.vlines(x_val, 0, cdf_val, colors='k', label='Probability')
plt.legend(loc = 'best', frameon = True)

plt.show()