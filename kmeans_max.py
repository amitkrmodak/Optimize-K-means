import matplotlib.pyplot as plt
import math
import random
import time
from pandas import *
import numpy as np
import getData_Csv
def cal_distance(p1, p2):
    # print(p1)
    # print(p2)
    if(not p1) or (not p2):
        distance = 0
    else:
        distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

    return (distance)

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

input_data =getData_Csv.input_data

# res = np.unique(np.array([np.sort(sub) for sub in input_data]), axis=0)
# input_data=res.tolist()
#input_data = [[4,21],[5,19],[20,24],[15,22],[11,17],[18,20],[19,14],[8,7],[10,12],[15,18],[12,15],[14,16],[15,12],[1,4],[1,5],[2,8],[3,9],[6,14],[3,18],[5,10],[6,18],[5,18],[4,20],[8,25],[15,17],[10,10],[11,11],[12,11],[13,11],[15,10],[16,11]]
print("Length of input data=",len(input_data))
k=int(input("Enter the K="))

# print(input_data)
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

# unique_list = []
# seen = set()
# for sublist in input_data:
#     # Convert each sublist to a tuple since lists are unhashable
#     sublist_tuple = tuple(sublist)
#
#     if sublist_tuple not in seen:
#         # Add the sublist to the unique_list
#         unique_list.append(list(sublist_tuple))
#
#         # Add the sublist_tuple to the set of seen tuples
#         seen.add(sublist_tuple)
# input_data=unique_list
# ###################   max algo to determine the initial centroid #####################


int_centroid=[]
DM = []
    # m = mean([dataset])
x_sum = 0
y_sum = 0

for i in range(0, len(input_data)):
        # element_data = [input_data[i]]
        test_data = input_data[i]
        #print("test data =", input_data[i])
        #print("test element =", test_data[0])
        x_sum = x_sum + test_data[0]
        #print("test element =", test_data[1])
        y_sum = y_sum + test_data[1]
#print("x sum ", x_sum)
#print("y sum ", y_sum)
mean_x = round(x_sum / len(input_data))
mean_y = round(y_sum / len(input_data))
#print("x mean ", mean_x)
#print("y mean ", mean_y)
mean_point = [mean_x, mean_y]
print(mean_point)
# print("grand mean ", mean_point)

for j in range(0, len(input_data)):
        Dis = cal_distance(input_data[j], mean_point)
        DM.append(Dis)
        # print("distance=", Dis)
max_value = max(DM)
max_value_index = DM.index(max(DM))
# print("accumulated distant matrix ", DM)
# print("maximum among the list ", max_value)
# print("maximum value index among the list ", max_value_index)
centroid1 = input_data[max_value_index]
# print("centroid1 = ", centroid1)
centroid.append(input_data[max_value_index])
int_centroid.append(input_data[max_value_index])
DM[max_value_index] = 0
# print("final DM", DM)

for p in range(1, k):
    for q in range(0, len(input_data)):
            # print(DM)
            Dis1 = cal_distance(input_data[q], centroid1)
            # print("distance=", Dis1)
            if DM[q] != 0:
                DM[q]=Dis1
    max_value = max(DM)
    max_value_index = DM.index(max(DM))
    # print("accumulated distant matrix ", DM)
    # print("maximum among the list ", max_value)
    # print("maximum value index among the list ", max_value_index)
    new_cen = input_data[max_value_index]
    # print("centroid ", new_cen)
    centroid.append(input_data[max_value_index])
    int_centroid.append((input_data[max_value_index]))
    centroid1 = new_cen
    DM[max_value_index] = 0


print("initial centroids", centroid)

##################### max algo to determine theb initial centroid #######################

start = time.time()
while p_dataset != dataset:
    # print("Compare=",p_dataset != dataset)
    copyData(dataset)
    dataset = [[], [], [], [], [], [], [], [], [], []]


    # print("dataset=", dataset)
    # print("P_dataset=", p_dataset)
    cls_index=0
    data =[]
    for i in range(0, len(input_data)):
        prev_dis = 10000000000
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
with open('standard_output_max.txt', 'w') as f:
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
print("int_cen=",int_centroid)
print("cen=",centroid)
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
int_centroid_x=[]
int_centroid_y=[]
for i in range(0, len(int_centroid)):
    temp1 = int_centroid[i]
    int_centroid_x.append(temp1[0])
    int_centroid_y.append(temp1[1])
    plt.scatter(int_centroid_x, int_centroid_y,marker='*',color='black')
centroid_x=[]
centroid_y=[]
for i in range(0, len(centroid)):
    temp1 = centroid[i]
    centroid_x.append(temp1[0])
    centroid_y.append(temp1[1])
    plt.scatter(centroid_x, centroid_y,marker='*',color='pink')
plt.title("Standard K-means Clustering")
# plt.title("Data Set")
plt.xlabel('x -->')
plt.ylabel('y -->')
plt.show()


