from pandas import *
import csv

input_data=[]
data = read_csv("data1L.csv")
c1 = data['A1'].tolist()
c2 = data['A2'].tolist()
for i in range(0, len(c1)):
    input_data.append([])
    input_data[i].append(c2[i])
    input_data[i].append(c1[i])
# j = len(c1)
# # data = read_csv("UCI_dataSet\gas-sensor-array-temperature-modulation/20161013_143355.csv")
# c1 = data['R5 (MOhm)'].tolist()
# c2 = data['Time (s)'].tolist()
# for i in range(0, len(c1)):
#     input_data.append([])
#     input_data[j].append(c2[i])
#     input_data[j].append(c1[i])
#     j = j + 1
# def get_first_row_as_list(file_path):
#     with open(file_path, 'r') as file:
#         csv_reader = csv.reader(file)
#         first_row = next(csv_reader)
#         return first_row
# file_path = 'dataset2/archive\Filtering_pyComBat.csv'
# first_row_list = get_first_row_as_list(file_path)
#
# # print(len(first_row_list))
# # print(first_row_list)
# data = read_csv(file_path)
# j=0
# l=1
# while(l<=4180):
#     if(first_row_list[l]!=' ' and first_row_list[l+1]!=' '):
#         c1 = data[first_row_list[l]].tolist()
#         c2 = data[first_row_list[l+1]].tolist()
#         for i in range(0, len(c1)):
#             input_data.append([])
#             input_data[j].append(c2[i])
#             input_data[j].append(c1[i])
#             j=j+1
#         l=l+1
#     l=l+1
# print(input_data)