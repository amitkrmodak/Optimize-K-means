
from pandas import *
import numpy as np
def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


input_data=[]

data = read_csv("UCI_dataSet\individual+household+electric+power+consumption\Book2.csv")
c1 = data['Global_active_power'].tolist()
c2 = data['Voltage'].tolist()
for i in range(0, 1000000):
    input_data.append([])
    input_data[i].append(c1[i])
    input_data[i].append(c2[i])
# input_data=[[4,21],[5,19],[20,24],[15,22],[14,19],[14,16],[11,17],[18,20],[15,12],[19,14],[8,7],[10,12],[4,21],[15,18],[12,15],[14,16],[15,12],[1,4],[1,5],[2,8],[3,9],[6,14],[3,18],[5,10],[6,18],[5,18],[4,20],[8,25],[15,17],[10,10],[11,11],[12,11],[13,11],[15,10],[16,11]]
print("len of input data",len(input_data))
res = np.unique(np.array([np.sort(sub) for sub in input_data]), axis=0)
dd=res.tolist()
# print("The list after duplicate removal : " , dd)
print("len of duplicate removal data",len(dd))
# print(type(dd))
# print(Repeat(input_data))

