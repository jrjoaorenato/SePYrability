import numpy as np

class Distance:
    @staticmethod
    def euclidian(ref, X):
        dist = X - ref
        dist = np.sqrt(np.sum(np.power(dist, 2), axis = 1))
        dist = dist/np.max(dist)
        return dist
