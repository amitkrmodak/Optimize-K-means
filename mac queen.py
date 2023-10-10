import random
import getData_Csv
# Function to calculate the Euclidean distance between two points
def euclidean_distance(point1, point2):
    squared_distance = 0
    for i in range(len(point1)):
        squared_distance += (point1[i] - point2[i]) ** 2
    return squared_distance ** 0.5

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

# Function to perform MacQueen clustering (K-means)
def macqueen(data, k, max_iterations=1000):
    # Randomly initialize centroids
    centroids = random.sample(data, k)

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

k = 3
clusters, centroids = macqueen(input_data, k)

# Print the resulting clusters and centroids
print("Clusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i+1}: {cluster}")

print("\nCentroids:")
for i, centroid in enumerate(centroids):
    print(f"Centroid {i+1}: {centroid}")
