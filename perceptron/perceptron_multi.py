# -*- coding: utf-8 -*-

import sys
sys.path.append("../mylibrary")

import numpy as np
import mathfunction
    
# 重み空間表示
def perceptron(X, W, rho):
    canContinue = True
    
    
    # print(mathfunction.g(X[0], W[0]))
    
    max = -1000000
    max_index = -1
    for i in range(3):
        g = mathfunction.g(X[0], W[i])
        print(g)
        if g > max:
            max = g
            max_index = i
            
    if max_index+1 != X[0][2]:
        print(max_index+1)
        W[0][0] += rho * X[0][0]
        W[0][1] += rho * X[0][1]
        W[1][0] += rho * X[0][0]
        W[1][1] += rho * X[0][1]
        W[2][0] += rho * X[0][0]
        W[2][1] += rho * X[0][1]
        
            
    # while canContinue:
    #     canContinue = False
    #     for i in range(len(X)):
            
    #         g_value = mathfunction.g(X[i], W)
    #         print(str(X[i]) + ":" + str(W) + ":" + str(g_value))
    #         if g_value < 0 and X[i][2] == 1:
    #             print("1→2")
    #             W[0] = W[0] + rho * X[i][0]
    #             W[1] = W[1] + rho * X[i][1]
    #             canContinue = True
    #         elif g_value > 0 and X[i][2] == 2:
    #             print("2→1")
    #             W[0] = W[0] - rho * X[i][0]
    #             W[1] = W[1] - rho * X[i][1]
    #             canContinue = True
    
if __name__ == '__main__':
    
    # 初期値
    X = [[1.0, 1.2, 1], [1.0, 0.2, 1], [1.0, -0.2, 1],
        [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2],
        [1.0, -1.7, 3], [1.0 -2.0, 3]]
        
    W = [[-7.0, 2.0], [2.0, 3.0], [1.0, -2.0]]
    rho = 3.6
    perceptron(X, W, rho)
