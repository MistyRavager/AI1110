'''python code for finding the length PT 
Given: Angles of elevations QPR & PQT
       Length of QR'''

import matplotlib.pyplot as plt
import numpy as np

x='x'
y='y'

#--------------------------------
#input parameters
angle_QPR=np.pi/3
angle_PQT=np.pi/6

Q={x:40,y:0}
R={x:40,y:50}
#--------------------------------

plt.xticks(list(range(-2,Q[x]+10,2)))
plt.yticks(list(range(-2,R[y]+10,2)))

plt.plot([Q[x],R[x]],[Q[y],R[y]])
plt.annotate('Q',xy=(Q[x]+0.25,Q[y]))
plt.annotate('R',xy=(R[x]+0.25,R[y]))

P={x:0,y:0}
P[x]=Q[x]-((R[y]-Q[y])/np.tan(angle_QPR))
P[y]=Q[y]

plt.plot([Q[x],P[x]],[Q[y],P[y]])
plt.plot([R[x],P[x]],[R[y],P[y]])
plt.annotate('P',xy=(P[x]-0.5,P[y]-1))

T={x:0,y:0}
T[x]=P[x]
T[y]=P[y]+np.tan(angle_PQT)*(Q[x]-P[x])

plt.plot([T[x],P[x]],[T[y],P[y]])
plt.plot([T[x],Q[x]],[T[y],Q[y]])
plt.annotate('T',xy=(T[x]-0.5,T[y]))

PT=round(T[y]-P[y])
plt.grid()

#answer given in graph
plt.title("PT = {}m after rounding off".format(PT))

plt.show()


