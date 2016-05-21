# -*- coding: utf-8 -*-

import sys
sys.path.append("../mylibrary")

import numpy as np
import mathfunction
import math

def widrowhoff():
    
    classSize = len(B)
    epoch = 100
    
    for ep in range(epoch):
        print("---"+ str(ep+1) + "th---")
        
        total_epsilon = 0
        
        for p in range(len(X)):
            
            g_v = []
            e_v = []
            p_total_epsilon = 0
            for i in range(classSize):
                g = mathfunction.g(X[p], W[i])
                
                    
                e = g - B[X[p][2]-1][i]
                W[i][0] -= rho * X[p][0] * e
                W[i][1] -= rho * X[p][1] * e
                g_v.append(g)
                e_v.append(e)
            
            p_total_epsilon = math.fabs(e_v[i])
                    
            g_str = ""
            B_str = ""
            e_str = ""
            for i in range(classSize):
                g_str += str(g_v[i]) + ","
                B_str += str(B[X[p][2]-1][i]) + ","
                e_str += str(e_v[i]) + ","
            print("Xp:" + str(p) 
            + " g:[" + g_str 
            + "] B:[" + B_str 
            + "] e:[" + e_str + "]"
            + "=" + str(p_total_epsilon))
            
            
            for i in range(classSize):
                total_epsilon += p_total_epsilon

        print("total_e:" + str(total_epsilon))
        
if __name__ == '__main__':
    
    # 初期値
    X = [[1.0, 1.2, 1], [1.0, 0.2, 1], [1.0, -0.2, 1], [1.0, 3.0, 1],
        [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2],
        [1.0, -1.7, 3], [1.0, -2.0, 3], [1.0, -5.1, 3]]
    # X = [[1.0, 1.2, 1], [1.0, 0.2, 1], [1.0, -0.2, 1],
    #     [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2]]
        
    W = [[-7.0, 2.0], [6.0, 3.0], [1.0, 5.0]] #W0, W1
    # W = [[-7.0, 2.0], [6.0, 3.0]] #W0, W1
    rho = 0.01
    
    # 教師ベクトル
    B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    # B = [[1, 0], [0, 1]]
    
    widrowhoff()
    