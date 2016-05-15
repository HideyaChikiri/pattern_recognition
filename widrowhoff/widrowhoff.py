# -*- coding: utf-8 -*-

# SSHリモートログイン時はこれを利用
import matplotlib
matplotlib.use("Agg")

import sys
sys.path.append("../mylibrary")

import numpy as np
import mathfunction
import math

# 特徴空間表示
def widrhohoff(X, W , rho):
    
    for i in range(20):
        print("---"+ str(i+1) + "th---")
        
        total_epsilon = 0
        
        for p in range(len(X)):
            
            g1 = mathfunction.g(X[p], W[0])
            g2 = mathfunction.g(X[p], W[1])

            if X[p][2] == 1:
                
                epsilon1 = g1 - B[0][0]
                W[0][0] -= rho * X[p][0] * epsilon1
                W[0][1] -= rho * X[p][1] * epsilon1

                epsilon2 = g2 - B[0][1]
                W[1][0] -= rho * X[p][0] * epsilon2
                W[1][1] -= rho * X[p][1] * epsilon2
                
                print("Xp:" + str(p) + " g:[" + str(g1) + "," + str(g2) 
                + "] B:[" + str(B[0][0]) + "," + str(B[0][1]) + "] e:["
                + str(epsilon1) + "," + str(epsilon2) + "]")
                total_epsilon += math.fabs(epsilon1) + math.fabs(epsilon2)

            elif X[p][2] == 2:
                epsilon1 = g1 - B[1][0]
                W[0][0] -= rho * X[p][0] * epsilon1
                W[0][1] -= rho * X[p][1] * epsilon1

                epsilon2 = g2 - B[1][1]
                W[1][0] -= rho * X[p][0] * epsilon2
                W[1][1] -= rho * X[p][1] * epsilon2
                print("Xp:" + str(p) + " g:[" + str(g1) + "," + str(g2) 
                + "] B:[" + str(B[1][0]) + "," + str(B[1][1]) + "] e:["
                + str(epsilon1) + "," + str(epsilon2) + "]")
                total_epsilon += math.fabs(epsilon1) + math.fabs(epsilon2)


            # 0~2
            # if X[p][2] == 1:
            #     epsilon1 = g1 - B[0][0]
            #     epsilon2 = g2 - B[0][1]
            #     W[0][0] -= rho * X[p][0] * epsilon1
            #     W[0][1] -= rho * X[p][1] * epsilon2
                
            #     print("Xp:" + str(p) + " g:[" + str(g1) + "," + str(g2) 
            #     + "] B:[" + str(B[0][0]) + "," + str(B[0][1]) + "] e:["
            #     + str(epsilon1) + "," + str(epsilon2) + "]")
            #     total_epsilon += math.fabs(epsilon1) + math.fabs(epsilon2)
            # # 3~5
            # elif X[p][2] == 2:
            #     epsilon1 = g1 - B[1][0]
            #     epsilon2 = g2 - B[1][1]
            #     W[1][0] -= rho * X[p][0] * epsilon1
            #     W[1][1] -= rho * X[p][1] * epsilon2
            #     print("Xp:" + str(p) + " g:[" + str(g1) + "," + str(g2) 
            #     + "] B:[" + str(B[1][0]) + "," + str(B[1][1]) + "] e:["
            #     + str(epsilon1) + "," + str(epsilon2) + "]")
            #     total_epsilon += math.fabs(epsilon1) + math.fabs(epsilon2)
                
        print("total_e:" + str(total_epsilon))
    
if __name__ == '__main__':
    
    # 初期値
    X = [[1.0, 1.2, 1], [1.0, 0.2, 1], [1.0, -0.2, 1],
        [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2]]
        
    W = [[-7.0, 2.0], [6.0, 3.0]] #W0, W1
    rho = 0.2
    
    # 教師ベクトル
    B = [[1, 0], [0, 1]]
    
    widrhohoff(X, W, rho)
    