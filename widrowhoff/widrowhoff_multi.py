# -*- coding: utf-8 -*-

import sys
sys.path.append("../mylibrary")

import numpy as np
import mathfunction
import math

# 特徴空間表示
def widrowhoff():
    
    classSize = len(B)
    epoch = 100
    
    for i in range(epoch):
        print("---"+ str(i+1) + "th---")
        
        total_epsilon = 0
        
        for p in range(len(X)):
            
            g = []
            for c in range(classSize):
                g.append(mathfunction.g(X[p], W[c]))
            
            if X[p][2] == 1:
                
                epsilon = []
                for w_c in range(classSize):
                    epsilon.append(g[w_c] - B[0][w_c])
                    W[w_c][0] -= rho * X[p][0] * epsilon[w_c]
                    W[w_c][1] -= rho * X[p][1] * epsilon[w_c]
                    
                
                g_str = ""
                B_str = ""
                e_str = ""
                for c in range(classSize):
                    g_str += str(g[c]) + ","
                    B_str += str(B[0][c]) + ","
                    e_str += str(epsilon[c]) + ","
                print("Xp:" + str(p) 
                + " g:[" + g_str 
                + "] B:[" + B_str 
                + "] e:[" + e_str + "]")
                
                
                for w_c in range(classSize):
                    total_epsilon +=math.fabs(epsilon[w_c])

            elif X[p][2] == 2:
                
                epsilon = []
                for w_c in range(classSize):
                    epsilon.append(g[w_c] - B[1][w_c])
                    W[w_c][0] -= rho * X[p][0] * epsilon[w_c]
                    W[w_c][1] -= rho * X[p][1] * epsilon[w_c]
                
                # print("Xp:" + str(p) + " g:[" + str(g[0]) + "," + str(g[1]) 
                # + "] B:[" + str(B[1][0]) + "," + str(B[1][1]) + "] e:["
                # + str(epsilon[0]) + "," + str(epsilon[1]) + "]")
                
                
                g_str = ""
                B_str = ""
                e_str = ""
                for c in range(classSize):
                    g_str += str(g[c]) + ","
                    B_str += str(B[1][c]) + ","
                    e_str += str(epsilon[c]) + ","
                print("Xp:" + str(p) 
                + " g:[" + g_str 
                + "] B:[" + B_str 
                + "] e:[" + e_str + "]")
                
                
                for w_c in range(classSize):
                    total_epsilon +=math.fabs(epsilon[w_c])
                
            elif X[p][2] == 3:
                
                epsilon = []
                for w_c in range(classSize):
                    epsilon.append(g[w_c] - B[2][w_c])
                    W[w_c][0] -= rho * X[p][0] * epsilon[w_c]
                    W[w_c][1] -= rho * X[p][1] * epsilon[w_c]
                
                # print("Xp:" + str(p) + " g:[" + str(g[0]) + "," + str(g[1]) 
                # + "] B:[" + str(B[2][0]) + "," + str(B[2][1]) + "] e:["
                # + str(epsilon[0]) + "," + str(epsilon[1]) + "]")
                
                
                g_str = ""
                B_str = ""
                e_str = ""
                for c in range(classSize):
                    g_str += str(g[c]) + ","
                    B_str += str(B[2][c]) + ","
                    e_str += str(epsilon[c]) + ","
                print("Xp:" + str(p) 
                + " g:[" + g_str 
                + "] B:[" + B_str 
                + "] e:[" + e_str + "]")
                
                
                
                for w_c in range(classSize):
                    total_epsilon +=math.fabs(epsilon[w_c])
                
        print("total_e:" + str(total_epsilon))
        
if __name__ == '__main__':
    
    # 初期値
    X = [[1.0, 1.2, 1], [1.0, 0.2, 1], [1.0, -0.2, 1],
        [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2],
        [1.0, -1.7, 3], [1.0, -2.0, 3]]
    #     [1.0, 0.5, 2], [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2]]
        
    W = [[-7.0, 2.0], [6.0, 3.0], [1.0, -2.0]] #W0, W1
    rho = 0.1
    
    # 教師ベクトル
    B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    
    widrowhoff()
    