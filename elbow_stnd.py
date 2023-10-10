import matplotlib.pyplot as plt
import math;
import random;
import numpy;
from pandas import *
import getData_Csv

input_data = getData_Csv.input_data
# data = read_csv("bank.csv")
# c1 = data['age'].tolist()
# c2 = data['balance'].tolist()
# data = read_csv("beginner_datasets\satellite.csv")
# c1 = data['Attribute10'].tolist()
# c2 = data['Attribute11'].tolist()
# for i in range(0, len(c1)):
#     input_data.append([])
#     input_data[i].append(c1[i])
#     input_data[i].append(c2[i])

#input_data = [[4,21],[5,19],[20,24],[15,22],[11,17],[18,20],[19,14],[8,7],[10,12],[15,18],[12,15],[14,16],[15,12],[1,4],[1,5],[2,8],[3,9],[6,14],[3,18],[5,10],[6,18],[5,18],[4,20],[8,25],[15,17],[10,10],[11,11],[12,11],[13,11],[15,10],[16,11]]
def getOptimal_k(t):
    for i in range(0, 10):
        if t[i]-t[i+1] <=100000000000000000000000:
            return i+1

def cal_kmeans(k):
    print("K=",k)
    cls_index = 0
    #print("Input Data=", input_data)
    #print("Length of input data=", len(input_data))
    #print(type(input_data[0]))
    # len=len(input_data)
    centroid = []
    dataset = [[], [], [], [], [], [], [], [], [], []]

    def cal_distance(p1, p2):
        # print("p1=",p1)
        # print("p2=",p2)
        if ((not p1) or (not p2)):
            distance = 0
        else:
            distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

        return (round(distance))

    def copyData(x):
        l = len(x)
        p_dataset.clear()
        for i in range(0, l):
            p_dataset.append(x[i])

    # def cal_centroid(centroid, k):
    #     print("dataset=", dataset)
    #     print("centroid=", centroid)
    #     l = []
    #     for i in range(0, k):
    #         # print("centroid dataset=",dataset[i])
    #         x = 0
    #         y = 0
    #         temp = dataset[i]
    #         print("temp=", temp)
    #         if not temp:
    #             print("list is  empty")
    #             centroid.append([])
    #         else:
    #             ln = len(temp)
    #             l.clear()
    #             for j in range(0, ln):
    #                 temp1 = temp[j]
    #                 print("temp1=",temp1)
    #                 x += temp1[0]
    #                 y += temp1[1]
    #             x = int(x/ln)
    #             y = int(y/ln)
    #             l.append(x)
    #             l.append(y)
    #             print("l=",l)
    #             centroid[i].append(x)
    #             centroid[i].append(y)
    #             # rand_data = random.choice(temp)
    #             # centroid.append(rand_data)
    #
    #     print("centroid=", centroid)
    def cal_centroid(centroid, k):
        #print("dataset (cal_centroid=", dataset)
        #print("dataset length=", len(dataset))
        #print("k=", k)
        #print("centroid=", centroid)
        for i in range(0, k):
            # print("centroid dataset=",dataset[i])
            temp = dataset[i]
            #print("temp=", temp)
            if not temp:
                print("list is  empty")
                centroid.append([])
            else:
                ln = len(temp)
                tx = 0
                ty = 0
                for j in range(0, ln):
                    temp1 = temp[j]
                    #print("temp1=", temp1)
                    tx = tx + temp1[0]
                    ty = ty + temp1[1]
                tx = round(tx / ln)
                ty = round(ty / ln)
                centroid[i].append(tx)
                centroid[i].append(ty)

    def blankDelete(data, k):
        l = 10 - k
        for i in range(0, l):
            data.pop()

    blankDelete(dataset, k)
    p_dataset = []
    loop_count = 0
    x = [[]]
    y = [[]]

    # a = round(len(input_data) / k)
    # ind = 0
    # for i in range(0, k):
    #     centroid.append(input_data[ind])
    #     ind += a
    # print("centroid=", centroid)

    for i in range(0, k):
        centroid.append(random.choice(input_data))
    #print("centroid=", centroid)

    while p_dataset != dataset:
        # print("Compare=",p_dataset != dataset)
        copyData(dataset)
        dataset = [[], [], [], [], [], [], [], [], [], []]

        # print("dataset=", dataset)
        # print("P_dataset=", p_dataset)
        for i in range(0, len(input_data)):
            prev_dis = 10000000000000000000000
            for j in range(0, k):
                # print("input data=",input_data[i])
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
        # for i in range(0, k):
        #     temp=dataset[i]
        #     centroid.append(random.choice(temp))
        # print("centroid=",centroid)
        # print("Compare=", p_dataset != dataset)
        loop_count += 1
        # print("loop_count=",loop_count)
        #print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    #print("dataset=", dataset)
    #print("total iteration=", loop_count)
    wcss = 0
    for i in range(0, len(dataset)):
        temp = dataset[i]
        dis = 0
        for j in range(0, len(temp)):
            dis += cal_distance(temp[j], centroid[i])
        wcss += dis * dis
    #print("wcss=", wcss)
    return(wcss)



wcss_list = [[],[],[],[],[],[],[],[],[],[]]
temp = [[],[],[],[],[],[],[],[],[],[]]
ch=1
for i in range(0, 10):
    #ch = int(input("Enter choice="))
    if ch==1:
        wcss_list[i] = cal_kmeans(i+1)
        temp[i]=round(wcss_list[i]/10000000000)
        #print("temp wcss list=", wcss_list)
print("wcss list=",wcss_list)
print("temp list=",temp)
print("Optimal k=",getOptimal_k(temp))

with open('elbow_output.txt', 'w') as f:
    f.write("WCSS= ")
    for line in temp:
        #f.write("WCSS= ")
        i += 1

        f.write(f"{line}, ")
    f.write("\nOptimal K =")
    f.write(f"{getOptimal_k(temp)}\n")


cluster = [1,2,3,4,5,6,7,8,9,10]
plt.scatter(cluster,temp,color = 'r')
#plt.plot(cluster,wcss_list)
plt.plot(cluster,temp)
plt.title("Elbow of Standard K-means")
plt.xlabel('Cluster No-->')
plt.ylabel('WCSS -->')
plt.show()