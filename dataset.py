import matplotlib.pyplot as plt
from pandas import *

input_data = []
data = read_csv("bank.csv")
c1 = data['age'].tolist()
c2 = data['balance'].tolist()
for i in range(0, len(c1)):
    print(i)
    #input_data.append([])
    plt.scatter(c1[i], c2[i])
    #input_data[i].append(c1[i])
    #input_data[i].append(c2[i])

print("Done")

# x=[]
# y=[]
# l1 = len(input_data)
# for i in range(0, l1):
#     temp1=input_data[i]
#     print(i)
#     x.append(temp1[0])
#     y.append(temp1[1])
#     # print("X=",x)
#     # print("Y=",y)
#     plt.scatter(x, y)
#     x.clear()
#     y.clear()
plt.show()
