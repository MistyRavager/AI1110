from audioop import avg
import numpy as np
import pandas as pd

def cls_interval(a):
    if a%10<5:
        return a - (a%10)
    else: return a - (a%10) + class_length

#reading from excel
read = pd.read_excel(r'tables/raw_data.xlsx')
raw_data = np.array(read)

#generating bins and class intervals
max_h = np.amax(raw_data)
min_h = np.amin(raw_data)
class_length = 5
min_cls_interval = cls_interval(min_h)
max_cls_interval = cls_interval(max_h)
bin=[]
bin.append(i for i in range(min_cls_interval,max_cls_interval+class_length*2,5))

class_intervals = [f"{bin[ind]}-{bin[ind+1]}" for ind,i in enumerate(bin[:len(bin)-1])]


# using inbuilt function for frequencies / class indices
hist = np.histogram(raw_data,bins=bin)

# writing to excel file
write = pd.DataFrame({"Relative Humidity":class_intervals,"Frequency":hist[0]})
write.to_excel('tables/frequency_distribution.xlsx',index=False)

#------------------------------------
#properties

range = max_h - min_h #range
sum_h = np.sum(raw_data) #total sum of heights
print(sum_h)
num = len(raw_data)*len(raw_data[0]) #total number of students
avg_h = sum_h / num #average
print(avg_h)
max_i = np.amax(hist[0])
for ind,i in enumerate(hist[0]):
    if i==max_i:
        print(class_intervals[ind]) #most frquent class


