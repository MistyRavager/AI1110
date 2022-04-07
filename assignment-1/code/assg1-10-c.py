'''python code for finding the length PT 
Given: Angles of elevations QPR & PQT
       Length of QR'''

import matplotlib.pyplot as plt
import numpy as np


#--------------------------------
#input parameters
angle_QPR=np.pi/3
angle_PQT=np.pi/6

h = 50 #length of QR
#--------------------------------
#setting up graph outline

plt.xticks(list(range(-2,44,2)))
plt.yticks(list(range(-2,h+4,2)))
plt.grid()
#--------------------------------
#plotting of lines and calculating lengths of other parameters
plt.plot([40,40],[h,0])

d = h/np.tan(angle_QPR)  # length of base PQ

plt.plot([40,40-d],[0,0])
plt.plot([40,40-d],[h,0])
plt.annotate('P',xy=(40-d-0.5,-1))

h2 = np.tan(angle_PQT)*(d)  # length of PT 

plt.plot([40-d,40-d],[h2,0])
plt.plot([40-d,40],[h2,0])

#--------------------------------
#labellings

plt.annotate('Q',xy=(40+0.25,0))
plt.annotate('R',xy=(40+0.25,h))
plt.annotate('T',xy=(40-d-0.5,h2))
plt.annotate('h',xy=(40.25,28))
plt.annotate('d',xy=(25,-1.5))
plt.annotate('h2',xy=(40-d-1,8))

#---------------------------------
#answer given in graph
plt.title(f"PT = {round(h2)}m after rounding off")

plt.show()
