import numpy as np

def euclidian(ref, X):
    dist = X - ref
    dist = np.sqrt(np.sum(np.power(dist, 2), axis = 1))
    dist = dist/np.max(dist)
    return dist

