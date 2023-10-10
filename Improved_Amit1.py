import matplotlib.pyplot as plt
import math;
import random;
import numpy;
import time
from pandas import *

def cal_distance(p1, p2):
    # print("p1=",p1)
    # print("p2=",p2)
    if ((not p1) or (not p2)):
        distance = 0
    else:
        # distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
        distance = math.dist(p1, p2)

    return (round(distance))


def copyData(x):
    l = len(x)
    p_dataset.clear()
    for i in range(0, l):
        p_dataset.append(x[i])


def cal_centroid(centroid,k):
    #print("dataset 28=", dataset)
    #print("centroid 29=", centroid)
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
                #print("temp1 45=", temp1)
                tx = tx+temp1[0]
                ty = ty+temp1[1]
            tx = round(tx/ln)
            ty = round(ty/ln)
            centroid[i].append(tx)
            centroid[i].append(ty)
            # rand_data = random.choice(temp)
            # centroid.append(rand_data)
    #print("centroid 54=",centroid)


def blankDelete(data, k):
    l = 10 - k
    for i in range(0, l):
        data.pop()


def createNewDataset(x, cls_index, prev_dis):
    #print(x, "stored in ", cls_index, " and new distance=", prev_dis)
    new_dataset[cls_index].append(x)
    new_distanceset[cls_index].append(prev_dis)


def cal_cluster(x,y):
    #print("After further calculation--")
    prev_dis = 10000
    cls_index=y
    for i in range(0, k):
        dis = cal_distance(x, centroid[i])
        if prev_dis > dis:
            cls_index = i
            prev_dis = dis

    createNewDataset(x, cls_index, prev_dis)
input_data = []
data = read_csv("bank.csv")
c1 = data['age'].tolist()
c2 = data['balance'].tolist()
for i in range(0, len(c1)):
    input_data.append([])
    input_data[i].append(c1[i])
    input_data[i].append(c2[i])

print("Length=",len(input_data))
k = int(input("Enter the K (0 to 10)="))


centroid = []
dataset = [[], [], [], [], [], [], [], [], [], []]
new_dataset = [[], [], [], [], [], [], [], [], [], []]
distanceset = [[], [], [], [], [], [], [], [], [], []]
new_distanceset = [[], [], [], [], [], [], [], [], [], []]
blankDelete(dataset, k)
blankDelete(distanceset, k)
blankDelete(new_dataset, k)
blankDelete(new_distanceset, k)
p_dataset = []
loop_count = 0
x = [[]]
y = [[]]
temp_list = []
step_count = 1
improve_count = 0
wcss = 0
execution_time = 0

#start = time.time()
for i in range(0, k):
    centroid.append(random.choice(input_data))
#print("Initial centroid=", centroid)
start = time.time()
for i in range(0, len(input_data)):
    prev_dis = 10000
    for j in range(0, k):
        # print("cntrd=",centroid[j])
        dis = cal_distance(input_data[i], centroid[j])
        # print("distance=", dis)
        if prev_dis > dis:
            data = input_data[i]
            cls_index = j
            prev_dis = dis

        # print("------------------")

    # print("data=",data)
    # print("cls_index=",cls_index)
    dataset[cls_index].append(data)
    distanceset[cls_index].append(prev_dis)

while p_dataset != dataset:

    step_count += 1
    #print("eeeeeeeeeeeeeeeeeeeeeeeee")
    new_dataset = [[], [], [], [], [], [], [], [], [], []]
    new_distanceset = [[], [], [], [], [], [], [], [], [], []]
    centroid = [[], [], [], [], [], [], [], [], [], []]
    blankDelete(new_dataset, k)
    blankDelete(new_distanceset, k)
    blankDelete(centroid, k)
    cal_centroid(centroid, k)
    # print("Compare=",p_dataset != dataset)

    # print("dataset=", dataset)
    # print("new dataset=", new_dataset)
    # print("distanceset=", distanceset)
    # print("new distanceset=", new_distanceset)
    # print("P_dataset=", p_dataset)
    for i in range(0, len(dataset)):
        data = dataset[i]
        distance = distanceset[i]

        for j in range(0, len(data)):

            # print("input data=",input_data[i])
            # print("cntrd=",centroid[j])
            dis = cal_distance(data[j], centroid[i])
            # print("distace cal data=", data[j])
            # print("dis=", dis)
            # print("dis[j]=", distance[j])

            if dis > distance[j]:

                #print("need further calculation")
                d=data[j]
                cal_cluster(d,j)
            else:
                #print("no need further calculation")
                improve_count += 1
                createNewDataset(data[j], i, dis)

            #print("------------------")

        #print("===========================")

    # print("dataset=", dataset)
    # print("new dataset=", new_dataset)
    # print("distanceset=", distanceset)
    # print("new distanceset=", new_distanceset)
    copyData(dataset)
    l = len(new_dataset)
    dataset.clear()
    distanceset.clear()
    for i in range(0, l):
        dataset.append(new_dataset[i])
        distanceset.append(new_distanceset[i])
    new_dataset.clear()
    new_distanceset.clear()
    # for i in range(0, k):
    #     temp=dataset[i]
    #     centroid.append(random.choice(temp))
    # print("centroid=",centroid)
    # print("Compare=", p_dataset != dataset)
    loop_count += 1

    #print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

end = time.time()
execution_time  += (end-start)
for i in range(0, len(dataset)):
    data = dataset[i]
    for j in range(0, len(data)):
        dis = cal_distance(data[j], centroid[i])
        wcss += dis

print("After calculation-----")

print("improve_count=",improve_count)
print("Total steps=", step_count)
print("wcss for ", k, " cluster = ", wcss)
execution_time = execution_time*1000
print("Total time=",execution_time)
i=1
with open('Improved_output.txt', 'w') as f:
    for line in centroid:
        f.write("Centroid of cluster ")
        f.write(f"{i}\n")
        i += 1
        f.write(f"{line}\n")
    f.write("\nTotal time =")
    f.write(f"{execution_time}\n")
x = []
y = []
l1 = len(dataset)
for i in range(0, l1):
    temp1 = dataset[i]
    l2 = len(temp1)
    for j in range(0, l2):
        temp2 = temp1[j]
        x.append(temp2[0])
        y.append(temp2[1])
    # print("X=",x)
    # print("Y=",y)
    plt.scatter(x, y)
    x.clear()
    y.clear()

plt.title("Improved K-means Clustering")
# plt.title("Data Set")
plt.xlabel('x -->')
plt.ylabel('y -->')
plt.show()
