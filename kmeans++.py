import random
import math
import matplotlib.pyplot as plt
import getData_Csv
# Euclidean distance calculation
def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def cal_distance(p1, p2):
    if(not p1) or (not p2):
        distance = 0
    else:
        distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

    return (distance)
# Initialization using k-means++ method
def kmeans_plusplus_init(k, data):
    centroids = [random.choice(data)]

    for _ in range(1, k):
        distances = []
        for point in data:
            min_dist = min(euclidean_distance(point, centroid) for centroid in centroids)
            distances.append(min_dist)
        probabilities = [dist ** 2 / sum(distances) for dist in distances]
        centroid = random.choices(data, probabilities)[0]
        centroids.append(centroid)

    return centroids

# K-means clustering
def kmeans_clustering(k, data, max_iterations=100):
    centroids = kmeans_plusplus_init(k, data)
    clusters = [[] for _ in range(k)]

    for _ in range(max_iterations):
        new_clusters = [[] for _ in range(k)]
        for point in data:
            min_dist = math.inf
            cluster_idx = None
            for i, centroid in enumerate(centroids):
                dist = euclidean_distance(point, centroid)
                if dist < min_dist:
                    min_dist = dist
                    cluster_idx = i
            new_clusters[cluster_idx].append(point)

        if clusters == new_clusters:
            break

        clusters = new_clusters

        centroids = []
        for cluster in clusters:
            centroid = [sum(coord) / len(cluster) for coord in zip(*cluster)]
            centroids.append(centroid)

    return clusters, centroids

# Generate sample data
data = getData_Csv.input_data

# Perform k-means++ clustering
k=int(input("Enter the K="))
clusters, centroids = kmeans_clustering(k, data)

# Display cluster data
# for i, cluster in enumerate(clusters):
#     print(f"Cluster {i+1}:", cluster)

wcss=0
for i in range(0, len(clusters)):
    temp = clusters[i]
    dis = 0
    for j in range(0, len(temp)):
        dis += cal_distance(temp[j], centroids[i])
    wcss += dis
print("wcss=",wcss)
bcss=0
for i in range(0, len(centroids)):
    dis = 0
    for j in range(i+1, len(centroids)):
        dis += cal_distance(centroids[j], centroids[i])
    bcss += dis
print("bcss=",bcss)
# wcss=int(wcss)
# bcss=round(bcss)
# print("wcss=",wcss)
# print("bcss=",bcss)
variance=(wcss/bcss)*100
print("variance=",variance)


# Plot the cluster data
colors = ['r', 'g', 'b', 'c', 'm', 'y']
for i, cluster in enumerate(clusters):
    for point in cluster:
        plt.scatter(point[0], point[1], color=colors[i])
plt.scatter([centroid[0] for centroid in centroids], [centroid[1] for centroid in centroids], color='black', marker='X')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-means++ Clustering')
plt.show()
