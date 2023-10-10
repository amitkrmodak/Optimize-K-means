from pandas import *
import csv
input_data=[]

j=0
# data = read_csv("amzn-anon-access-samples/amzn-anon-access-samples-history-2.0.csv")
############### diabetic_data.csv start ##################
# data = read_csv("UCI_dataSet\diabetes+130+us+hospitals+for+years+1999+2008\dataset_diabetes\diabetic_data.csv")
# c1 = data['encounter_id'].tolist()
# c2 = data['patient_nbr'].tolist()
# # c1 = data['num_lab_procedures'].tolist()
# # c2 = data['num_medications'].tolist()
# for i in range(0, len(c1)):
#     input_data.append([])
#     input_data[i].append(c1[i])
#     input_data[i].append(c2[i])
################ diabetic_data.csv end ##################

################ bank start #######################
# data = read_csv("bank.csv")
# c1 = data['age'].tolist()
# c2 = data['balance'].tolist()
# for i in range(0, len(c1)):
#     input_data.append([])
#     input_data[j].append(c1[i])
#     input_data[j].append(c2[i])
#     j+=1

################# bank end #####################

############### hypothyroid.csv start ##################
data = read_csv("hypothyroid.csv")
c1 = data['age'].tolist()
c2 = data['TT4'].tolist()
for i in range(0, len(c1)):
    input_data.append([])
    input_data[j].append(c1[i])
    input_data[j].append(c2[i])
    j=j+1
################ hypothyroid.csv end ##################

################ bank.csv start ##################
# data = read_csv("bank.csv")
# c1 = data['age'].tolist()
# c2 = data['balance'].tolist()
# for i in range(0, len(c1)):
#     input_data.append([])
#     input_data[i].append(c1[i])
#     input_data[i].append(c2[i])
################ bank.csv end ##################


# def get_first_row_as_list(file_path):
#     with open(file_path, 'r') as file:
#         csv_reader = csv.reader(file)
#         first_row = next(csv_reader)
#         return first_row
# # file_path = 'beginner_datasets\gold.csv'
# # file_path = 'dataset2/archive\Multi_group_batch.csv'
# file_path = 'UCI_dataSet\gas-sensor-array-temperature-modulation/20161004_104124.csv'
# first_row_list = get_first_row_as_list(file_path)
# data = read_csv(file_path)
# j=0
# l=6
# while(l<20):
#     if(first_row_list[l]!=' ' and first_row_list[l+1]!=' '):
#         c1 = data[first_row_list[l]].tolist()
#         c2 = data[first_row_list[l+1]].tolist()
#         for i in range(0, len(c1)):
#             if isinstance(c1[i], float) and isinstance(c2[i], float):
#                 input_data.append([])
#                 input_data[j].append(c2[i])
#                 input_data[j].append(c1[i])
#                 j=j+1
#                 input_data.append([])
#                 input_data[j].append(c1[i])
#                 input_data[j].append(c2[i])
#                 j=j+1
#         l=l+1
#     l=l+1
print(len(input_data))