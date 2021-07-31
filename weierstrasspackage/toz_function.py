from numpy import *
import math
import numpy as np
from weierstrasspackage.diagonal_matrix import DiagonalMatrix

class ToszFunction(object):

    def __init__(self,R,Q,x_vector,dim,seedR,seedQ):
        self.R = R
        self.Q = Q
        self.x_vector = x_vector
        self.dim = dim
        self.seedR = seedR
        self.seedQ = seedQ


    def x_column(self):
        return self.R.dot(self.x_vector)

    def sign_function(self):

        x_column = self.x_column()
        sign_ = np.sign(x_column)
        return sign_

    def x_hat_function(self):
        #global x_hat
        x_column = self.x_column()
        x_hat = 0
        x_hat=np.ones((self.dim),dtype=np.float64)
        for i in range(1,self.dim-1):
            x_hat[i] = x_column[i]
            if(x_column[i] !=0):
                x_hat[i] = math.log((abs(x_column[i])))
            else:
                x_hat[i] = 0
        return x_hat

    def c1_value_function(self):
        x_column = self.R.dot(self.x_vector)
        c1_value = np.ones((self.dim),dtype=np.float64)
        c1_value  = 0
        for i in range(1,self.dim-1):
            c1_value[i] = x_column[i]
            if(x_column[i] > 0):
                c1_value[i] = 10
            else:
                c1_value[i] = 5.5
        return c1_value

    def c2_value_function(self):
        x_column = self.R.dot(self.x_vector)
        c2_value = np.ones((self.dim), dtype=np.float64)
        for i in range(self.dim):
            c2_value[i] = x_column[i]
            if (x_column[i] > 0):
                c2_value[i] = 7.9
            else:
                c2_value[i] = 3.1
        return c2_value

    def tosz_function(self):

        sign = self.sign_function()
        hat = self.x_hat_function()
        c1 = self.c1_value_function()
        c2 = self.c2_value_function()
        x_col = np.ones((self.dim), dtype=np.float64)
        for i in range(1,self.dim-1):
            x_col[i] = sign[i] * (math.exp(hat[i] + 0.049 * (math.sin(c1[i] * hat[i])) + math.sin(c2[i] * hat[i])))
        return x_col

    def zi_function(self):

        diagonal = DiagonalMatrix(self.dim)
        tosz = self.tosz_function()
        diagonal_matrix = diagonal.alfa_generator()
        productQ_tosz = self.Q.dot(tosz)
        productLambda_q = diagonal_matrix.dot(productQ_tosz)
        zi = self.R.dot(productLambda_q)

        return zi

















