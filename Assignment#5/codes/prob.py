import numpy as np

#0 => left
#1 => middle
#2 => right
#(son,mother,father)
#function that checks if the tuple x satisfies the conditions of event F
def countF(x):
    if x[0] == x[1] or x[1]==x[2] or x[2]==x[0]:
        return 0
    if x[2] == 1 :
        return 1
    return 0

#sample size
N = 10000

#randomly generate 3-tuples to simulate die throws
probarr1 = np.random.randint(0,3,size=(N,3))
problist = probarr1.tolist()

#count1 is the number of times the desired event A intersection B occurs
count1 = problist.count([0,2,1])
count1 += problist.count([2,0,1])
print(count1)
#code block counts the number of times F occurs
#this value is stored in count2
bitlist = map(lambda x: countF(x), problist)
bitlist = list(bitlist)
count2 = sum(bitlist)
print(count2)
#output the empirical probability
print("Empirical probability is",count1/count2)
