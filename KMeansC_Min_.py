import matplotlib.pyplot as plt
import math
import random
import time
import functools
from pandas import *
import getData_Csv

def cal_distance(p1, p2):
    if(not p1) or (not p2):
        distance = 0
    else:
        distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

    return (distance)

def cal_ccpi(c1:list, c2:list):
    div = k*2
    sum=0.0
    for s in range(k):
        for j in range(2):
            #print(s,j, c1, c2)
            sum+=abs((c1[s][j]-c2[s][j])/(c1[s][j] if c1[s][j] != 0 else 1e-10))
    return (sum/div)
# def cal_ccpi(c1, c2):
#     sum=0.0
#     for i in range(0, len(dataset)):
#         temp = dataset[i]
#         for j in range(0, len(temp)):
#             dis_mat = []
#             for l in range(0, len(c1)):
#                 dis_mat.append(cal_distance(c1[i],temp[j]))
#             dis1=min(dis_mat)
#             dis2=cal_distance(temp[j],c2[i])
#             sum+=abs(((dis2-dis1)/dis2) if dis2 != 0 else 1e-10)
#     return (sum/(k*2))
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

# res = np.unique(np.array([np.sort(sub) for sub in input_data]), axis=0)
# input_data=res.tolist()
#input_data = [[4,21],[5,19],[20,24],[15,22],[11,17],[18,20],[19,14],[8,7],[10,12],[15,18],[12,15],[14,16],[15,12],[1,4],[1,5],[2,8],[3,9],[6,14],[3,18],[5,10],[6,18],[5,18],[4,20],[8,25],[15,17],[10,10],[11,11],[12,11],[13,11],[15,10],[16,11]]

uniqueData = set(tuple(x) for x in input_data)
uniqueData = [list(x) for x in uniqueData]

k=int(input("Enter the value of K = "))
print("Length =",len(input_data))
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


dis_matrix=[]
c_dis=[]
tx=0
ty=0
center=[]
for i in range(0, len(uniqueData)):
    p=input_data[i]
    tx += p[0]
    ty +=p[1]
tx=int(tx/len(uniqueData))
ty=int(ty/len(uniqueData))
center.append(tx)
center.append(ty)
print("Center =",center)
for j in range(0, len(uniqueData)):
    Dis = cal_distance(uniqueData[j], center)
    dis_matrix.append(Dis)
max_dis=max(dis_matrix)
min_dis=min(dis_matrix)

for i in range(0,len(dis_matrix)):
    if min_dis == 0:
        min_value_index = dis_matrix.index(min(dis_matrix))
        dis_matrix[min_value_index] = max_dis
        min_dis = min(dis_matrix)
    else:
        break

min_dis=min(dis_matrix)
min_value_index = dis_matrix.index(min(dis_matrix))
centroid.append(uniqueData[min_value_index])
print("Center 1 =",centroid)
c_dis.append(dis_matrix[min_value_index])
dis_matrix[min_value_index] += max_dis
p_min=min_dis
l=1
while(l!=k):
    min_dis = min(dis_matrix)
    min_value_index = dis_matrix.index(min(dis_matrix))
    dis_matrix[min_value_index] += max_dis
    # while(min_dis == p_min):
    #     p_min = min_dis
    #     min_dis = min(dis_matrix)
    #     min_value_index = dis_matrix.index(min(dis_matrix))
    #     dis_matrix[min_value_index] += max_dis
    flag=1
    for j in range(0, len(int_centroid)):
        dis=cal_distance(uniqueData[min_value_index],centroid[j])
        mdis=cal_distance(center,centroid[j])
        if dis <= mdis:
            flag=0
            break
    if (flag == 1):
        centroid.append(uniqueData[min_value_index])
        l=l+1
print("Centroids generated using min Algorithm =",centroid)

centroid_1 = centroid.copy()

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
end = time.time()
execution_time = end - start

centroid_f = centroid

ccpi=cal_ccpi(centroid_1, centroid_f)
print("CCPI =",ccpi)

#print("dataset=",dataset)
#print("total iteration=",loop_count)
wcss=0
for i in range(0, len(dataset)):
    temp = dataset[i]
    dis = 0
    for j in range(0, len(temp)):
        dis += int(cal_distance(temp[j], centroid[i]))
    wcss += dis
print("WCSS =",wcss)
bcss=0
for i in range(0, len(centroid)):
    dis = 0
    for j in range(i+1, len(centroid)):
        dis += cal_distance(centroid[j], centroid[i])
    bcss += dis
print("BCSS =",bcss)
wcss=int(wcss)
# bcss=round(bcss)
variance=(wcss/bcss)*100
print("Variance =",variance)

print("Iterations =",iteration)
execution_time = execution_time *1000
print("Total Time =",execution_time)
i=1
with open('kmeansC_output_min2.txt', 'w') as f:
    f.write("\nLength =")
    f.write(f"{len(input_data)}\n")
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
    f.write("\nWCSS =")
    f.write(f"{wcss}\n")
    f.write("\nBCSS =")
    f.write(f"{bcss}\n")
    f.write("\nVariance =")
    f.write(f"{variance}\n")
    f.write("\nCCPI =")
    f.write(f"{ccpi}\n")
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
# centroid_x = []
# centroid_y = []
# for centroid_point in centroid:
#     centroid_x.append(centroid_point[0])
#     centroid_y.append(centroid_point[1])
#     plt.scatter(centroid_point[0], centroid_point[1], color='red', marker='x')
#     plt.text(centroid_point[0], centroid_point[1], f'({centroid_point[0]}, {centroid_point[1]})', ha='center', va='bottom')

plt.title("Standard K-means Clustering(min)")
# plt.title("Data Set")
plt.xlabel('x -->')
plt.ylabel('y -->')
plt.show()


# [[341.0916, 341.3147], [341.3147, 341.0916], [343.3702, 342.008]]
