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
    input_data = [list(x) for x in uniqueData]
    centroid=[]
    mean_x = sum([point[0] for point in input_data]) / len(input_data)
    mean_y = sum([point[1] for point in input_data]) / len(input_data)
    mean_point = [mean_x, mean_y]
    print(mean_point)

    # Calculate the distances from each data point to the mean point
    DM = [euclidean_distance(point, mean_point) for point in input_data]

    # Select the point with the maximum distance as the first centroid
    max_value_index = max(range(len(DM)), key=DM.__getitem__)
    centroid.append(input_data[max_value_index])
    centroid1 = input_data[max_value_index]
    DM[max_value_index] = 0

    # Select the remaining centroids
    for _ in range(1, k):
        for i, point in enumerate(input_data):
            distance = euclidean_distance(point, centroid1)
            if DM[i] != 0:
                DM[i] = distance
        max_value_index = max(range(len(DM)), key=DM.__getitem__)
        centroid.append(input_data[max_value_index])
        new_cen = input_data[max_value_index]
        centroid1 = new_cen
        DM[max_value_index] = 0

    print("Initial Centroids:", centroid)
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
