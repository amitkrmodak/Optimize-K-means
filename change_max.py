import matplotlib.pyplot as plt
import math
import random
import time
import pandas as pd
import numpy as np
import getData_Csv

def cal_distance(p1, p2):
    if (not p1) or (not p2):
        distance = 0
    else:
        distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return distance

def copyData(x):
    l = len(x)
    p_dataset.clear()
    for i in range(0, l):
        p_dataset.append(x[i])

def cal_centroid(centroid, k):
    l = []
    for i in range(0, k):
        temp = dataset[i]
        if not temp:
            centroid.append([])
        else:
            ln = len(temp)
            l.clear()
            tx = 0
            ty = 0
            for j in range(0, ln):
                temp1 = temp[j]
                tx = tx + temp1[0]
                ty = ty + temp1[1]
            tx = round(tx / ln)
            ty = round(ty / ln)
            l.append(tx)
            l.append(ty)
            centroid[i].append(tx)
            centroid[i].append(ty)

def blankDelete(data, k):
    l = 10 - k
    for i in range(0, l):
        data.pop()

input_data = []
input_data = getData_Csv.input_data
# x_data = []
# y_data = []
# read_data = pd.read_csv('UCI_dataSet\diabetes+130+us+hospitals+for+years+1999+2008\dataset_diabetes\diabetic_data.csv')
# data1 = read_data["num_lab_procedures"]
# data2 = read_data["num_medications"]
# for i in range(0, len(data1)):
#     x_data.append(data1[i])
# for j in range(0, len(data1)):
#     y_data.append(data2[j])
# for p in range(0, len(data1)):
#     input_data.append([x_data[p], y_data[p]])

k = int(input("Enter the K: "))

centroid = []
int_centroid = []
p_centroid = []
dataset = [[], [], [], [], [], [], [], [], [], []]
blankDelete(dataset, k)
p_dataset = []
initial_dis = []
iteration = 0
x = [[]]
y = [[]]
execution_time = 0

#################################### Initial Centroid ######################################
# Calculate the mean point
mean_x = sum([point[0] for point in input_data]) / len(input_data)
mean_y = sum([point[1] for point in input_data]) / len(input_data)
mean_point = [mean_x, mean_y]
print (mean_point)

# Calculate the distances from each data point to the mean point
DM = [cal_distance(point, mean_point) for point in input_data]

# Select the point with the maximum distance as the first centroid
max_value_index = max(range(len(DM)), key=DM.__getitem__)
centroid.append(input_data[max_value_index])
centroid1 = input_data[max_value_index]
DM[max_value_index] = 0

# Select the remaining centroids
for _ in range(1, k):
    for i, point in enumerate(input_data):
        distance = cal_distance(point, centroid1)
        if DM[i] != 0:
                DM[i] = distance
    max_value_index = max(range(len(DM)), key=DM.__getitem__)
    centroid.append(input_data[max_value_index])
    new_cen=input_data[max_value_index]
    centroid1 = new_cen
    DM[max_value_index] = 0

print("Initial Centroids:", centroid)
centroid_x = []
centroid_y = []
# for centroid_point in centroid:
#     centroid_x.append(centroid_point[0])
#     centroid_y.append(centroid_point[1])
#     plt.scatter(centroid_point[0], centroid_point[1], color='green', marker='*')
#     plt.text(centroid_point[0], centroid_point[1], f'({centroid_point[0]}, {centroid_point[1]})', ha='center', va='bottom')

#################################### Initial Centroid ######################################
start = time.time()
while p_dataset != dataset:
    copyData(dataset)
    dataset = [[], [], [], [], [], [], [], [], [], []]

    cls_index = 0
    data = []
    for i in range(0, len(input_data)):
        prev_dis = math.inf
        for j in range(0, k):
            dis = cal_distance(input_data[i], centroid[j])
            if prev_dis > dis:
                data = input_data[i]
                cls_index = j
                prev_dis = dis
        dataset[cls_index].append(data)

    blankDelete(dataset, k)
    centroid.clear()
    centroid = [[], [], [], [], [], [], [], [], [], []]
    blankDelete(centroid, k)
    cal_centroid(centroid, k)
    iteration = iteration + 1

end = time.time()
execution_time = end - start


wcss = 0
for i in range(0, len(dataset)):
    temp = dataset[i]
    dis = 0
    for j in range(0, len(temp)):
        dis += cal_distance(temp[j], centroid[i])
    wcss += dis
print("WCSS =", wcss)
print("Iterations =", iteration)
execution_time = execution_time * 1000
print("Total time =", execution_time)

########################################### BCSS #######################################
#print("Final centroids are:",centroid)
tmp=[]
total_sumsquares=0
for m in range(len(centroid)):
    tmp.append(centroid[m])
for n in range(len(tmp)):
    for p in range(n+1,len(tmp)):
        cluster_sumsquares = cal_distance(tmp[n],tmp[p])
        total_sumsquares += cluster_sumsquares
print("BCSS",total_sumsquares)
bcss=total_sumsquares
v=(wcss/bcss)*100
print("varience of cluster",v)
    #cluster_sumsquares = np.sum((cluster_points - cluster_center) ** 2)
    #total_sumsquares += cluster_sumsquares



########################################### BCSS #######################################
i = 1
with open('kmeans_output_max.txt', 'w') as f:
    f.write("\nLength =")
    f.write(f"{len(input_data)}\n")
    for line in centroid:
        f.write("Centroid of cluster ")
        f.write(f"{i}\n")
        i += 1
        f.write(f"{line}\n")
    f.write("\nK = ")
    f.write(f"{k}\n")
    f.write("\nTotal time = ")
    f.write(f"{execution_time}\n")
    f.write("\nTotal iteration = ")
    f.write(f"{iteration}\n")
    f.write("\nWCSS =")
    f.write(f"{wcss}\n")
    f.write("\nBCSS =")
    f.write(f"{bcss}\n")
    f.write("\nVariance =")
    f.write(f"{v}\n")
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
    plt.scatter(x, y)
    x.clear()
    y.clear()

# centroid_x = []
# centroid_y = []
# for centroid_point in centroid:
#     centroid_x.append(centroid_point[0])
#     centroid_y.append(centroid_point[1])
#     plt.scatter(centroid_point[0], centroid_point[1], color='red', marker='x')
#     plt.text(centroid_point[0], centroid_point[1], f'({centroid_point[0]}, {centroid_point[1]})', ha='center', va='bottom')

plt.title("K-means Clustering (max)")
plt.xlabel('x -->')
plt.ylabel('y -->')
plt.show()
