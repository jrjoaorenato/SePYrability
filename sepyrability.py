import numpy as np

def separability(data, labels, dist, dx = 0.02, start= 0.01):
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
    #inicialmente encontramos um ponto de referência para cada classe e salvamos
    #em refData
    unique = np.unique(labels)
    refData = np.empty((unique.shape[0], data.shape[1]))
    for i in unique:
        ref_ind = np.argmax(labels == i)
        refData = np.append(refData, data[ref_ind, :], axis = 0)

    #para cada referência, calculo a separabilidade por classe e armazeno
    #em sep. Cada linha de sep é uma classe~
    sep = np.empty(0, dx.shape[0])
    for i in range(0, unique.shape[0]):
        ref = refData[i]
        #todo: change to distance function
        #calculo a distancia entre ref e todos os pontos
        dist = data - ref
        dist = np.sqrt(np.sum(np.power(dist, 2), axis = 1))
        dist = dist/np.max(dist)

        aux = np.array([[]])
        for j in dx:
            nrc = (np.where(dist <= j)).shape[0]
            sd = 1 - (nrc/data.shape[0])
            aux = np.append(aux, sd)
        sep = np.vstack((sep, aux))

    multiscale_separability = {
        'multiscale_separability': np.mean(sep),
        'distance': dx
    }
    return multiscale_separability