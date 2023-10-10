import matplotlib.pyplot as plt
from pandas import *

standard_kmeans_variance= []
minimize_kmeans_variance= []
maximize_kmeans_variance= []
data = read_csv("report1.csv")
c1 = data['Standard Kmeans'].tolist()
c2 = data['Kmeans_min'].tolist()
c3 = data['Kmeans_max'].tolist()
for i in range(0, 9):
    standard_kmeans_variance.append(c1[i])
    minimize_kmeans_variance.append(c2[i])
    maximize_kmeans_variance.append(c3[i])

cluster = [2,3,4,5,6,7,8,9,10]
print(standard_kmeans_variance)
plt.scatter(cluster,standard_kmeans_variance)
plt.plot(cluster,standard_kmeans_variance,color = 'r')

plt.title("TIME VS K")
plt.xlabel('Cluster No-->')
plt.ylabel('Execution Time -->')

plt.scatter(cluster,minimize_kmeans_variance)
plt.plot(cluster,minimize_kmeans_variance, color = 'b')

plt.scatter(cluster,maximize_kmeans_variance)
plt.plot(cluster,maximize_kmeans_variance, color = 'g')
plt.show()