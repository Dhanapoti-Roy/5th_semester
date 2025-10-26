import numpy as np

# Each row = one house [Size, Bedrooms, Age]
X = np.array([
    [1500, 3, 20],
    [2500, 4, 15],
    [1200, 2, 40],
    [3200, 5, 8],
    [2100, 3, 30],
    [1800, 3, 25],
    [2800, 4, 10],
    [3500, 5, 5],
    [1600, 2, 35],
    [3000, 4, 12]
])
X_min = X.min(axis=0)   # column-wise minimum
X_max = X.max(axis=0)   # column-wise maximum

X_norm = (X - X_min) / (X_max - X_min)
print("Original Data:\n", X[:5])      # first 5 rows
print("\nNormalized Data:\n", X_norm[:5])
