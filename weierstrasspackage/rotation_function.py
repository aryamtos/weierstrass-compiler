import random

import numpy as np
import math
from numpy import *

class RotationFunction(object):

    def __init__(self):

        pass

    def coco_rand_uniform(self,dim,seed):

        #random.seed(seed)
        uniftmp: object = np.random.uniform(low=0.5, high=(seed), size=(1,dim))

        return uniftmp

    def coco_rand_gauss(self, dim, seed):
        g = np.ones((1,dim), dtype=np.float64)

        uniftmp = self.coco_rand_uniform(2*dim,seed)

        for i in range(dim):

            g[0][i] = math.sqrt(math.fabs(-2.0 * math.log(uniftmp[0][i]))) * math.cos(2.0 * math.acos(-1) * uniftmp[0][dim+i])
            if(g[0][i] == 0.):
                g[0][i] = 1e-99
        return g

    def coco_reshape(self,vetor, m,n):

        B = np.ones((m,n),dtype=np.float64)

        for i in range(m):
            for j in range(n):
                B[i][j] = vetor[0][j*m+i]
        return B

    def rotacao_gaussiana(self,dim, seed):

        gvect = self.coco_rand_gauss(dim*dim, seed)
        B = self.coco_reshape(gvect, dim, dim)

        for i in range(dim):
            for j in range(i):
                produto = 0
                for k in range(dim):
                    produto += B[k][i] * B[k][j]
                for k in range(dim):
                    B[k][i] -= produto * B[k][j]
            produto = 0
            for k in range(dim):
                produto += B[k][i] * B[k][i]
            for k in range(dim):
                B[k][i] /= math.sqrt(math.fabs(produto))

        return B
