import numpy as np

def euclidian(ref, X):
    #returns normalized euclidian distance from the reference point
    dist = X - ref
    dist = np.sqrt(np.sum(np.power(dist, 2), axis = 1))
    dist = dist/np.max(dist)
    return dist

#todo: find better cosine distance metric
def cosine(ref, X):
    #returns cosine distance between the reference point and X
    aux = []
    for x in X:
        dist = 1 - np.inner(ref, x)/(np.linalg.norm(ref) * np.linalg.norm(x))
        aux.append(dist)
    return aux

