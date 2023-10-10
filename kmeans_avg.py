import matplotlib.pyplot as plt
import math
import random
import time
import functools
import numpy as np
from pandas import *
import getData_Csv
def sortFunction(a, b):
    if (a[0] == b[0]):
        return 0;

    else:
        if (a[0] < b[0]):
            return -1
        return 1;
def sortArr(arr, n, p):

    vp = [0 for _ in range(n)]
    # Storing the distance with its
    # distance in the vector array
    for i in range(n):
        dist = math.sqrt(pow((p[0] - arr[i][0]), 2) + pow((p[1] - arr[i][1]), 2))
        vp[i] = [dist, [arr[i][0], arr[i][1]]];
    vp.sort(key=functools.cmp_to_key(sortFunction));

    return(vp)

def cal_distance(p1, p2):
    if(not p1) or (not p2):
        distance = 0
    else:
        distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

    return round(distance)

def copyData(x):
    l=len(x)
    p_dataset.clear()
    for i in range(0, l):
        p_dataset.append(x[i])

def cal_centroid(centroid,k):
    #print("dataset 24=", dataset)
    #print("centroid 25=", centroid)
    l=[]
    for i in range(0, k):
        #print("centroid dataset=",dataset[i])
        temp=dataset[i]
        #print("temp=",temp)
        if not temp:
            print("list is  empty")
            centroid.append([])
        else:
            ln = len(temp)
            l.clear()
            tx=0
            ty=0
            for j in range(0, ln):
                temp1 = temp[j]
                tx = tx+temp1[0]
                ty = ty+temp1[1]
            tx = round(tx/ln)
            ty = round(ty/ln)
            l.append(tx)
            l.append(ty)
            #print("l=", l)
            centroid[i].append(tx)
            centroid[i].append(ty)
            # rand_data = random.choice(temp)
            # centroid.append(rand_data)
    #print("centroid=",centroid)

def blankDelete(data,k):
    l=10-k
    for i in range(0, l):
        data.pop()


input_data = getData_Csv.input_data

res = np.unique(np.array([np.sort(sub) for sub in input_data]), axis=0)
input_data=res.tolist()
#input_data = [[4,21],[5,19],[20,24],[15,22],[11,17],[18,20],[19,14],[8,7],[10,12],[15,18],[12,15],[14,16],[15,12],[1,4],[1,5],[2,8],[3,9],[6,14],[3,18],[5,10],[6,18],[5,18],[4,20],[8,25],[15,17],[10,10],[11,11],[12,11],[13,11],[15,10],[16,11]]
print("Length of input data=",len(input_data))
k=int(input("Enter the K="))

#print(input_data)
#len=len(input_data)
centroid = []
int_centroid = []
p_centroid = []
dataset = [[],[],[],[],[],[],[],[],[],[]]
blankDelete(dataset,k)
p_dataset = []
initial_dis = []
iteration=0
x=[[]]
y=[[]]
execution_time =0


tx=0
ty=0
center=[]
for i in range(0, len(input_data)):
    p=input_data[i]
    tx += p[0]
    ty +=p[1]
tx=int(tx/len(input_data))
ty=int(ty/len(input_data))
center.append(tx)
center.append(ty)
print("center=",center)

vp=sortArr(input_data, len(input_data), center)
print(vp[0])
with open('min_vp.txt', 'w') as f:
    f.write(f"{vp}")
mid_vp=int(len(vp)/2)
mid_vp = mid_vp + 1
int_centroid.append(vp[mid_vp])
# for i in range(0, len(vp)):
#     if vp[i][0] ==0:
#         vp.pop(i)
# int_centroid.append(vp[0])
# print(int_centroid)

i=mid_vp+1
# for k in range(1, tk):
l=1
while(l!=k):
    flag=1
    for j in range(0, len(int_centroid)):
        dis=cal_distance(int_centroid[j][1],vp[i][1])
        if(dis < int_centroid[j][0]):
            flag=0
            l=l-1

    if(flag==1):
        int_centroid.append(vp[i])
    # print("flg=",flag)
    l=l+1
    i=i+1
print("int_centroid",int_centroid)
for i in range(0, len(int_centroid)):
    centroid.append(int_centroid[i][1])
print("centroid",centroid)

start = time.time()
while p_dataset != dataset:
    # print("Compare=",p_dataset != dataset)10
    copyData(dataset)
    dataset = [[], [], [], [], [], [], [], [], [], []]


    # print("dataset=", dataset)
    # print("P_dataset=", p_dataset)
    cls_index=0
    data =[]
    for i in range(0, len(input_data)):
        prev_dis = 10000000000000
        for j in range(0, k):
            # print("input data=",input_data[i])
            # print("cntrd=",centroid[j])
            dis=cal_distance(input_data[i], centroid[j])
            #print("distance=", dis)
            if prev_dis > dis :
                data=input_data[i]
                cls_index=j
                prev_dis=dis

            #print("------------------")

        # print("data=",data)
        # print("cls_index=",cls_index)
        dataset[cls_index].append(data)
        # print("dataset=",dataset)
        # print("P_dataset=", p_dataset)
        # print("===========================")
    # print("dataset=", dataset)
    blankDelete(dataset, k)
    # print("dataset=",dataset)
    # print("P_dataset=", p_dataset)
    centroid.clear()
    centroid = [[], [], [], [], [], [], [], [], [], []]
    blankDelete(centroid, k)
    cal_centroid(centroid, k)
    iteration = iteration + 1
    # for i in range(0, k):
    #     temp=dataset[i]
    #     centroid.append(random.choice(temp))
    # print("centroid=",centroid)
    # print("Compare=", p_dataset != dataset)
    # print("loop_count=",loop_count)
    #print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
end = time.time()
execution_time = end - start
#print("dataset=",dataset)
#print("total iteration=",loop_count)
wcss=0
for i in range(0, len(dataset)):
    temp = dataset[i]
    dis = 0
    for j in range(0, len(temp)):
        dis += cal_distance(temp[j], centroid[i])
    wcss += dis
print("wcss=",wcss)
print("itr=",iteration)
execution_time = execution_time *1000
print("Total time=",execution_time)
i=1
with open('standard_output_avg.txt', 'w') as f:
    for line in centroid:
        f.write("Centroid of cluster ")
        f.write(f"{i}\n")
        i += 1
        f.write(f"{line}\n")
    f.write("\nK=")
    f.write(f"{k}\n")
    f.write("\nTotal time =")
    f.write(f"{execution_time}\n")
    f.write("\nTotal iteration =")
    f.write(f"{iteration}\n")


x=[]
y=[]
l1 = len(dataset)
for i in range(0, l1):
    temp1=dataset[i]
    l2=len(temp1)
    for j in range(0, l2):
        temp2 = temp1[j]
        x.append(temp2[0])
        y.append(temp2[1])
    # print("X=",x)
    # print("Y=",y)
    plt.scatter(x, y)
    x.clear()
    y.clear()

plt.title("Standard K-means Clustering(min)")
# plt.title("Data Set")
plt.xlabel('x -->')
plt.ylabel('y -->')
plt.show()


