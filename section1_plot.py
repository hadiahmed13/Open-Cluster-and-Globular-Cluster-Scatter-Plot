import pandas as pd
import matplotlib.pyplot as plt

open_clusters_df = pd.read_csv('Project 2 Data - Open Cluster Coordinates.csv')
globular_clusters_df = pd.read_csv('Project 2 Data - Globular Cluster Coordinates.csv')

# Plot for open clusters
plt.figure(figsize=(10, 5))
plt.scatter(open_clusters_df['Galactic Longitude (deg)'], open_clusters_df['Galactic Latitude (deg)'], color='blue', label='Open Clusters')
plt.title('Galactic Longitude vs. Latitude for Open Clusters')
plt.xlabel('Galactic Longitude (deg)')
plt.ylabel('Galactic Latitude (deg)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Plot for globular clusters
plt.figure(figsize=(10, 5))
plt.scatter(globular_clusters_df['Galactic Longitude (deg)'], globular_clusters_df['Galactic Latitude (deg)'], color='orange', label='Globular Clusters')
plt.title('Galactic Longitude vs. Latitude for Globular Clusters')
plt.xlabel('Galactic Longitude (deg)')
plt.ylabel('Galactic Latitude (deg)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# To calculate average distances:
avg_distance_open = open_clusters_df['Distance (ly)'].mean()
avg_distance_globular = globular_clusters_df['Distance (ly)'].mean()

print(f"Average distance to open clusters: {avg_distance_open} lightyears")
print(f"Average distance to globular clusters: {avg_distance_globular} lightyears")
