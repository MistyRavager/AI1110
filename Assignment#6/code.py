import numpy as np

#[1,9] => U
#1 => AB
#1,2,3 => A
#1,4,5 => B
#6,7,8,9 => U - (A+B)

#function to count occurrence of event A
def countA(problist):
    return problist.count([1])+problist.count([2])+problist.count([3])

#function to count occurrence of event B
def countB(problist):
    return problist.count([1])+problist.count([4])+problist.count([5])


#sample size
N = 10000

#randomly generate numbers to simulate occuring event
probarr1 = np.random.randint(1,10,size=(N,1))
problist = probarr1.tolist()

#count1 is the number of times the event A occurs
count1 = countA(problist)
probA = count1/N

#count2 is the number of times the event B occurs
count2 = countB(problist)
probB = count2/N

#probAunionB is the probability that the desired event A union B occurs
probAunionB = probA + probB - probA*probB

#probx is the probability of 1-A'B'
probx = 1 - (1-probB)*(1-probA)

#output the empirical probability
print("A union B is",probAunionB)
print("1-A'B' is",probx)