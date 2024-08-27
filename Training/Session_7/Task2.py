import numpy as np
import pandas as pd

df = pd.read_csv('Session_7\\Breast_cancer_data.csv')

data = df[['mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area', 'mean_smoothness']].to_numpy()

query_point = np.array([20.57, 17.77, 132.9, 1326.0, 0.08474])

k = 3

# Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt(np.sum(np.square(a - b)))

euclidean_distances = np.array([euclidean_distance(point, query_point) for point in data])
sorted_euclidean_indices = np.argsort(euclidean_distances)[:k]

print("Nearest points using Euclidean norm:")
for idx in sorted_euclidean_indices:
    print(data[idx])
print("Euclidean distances:", euclidean_distances[sorted_euclidean_indices])

# Manhattan distance
def manhattan_distance(a, b):
    return np.sum(np.abs(a - b))

manhattan_distances = np.array([manhattan_distance(point, query_point) for point in data])
sorted_manhattan_indices = np.argsort(manhattan_distances)[:k]

print("\nNearest points using Manhattan norm:")
for idx in sorted_manhattan_indices:
    print(data[idx])
print("Manhattan distances:", manhattan_distances[sorted_manhattan_indices])

# Chebyshev distance
def chebyshev_distance(a, b):
    return np.max(np.abs(a - b))

chebyshev_distances = np.array([chebyshev_distance(point, query_point) for point in data])
sorted_chebyshev_indices = np.argsort(chebyshev_distances)[:k]

print("\nNearest points using Chebyshev norm:")
for idx in sorted_chebyshev_indices:
    print(data[idx])
print("Chebyshev distances:", chebyshev_distances[sorted_chebyshev_indices])
