from numpy import *
import math
import numpy as np

class FzeroFunction(object):

    def __init__(self,dim):
        self.dim = dim

    def fzero_function(self):


        for k in range(11):
            fzero = math.pow(1/2,k)*(math.cos(math.pow(2*pi*3,k))*(1/2))

        return fzero