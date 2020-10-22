import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import sepyrability.distance as dis

def separability(data, labels, distfun = dis.euclidian, dx = 0.01, start= 0.01):
    '''
    Separability function will calculate the separability metric 
    of the given data and labels.

    Returns a dictionary containing the distance intervals as well
    as the multiscale separability of each interval.

    Parameters:
        data (np.array): The data on which separability is to be
        calculated
        labels (np.array): label information for each piece of data
        dx (float): step of each interval
        dist (function): distance function on which separability is 
        going to be evaluated
    '''
    dx = np.arange(start, 1.0, dx)
    #we start by storing a reference point for each class in refData
    unique = np.unique(labels)
    refData = np.empty((0, data.shape[1]))
    for i in unique:
        ref_ind = np.argmax(labels == i)
        refData = np.vstack((refData, data[ref_ind, :]))

    #for each referece, the separability for class is calculated and stored in sep
    #each line of sep is a different class
    sep = np.empty((0, dx.shape[0]))
    for i in range(0, unique.shape[0]):
        ref = refData[i]
        
        #the corresponding distance between ref and every point
        #is then calculated using the parameter distfun
        dist = distfun(ref, data)

        #aux then stores the proportion of the data within that respective distance
        aux = np.array([[]])
        for j in dx:
            nrc = (np.where(dist <= j)[0]).shape[0]
            #separability is then calculated
            sd = 1 - (nrc/data.shape[0])
            aux = np.append(aux, sd)
        #all the separability data for that specific class is stored in sep
        sep = np.vstack((sep, aux))

    #after that multiscale separability is calculated for each distance
    #being the mean of each separability metric
    #and returns a dictionary containing the multiscale separability and each
    #respective radius
    multiscale_separability = {
        'multiscale_separability': np.mean(sep, axis = 0),
        'distance': dx
    }
    return multiscale_separability

def calculate_separability(data, labels, distfun = dis.euclidian, dx = 0.02, start= 0.01, show_graph = True):
    #calculates separability
    sep = separability(data, labels, distfun, dx, start)
    distance = sep['distance']
    ms = sep['multiscale_separability']
    auc = 0
    #calculates auc
    for i in ms:
        auc += i*dx
    #if True, show the separability graph and return, otherwise just return separability for each distance
    #and auc
    if (show_graph):
        plt.plot(distance, ms)
        plt.xlabel('Search Radius')
        plt.ylabel('Multiscale Separability')
        plt.xlim(0.0, 1.01)
        plt.ylim(0.0, 1.01)
        plt.show()
    return sep, auc


