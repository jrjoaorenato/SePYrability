import numpy as np

def separability(data, labels, dist, dx = 0.01):
    '''
    Separability function will calculate the separability metric 
    of the given data and labels.

    Returns a dictionary containing the distance intervals aswell
    as the multiscale separability of each interval.

    Parameters:
        data (np.array): The data on which separability is to be
        calculated
        labels (np.array): label information for each piece of data
        dx (float): step of each interval
        dist (function): distance function on which separability is 
        going to be evaluated
    '''

    #inicialmente encontramos um ponto de referência para cada classe
    

    return