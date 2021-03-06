import numpy as np

def polyFeatures(X, p):
    """takes a data matrix X (size m x 1) and
    maps each example into its polynomial features where
    X_poly[:,i-1] = [X[:,0] X[:,0]**2 X[:,0]**3 ...  X[:,0]**p]
    """
    # You need to return the following variables correctly.
    X_poly = np.zeros((X.shape[0], p))

    for i in range(1,p+1):
        X_poly[:,i-1] = X[:,0]**i    
    return X_poly
