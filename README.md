# SePYrability
Python implementation of the separability metric.

Python implementation of the Multiscale Separability metric as shown in \[1\]. The original paper from which the implementation was based of can be found [here](https://doi.org/10.1016/j.patcog.2003.10.007).

After using this package consider citing the paper from which the implementation was based of:

```
[1] TORRES, R. da S.; FALCAO, Alexandre X.; COSTA, L. da F. A graph-based approach for multiscale shape analysis. Pattern Recognition, v. 37, n. 6, p. 1163-1174, 2004.
```

# Table of Contents
* [SePYrability](#SePYrability)
* [Table of Contents](#table-of-contents)
* [Multiscale Separability](#multiscale-separability)
* [Installation](#installation)
    * [Method 1 - PIP](#method-1---pip)
    * [Method 2 - Manual Installation](#method-2---manual-installation)
* [Usage](#usage)
* [Custom Distance Function](#custom-distance-function)
* [Example](#example)

## Multiscale Separability
<!-- WIP: Better explanation of the Multiscale Separability -->
The separability of a descriptor indicates it's discriminatory capabilities among individuals of the same class. It measures the effectiveness of a descriptor by showing how far data is from that descriptor.

## Installation

### Method 1 - PIP
Just run:
```pip install sepyrability``` 

### Method 2 - Manual Installation

First, clone the directory, by running:

```git clone https://github.com/jrjoaorenato/SePYrability.git```

The package requires the following dependencies:
- numpy
- matplotlib

You can install those dependencies by running the following command in the package directory:
``` pip install -r requirements.txt ```

After that you can run the following command in the package directory to install the package:
``` pip install -e . ```

## Usage

You can import the package by using:
``` import sepyrability.separability as sep ```

The default distance metrics already implemented, can be imported by:
``` import sepyrability.distance as dis ```

The types of distance currently implemented are:

0. `euclidian` - Euclidian distance
1. `cosine` - Cosine distance

To access the distances you can use: `dis.<chosen distance>`.

After properly importing the package you can compute the multiscale separability with the following attributes:

```python
sep.calculate_separability(data, labels, distfun = dis.euclidian, dx = 0.02, start= 0.01, show_graph = True):
```

```
Arguments:
    n is the number of instances
    and f is the dimensionality of the features
    data {numpy Matrix [n x f]} -- The data on which separability is going to be calculated
    labels {np.array[n]} -- label information for each piece of data
    distfun {function} -- function used to calculate distance: euclidian
    dx {float} -- step size for distance calculation
    start {float} -- starting point for the steps
    show_graph {bool} -- Boolean to show or not the multiscale separability graph

Returns:
    multiscale_separability {dictionary} -- dictionary containing:
        - 'multiscale_separability' [array of floats] -- multiscale_separability for a specific radius
        - 'distance' [array of floats] -- corresponding radius distance for multiscale_separability
    auc -- area under the curve of the separability graph
    --plots graph if 'show_graph' is True
```
You can easily obtain the multiscale seprability data using sep.calculate_separability(data, labels). If you want, you can also specify a different distance function from euclidian, by passing the function as an argument of distfun, including your own, as shown in the next session.

## Custom Distance Function
You have the option to implement your own distance function and pass it as an argument of distfun. This can be done by creating a custom function that receives a reference point 'ref' and a data point 'X' as arguments, and returns the distance between these two points. 

NOTE: The distance should be normalized between 0 and 1.

An example can be seen below:

```python
def custom_euclidian(ref, X):
    #returns normalized euclidian distance from the reference point
    dist = X - ref
    dist = np.sqrt(np.sum(np.power(dist, 2), axis = 1))
    dist = dist/np.max(dist)
    return dist

#this can be called below by using:
ms, auc = sep.calculate_separability(Xt, Yt, distfun=dis.custom_euclidian)
```

## Example
```python
import sepyrability.separability as sep
import scipy.io as sio
import numpy as np

D = loadmat(<some .mat dataset location>)
X = D['X']
Y = D['Y']
ms, auc = sep.calculate_separability(X, Y)
```
