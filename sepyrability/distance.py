import numpy as np

def euclidian(ref, X):
    #returns normalized euclidian distance from the reference point
    dist = X - ref
    dist = np.sqrt(np.sum(np.power(dist, 2), axis = 1))
    dist = dist/np.max(dist)
    return dist

def cosine(ref, X):
    dist = np.inner(ref, X)/(np.linalg.norm(ref) * np.linalg.norm(X))
    return dist

