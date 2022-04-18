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
for i in range(min_cls_interval,max_cls_interval+class_length*2,5):
    bin.append(i)

class_intervals = [f"{bin[ind]}-{bin[ind+1]}" for ind,i in enumerate(bin[:len(bin)-1])]


# using inbuilt function for frequencies / class indices
hist = np.histogram(raw_data,bins=bin)

# writing to excel file
write = pd.DataFrame({"Relative Humidity":class_intervals,"Frequency":hist[0]})
write.to_excel('tables/frequency_distribution.xlsx',index=False)