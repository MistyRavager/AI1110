import numpy as np

#sample size
N = 10000
# 0 -> Tail
# 1 -> Head
#randomly generate 2-tuples to simulate die throws
probarr1 = np.random.choice(2,size=(N,2),p=[0.25,0.75])
problist = probarr1.tolist()

#count1 is the number of times the desired event ((2,2)) occurs
count1 = problist.count([1,1])
count2 = problist.count([0,1])+problist.count([1,0])
count3 = problist.count([0,0])

print("Empirical probability for no tails is",count1/N)
print("Empirical probability for 1 tail is",count2/N)
print("Empirical probability for 2 tails is",count3/N)