import numpy as np

# Define the dataset
data = np.array([
    [51, 92, 14, 71, 60],
    [20, 82, 86, 74, 70],
    [10, 84, 70, 33, 61],
    [75, 98, 56, 83, 41],
    [56, 92, 48, 37, 80],
    [28, 46, 93, 54, 22],
    [62, 99, 74, 50, 20],
    [21, 84, 77, 96, 19],
    [63, 29, 71, 48, 88],
    [17, 11, 94, 22, 48],
    [93, 66, 58, 54, 10],
    [71, 96, 87, 35, 99],
    [50, 82, 12, 73, 31],
    [83, 64, 50, 72, 19],
    [96, 53, 19, 60, 90],
    [25, 68, 42, 55, 94],
    [47, 81, 99, 72, 63],
    [52, 35, 40, 91, 12],
    [64, 58, 36, 22, 78],
    [89, 46, 68, 94, 21]
])

# Define the query point
query_point = np.array([63, 45, 76, 32, 14])

# Euclidean distance
def euclidean_distance(a, b):
    return np.sqrt(np.sum(np.square(a - b)))

euclidean_distances = np.array([euclidean_distance(point, query_point) for point in data])
nearest_point_euclidean = np.argmin(euclidean_distances)

print("Nearest point using Euclidean norm:", data[nearest_point_euclidean])
print("Euclidean distance:", euclidean_distances[nearest_point_euclidean])

# Manhattan distance
def manhattan_distance(a, b):
    return np.sum(np.abs(a - b))

manhattan_distances = np.array([manhattan_distance(point, query_point) for point in data])
nearest_point_manhattan = np.argmin(manhattan_distances)

print("Nearest point using Manhattan norm:", data[nearest_point_manhattan])
print("Manhattan distance:", manhattan_distances[nearest_point_manhattan])

# Chebyshev distance
def chebyshev_distance(a, b):
    return np.max(np.abs(a - b))

chebyshev_distances = np.array([chebyshev_distance(point, query_point) for point in data])
nearest_point_chebyshev = np.argmin(chebyshev_distances)

print("Nearest point using Chebyshev norm:", data[nearest_point_chebyshev])
print("Chebyshev distance:", chebyshev_distances[nearest_point_chebyshev])
