import numpy as np
import math
from numpy import *
import random


def coco_rand_uniform(dim,seed):

        #random.seed(seed)
        uniftmp = np.random.uniform(low=0.5, high=(seed), size=(1,dim))

        return uniftmp

def coco_rand_gauss( dim, seed):

        g = np.ones((1,dim), dtype=np.float64)


        uniftmp_ = coco_rand_uniform(2*dim,seed)

        for i in range(dim):

            g[0][i] = sqrt(fabs(-2.0 * log(uniftmp_[0][i]))) * cos(2.0 * math.acos(-1) * uniftmp_[0][dim+i])
            if(g[0][i] == 0.):
                g[0][i] = 1e-99
        return g

def coco_reshape(vetor, m,n):

        B = np.ones((m,n),dtype=np.float64)

        for i in range(m):
            for j in range(n):
                B[i][j] = vetor[0][j*m+i]
        return B

def rotacao_gaussiana(dim, seed):

        gvect = coco_rand_gauss(dim*dim, seed)
        G = coco_reshape(gvect, dim, dim)

        for i in range(dim):
            for j in range(i):
                produto = 0
                for k in range(dim):
                    produto += G[k][i] * G[k][j]
                for k in range(dim):
                    G[k][i] -= produto * G[k][j]
            produto = 0
            for k in range(dim):
                produto += G[k][i] * G[k][i]
            for k in range(dim):
                G[k][i] /= sqrt(fabs(produto))

        return G


def diagonal_matrix(dim):

        lambda_= np.zeros((dim,dim), dtype=np.float64)
        for i in range(dim):
            lambda_[i][i] = pow(0.01,1/2 * ((i - 1)/(dim - 1)))

        return lambda_

def fzero_function():

        for k in range(11):
            fzero = pow(1/2,k)*(cos(pow(2*pi*3,k))*(1/2))
        return fzero


def gvector_generator(dim):
    x_vector = []

    for i in range(dim):
        x_vector.append(float(input('x:')))

    return x_vector

def fpen_function(dim,x_vector):

    #fpen = np.ones((self.dim), dtype=np.float64)
    fpen = 0
    for i in range(1,dim):

        fpen = pow(max(0,abs(x_vector[i])-5),2)

    return fpen

def x_column(R,x_vector):

    return R.dot(x_vector)

def sign_function(x_col):

    sign_ = np.sign(x_col)
    return sign_

def x_hat_function(x_col,dim):
    x_hat = np.ndarray(dim, dtype=np.float64)

    for i in range(dim):
        if (x_col[i] != 0):
            x_hat[i] = log((abs(x_col[i])))
        else:
            x_hat[i] = 0

    return x_hat

def c1_value_function(x_col,dim):

    c1 = np.ndarray(dim,dtype=np.float64)
    #c1 = np.ones(dim,dtype=np.float64)
    for i in range(dim):
        if(x_col[i] > 0):
            c1[i] = 10
        else:
            c1[i] = 5.5

    return c1

def c2_value_function(x_col,dim):
    c2_value = np.ndarray(dim, dtype=np.float64)

    for i in range(dim):
        if (x_col[i] > 0):
            c2_value[i] = 7.9
        else:
            c2_value[i] = 3.1

    return c2_value
def tosz_function(dim,c1_,c2_,signal,x_hat):

    tosz = np.ndarray(dim,dtype=np.float64)
    for i in range(dim):
        tosz[i] = signal[i] * exp(x_hat[i] + 0.049 * (sin(c1_[i] * x_hat[i]) + sin(c2_[i] * x_hat[i])))
    return tosz

def zi_function(tosz,Q,R,diagonal):

    productQ_tosz = Q.dot(tosz)
    productLambda_q = diagonal.dot(productQ_tosz)
    zi = R.dot(productLambda_q)
    return zi

def weierstrass_function(dim,zi,fpen):

    weier = 0
    for i in range(1,dim-1):
         for k in range(11):
            weier = weier + pow(1 / 2, k) * cos(pow(2 * pi * 3, k) * (zi[i] + 1 / 2)) - pow(1 / 2, k) * cos(
                 pow(2 * pi * 3, k) * 1 / 2)

    fx = 0
    fx = 10 * pow((1/dim) * weier,3) + ((10/dim)*fpen)
    return fx
