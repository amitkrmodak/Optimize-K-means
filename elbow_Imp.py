import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load your data into a DataFrame (replace 'data.csv' with your file path)
data = pd.read_csv('UCI_dataSet\diabetes+130+us+hospitals+for+years+1999+2008\dataset_diabetes\diabetic_data.csv')

# Create an empty list to store the variance for each cluster
variance = []

# Set the range of clusters you want to test (e.g., from 1 to 10)
num_clusters = range(1, 10)

# Calculate variance for each cluster number
for k in num_clusters:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    variance.append(kmeans.inertia_)

# Plot the variance against the number of clusters
plt.plot(num_clusters, variance, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Variance (Within-Cluster Sum of Squares)')
plt.title('Elbow Method to Find Optimal Number of Clusters')
plt.show()
