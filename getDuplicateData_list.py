# Python program to print
# duplicates from a list
# of integers
# def Repeat(x):
#     _size = len(x)
#     repeated = []
#     for i in range(_size):
#         k = i + 1
#         for j in range(k, _size):
#             if x[i] == x[j] and x[i] not in repeated:
#                 repeated.append(x[i])
#     return repeated
#
#
# # Driver Code
# f = open('data.txt', 'r')
# lines = f.read().splitlines()
# f.close()
#
# input_data = []
#
# for i in range(0, len(lines)):
#     line = lines[i].split(',')
#     itemFeatures = []
#
#     for j in range(0,len(line)):
#         #v =line[j];
#         v = int(line[j])
#
#         # Add feature value to dict
#         itemFeatures.append(v)
#
#     input_data.append(itemFeatures)
# print (Repeat(input_data))
# print("input data=",input_data)
# This code is contributed
# by Sandeep_anand
from pandas import *
data = read_csv("dataset2\test data\train.csv (1)\train.csv")
my_list = [[1, 3], [4, 6], [1, 3],[3,1], [7, 9], [4, 6]]

# Using a set to keep track of unique lists
unique_list = []
seen = set()

for sublist in my_list:
    # Convert each sublist to a tuple since lists are unhashable
    sublist_tuple = tuple(sublist)

    if sublist_tuple not in seen:
        # Add the sublist to the unique_list
        unique_list.append(list(sublist_tuple))

        # Add the sublist_tuple to the set of seen tuples
        seen.add(sublist_tuple)

print(unique_list)
