# A simple Python3 program to find
# maximum score that
# maximizing player can get
import math
from pandas import *

def minimax(curDepth, nodeIndex,maxTurn, scores,targetDepth):

    if (curDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,False, scores, targetDepth),minimax(curDepth + 1, nodeIndex * 2 + 1,False, scores, targetDepth))

    else:
        return min(minimax(curDepth + 1, nodeIndex * 2,True, scores, targetDepth),minimax(curDepth + 1, nodeIndex * 2 + 1,True, scores, targetDepth))


# Driver code
# scores = [3, 5, 2, 9, 12, 5, 23, 23]
scores=[]
data = read_csv("bank.csv")
c1 = data['age'].tolist()
for i in range(0, 1023):
    scores.append(c1[i])
print(scores)
treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end="")
r=minimax(0, 0, True, scores, treeDepth)
print(r)

# This code is contributed
# by rootshadow
