from numpy import *
import math
import numpy as np


class FpenFunction(object):

    def __init__(self, dim,x_vector):
        self.x_vector = x_vector
        self.dim = dim

    def fpen_function(self):

        #fpen = np.ones((self.dim), dtype=np.float64)
        fpen = 0
        for i in range(self.dim):
            #fpen = fpen + np.amax(math.pow(abs(self.x_vector[i])-5,2))
            fpen = math.pow(np.amax(math.fabs(self.x_vector[i])-5),2)

        return fpen



