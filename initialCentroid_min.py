import matplotlib.pyplot as plt
import math
import random
import time
import functools
import numpy as np
from pandas import *
import getData_Csv

def cal_distance(p1, p2):
    if(not p1) or (not p2):
        distance = 0
    else:
        distance = (math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)))

    return (distance)
def sortFunction(a, b):
    if (a[0] == b[0]):
        return 0;

    else:
        if (a[0] < b[0]):
            return -1
        return 1;


# Function to sort the array of
# points by its distance from P
def sortArr(arr, n, p):
    # Vector to store the distance
    # with respective elements

    vp = [0 for _ in range(n)]
    # Storing the distance with its
    # distance in the vector array
    for i in range(n):
        dist=cal_distance(p, arr[i])
        # dist = math.sqrt(pow((p[0] - arr[i][0]), 2) + pow((p[1] - arr[i][1]), 2))
        vp[i] = [dist, [arr[i][0], arr[i][1]]];
    vp.sort(key=functools.cmp_to_key(sortFunction));

    return(vp)



int_centroid = []
centroid=[]
input_data = getData_Csv.input_data
tk=3
res = np.unique(np.array([np.sort(sub) for sub in input_data]), axis=0)
input_data=res.tolist()
# data = read_csv("UCI_dataSet\diabetes+130+us+hospitals+for+years+1999+2008\dataset_diabetes\diabetic_data.csv")
# # c1 = data['age'].tolist()
# # c2 = data['balance'].tolist()
# c1 = data['encounter_id'].tolist()
# c2 = data['patient_nbr'].tolist()
# for i in range(0, 100000):
#     input_data.append([])
#     input_data[i].append(c1[i])
#     input_data[i].append(c2[i])

tx=0
ty=0
center=[]
initial_distance= []
distance = []
for i in range(0, len(input_data)):
    p=input_data[i]
    tx += p[0]
    ty +=p[1]
tx=round(tx/len(input_data))
ty=round(ty/len(input_data))
center.append(tx)
center.append(ty)
print("center=",center)

vp=sortArr(input_data, len(input_data), center)

with open('int_centroid.txt', 'w') as f:
    f.write(f"{vp}\n")

for i in range(0, len(vp)):
    if vp[i][0] ==0:
        vp.pop(i)
int_centroid.append(vp[0])
# print(int_centroid)

i=1
# for k in range(1, tk):
k=1
while(k!=tk):
    flag=1
    for j in range(0, len(int_centroid)):
        dis=cal_distance(int_centroid[j][1],vp[i][1])
        # print("Vp[i][1]",vp[i][1])
        # print("dis=",dis)
        # print("cen=",int_centroid[j])
        if(dis < int_centroid[j][0]):
            flag=0
            k=k-1
            break
    if(flag==1):
        int_centroid.append(vp[i])
    print("flg=",flag)
    k=k+1
    i=i+1


print("int_centroid",int_centroid)
for i in range(0, len(int_centroid)):
    centroid.append(int_centroid[i][1])
print("centroid",centroid)