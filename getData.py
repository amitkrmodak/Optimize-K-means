from pandas import *


input_data=[]
data = read_csv("UCI_dataSet\gas-sensor-array-temperature-modulation/20161013_143355.csv")
c1 = data['R10 (MOhm)'].tolist()
c2 = data['Flow rate (mL/min)'].tolist()
for i in range(0, len(c1)):
    input_data.append([])
    input_data[i].append(c2[i])
    input_data[i].append(c1[i])
j = len(c1)
# data = read_csv("UCI_dataSet\gas-sensor-array-temperature-modulation/20161013_143355.csv")
c1 = data['R5 (MOhm)'].tolist()
c2 = data['Time (s)'].tolist()
for i in range(0, len(c1)):
    input_data.append([])
    input_data[j].append(c2[i])
    input_data[j].append(c1[i])
    j = j + 1