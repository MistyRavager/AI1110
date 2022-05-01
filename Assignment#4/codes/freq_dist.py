import numpy as np
import pandas as pd
#reading from excel sheet
read = pd.read_excel("input.xlsx","Sheet1")
data = np.array(read)
values = list(data[0])+list(data[1])

blood_groups = ['O','A','B','AB']
frequencies = [values.count(i) for i in blood_groups]
#creating dataframe of the frequency table and writing to excel
write = pd.DataFrame({"Blood Groups":blood_groups,"Frequency":frequencies})
write.to_excel("output.xlsx",index=False)