import random
import getData_Csv

def euclidean_distance(point1, point2):
    squared_distance = 0
    for i in range(len(point1)):
        squared_distance += (point1[i] - point2[i]) ** 2
    return squared_distance ** 0.5

def get_variance(clusters,centroids):
    wcss = 0
    for i in range(0, len(clusters)):
        temp = clusters[i]
        dis = 0
        for j in range(0, len(temp)):
            dis += euclidean_distance(temp[j], centroids[i])
        wcss += dis
    print("wcss=", wcss)
    bcss = 0
    for i in range(0, len(centroids)):
        dis = 0
        for j in range(i + 1, len(centroids)):
            dis += euclidean_distance(centroids[j], centroids[i])
        bcss += dis
    print("bcss=", bcss)
    wcss=int(wcss)
    bcss=round(bcss)
    variance = (wcss / bcss) * 100
    print("variance=", variance)
# Function to calculate the Euclidean distance between two points


# Function to assign each point to the nearest centroid
def assign_clusters(data, centroids):
    clusters = [[] for _ in range(len(centroids))]

    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        nearest_centroid_index = distances.index(min(distances))
        clusters[nearest_centroid_index].append(point)

    return clusters

# Function to update the centroids based on the assigned clusters
def update_centroids(clusters):
    centroids = []

    for cluster in clusters:
        if cluster:
            centroid = [sum(coordinates) / len(cluster) for coordinates in zip(*cluster)]
            centroids.append(centroid)

    return centroids
def cal_initialCentroid(data,k):
    uniqueData = set(tuple(x) for x in data)
    uniqueData = [list(x) for x in uniqueData]
    dis_matrix = []
    centroid=[]
    c_dis = []
    tx = 0
    ty = 0
    center = []
    for i in range(0, len(input_data)):
        p = input_data[i]
        tx += p[0]
        ty += p[1]
    tx = int(tx / len(input_data))
    ty = int(ty / len(input_data))
    center.append(tx)
    center.append(ty)
    print("center=", center)
    for j in range(0, len(uniqueData)):
        Dis = euclidean_distance(uniqueData[j], center)
        dis_matrix.append(Dis)
    max_dis = max(dis_matrix)
    min_dis = min(dis_matrix)

    for i in range(0, len(dis_matrix)):
        if min_dis == 0:
            min_value_index = dis_matrix.index(min(dis_matrix))
            dis_matrix[min_value_index] = max_dis
            min_dis = min(dis_matrix)
        else:
            break

    min_dis = min(dis_matrix)
    min_value_index = dis_matrix.index(min(dis_matrix))
    centroid.append(uniqueData[min_value_index])
    print("Cen1=", centroid)
    c_dis.append(dis_matrix[min_value_index])
    dis_matrix[min_value_index] += max_dis
    p_min = min_dis
    l = 1
    while (l != k):
        min_dis = min(dis_matrix)
        min_value_index = dis_matrix.index(min(dis_matrix))
        dis_matrix[min_value_index] += max_dis
        # while(min_dis == p_min):
        #     p_min = min_dis
        #     min_dis = min(dis_matrix)
        #     min_value_index = dis_matrix.index(min(dis_matrix))
        #     dis_matrix[min_value_index] += max_dis
        flag = 1
        for j in range(0, len(centroid)):
            dis = euclidean_distance(uniqueData[min_value_index], centroid[j])
            mdis = euclidean_distance(center, centroid[j])
            if dis <= mdis:
                flag = 0
                break
        if (flag == 1):
            centroid.append(uniqueData[min_value_index])
            l = l + 1
    print("centroid", centroid)
    return centroid


# Function to perform K-means clustering
def kmeans(data, k, max_iterations=100000000):
    # Randomly initialize centroids
    centroids = cal_initialCentroid(data, k)

    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)

        # Check for convergence
        if new_centroids == centroids:
            break

        centroids = new_centroids

    return clusters, centroids

# Example usage
input_data = getData_Csv.input_data

k=int(input("Enter the K="))
clusters, centroids = kmeans(input_data, k)
get_variance(clusters,centroids);
# Print the resulting clusters and centroids
#print("Clusters:")
# for i, cluster in enumerate(clusters):
#     print(f"Cluster {i+1}: {cluster}")
#
# print("\nCentroids:")
# for i, centroid in enumerate(centroids):
#     print(f"Centroid {i+1}: {centroid}")
