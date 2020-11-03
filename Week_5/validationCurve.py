import numpy as np

from trainLinearReg import trainLinearReg
from linearRegCostFunction import linearRegCostFunction

def validationCurve(X, y, Xval, yval):
    """returns the train
    and validation errors (in error_train, error_val)
    for different values of lambda. You are given the training set (X,
    y) and validation set (Xval, yval).
    """

# Selected values of lambda (you should not change this)
    lambda_vec = np.array([0, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1, 3, 10])

# You need to return these variables correctly.
    error_train = np.zeros(lambda_vec.size)
    error_val = np.zeros(lambda_vec.size)

    for i in range(lambda_vec.size):
        Lambda = lambda_vec[i]
        theta = trainLinearReg(X, y, Lambda)
        error_train[i] = linearRegCostFunction(X, y, theta, Lambda)[0]
        error_val[i] = linearRegCostFunction(Xval, yval, theta, Lambda)[0]
    
    return lambda_vec, error_train, error_val