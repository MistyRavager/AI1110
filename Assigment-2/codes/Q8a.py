import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
import sympy as sp

#input 
# f(x) = 4x^3 - 3x + 5

plt.xlabel('$x$')
plt.ylabel('$y$')                             #labellings of x and y axes
plt.xticks(list(range(-2,8,1)))
plt.yticks(list(range(-5,16,1)))

def f(x):
    return 4*(x**3) - 3*x + 5

def plot_tangent(x_roots):
    y_roots = []                                #contains y coordinates of roots
    for i in x_roots:
        y_root = 4*(i**3) - 3*i + 5
        y_roots.append(y_root)

        plt.plot(i,y_root,marker = 'o')

        x2values = np.linspace(-1.5,1.5,100)
        y2values=[]
        slope = mp.diff(lambda x : 4*(x**3) - 3*x + 5, i)      #calculates slope at roots

        plt.annotate(f'({i},{y_root})',xy=(i,y_root-1))     #i is x_root
            
        for j in x2values:
            y2 = y_root - slope * (i - j)
            y2values.append(y2)
        plt.plot(x2values,y2values,label = f'$y = {y_root}$')   #plots the tangent
    return y_roots


xvalues = np.linspace(-1.5,1.5,num=100)
yvalues = f(xvalues)
plt.plot(xvalues,yvalues,label='curve $y = 4x^3 -3x +5$')    #plots curve


x = sp.symbols('x')
f1_x = sp.diff(4*(x**3) - 3*x + 5,x)            #returns differential of original curve

x_roots = sp.solve(f1_x)                      #finds roots of f'(x)
y_roots = plot_tangent(x_roots)

plt.legend(loc = 'lower right')

plt.grid()
plt.show()