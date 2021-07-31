from weierstrasspackage.toz_function import ToszFunction
from weierstrasspackage.fpen_function import FpenFunction
from numpy import *


class WeierstrassFunction(object):

    def __init__(self,R,Q,x_vector,D, seed_R,seed_Q):
        self.R = R
        self.Q = Q
        self.x_vector = x_vector
        self.D = D
        self.seed_R = seed_R
        self.seed_Q = seed_Q

    @property
    def function_summation(self):
        tosz_class = ToszFunction(self.R, self.Q, self.x_vector, self.D, self.seed_R, self.seed_Q)
        fpen_ = FpenFunction(self.D, self.x_vector)
        fpen = fpen_.fpen_function()
        fx = 0
        zi = tosz_class.zi_function()
        for i in range(1,self.D-1):
            for k in range(11):
                fx = math.pow(1/2,k)*math.cos(math.pow(2*pi*3,k)* (zi[i]+1/2))-math.pow(1/2,k)*math.cos(math.pow(2*pi*3,k)*1/2)
        return fx

