from weierstrasspackage.rotation_function import RotationFunction
from weierstrasspackage.toz_function import ToszFunction
from weierstrasspackage.diagonal_matrix import DiagonalMatrix
from weierstrasspackage.fpen_function import FpenFunction
from weierstrasspackage.f0_function import FzeroFunction
from weierstrasspackage.weierstass import WeierstrassFunction
from numpy import *

def gvector_generator(dim):
    x_vector = []

    for i in range(dim):
        x_vector.append(float(input('x:')))

    return x_vector

if __name__ == '__main__':


    dim = int(input('Dimensão:'))
    seed_R = int(input('Seed matriz R:'))
    seed_Q = int(input('Seed matriz Q:'))

    rotation = RotationFunction()

    diagonal = DiagonalMatrix(dim)

    R = rotation.rotacao_gaussiana(dim, seed_R)
    Q = diagonal.alfa_generator()
    print('\n')
    print('<======Matriz de Rotação======>\n')
    print(R)
    print('\n')
    print('<======Matriz Diagonal======>\n')
    print(Q)
    print('\n')



    Q = rotation.rotacao_gaussiana(dim,seed_Q)

    x_vector = gvector_generator(dim)

    tosz_class = ToszFunction(R,Q,x_vector,dim,seed_R,seed_Q)
    fpen = FpenFunction(dim,x_vector)
    fp = fpen.fpen_function()
    zi = tosz_class.zi_function()
    tosz = tosz_class.tosz_function()
    c2 = tosz_class.c2_value_function()

    wei = WeierstrassFunction(R,Q,x_vector,dim,seed_R,seed_Q)
    weierstrass = wei.function_summation()
    print(c2)


