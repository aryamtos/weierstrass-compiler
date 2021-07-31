import numpy as np
from numpy import *
import math

class DiagonalMatrix(object):
    def __init__(self,dim):
        self.dim = dim

    def alfa_generator(self):

        lambda_= np.zeros((self.dim,self.dim), dtype=np.float64)
        for i in range(self.dim):
            lambda_[i][i] = math.pow(0.01,1/2 * ((i - 1)/(self.dim - 1)))

        return lambda_
