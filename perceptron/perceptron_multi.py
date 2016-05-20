# -*- coding: utf-8 -*-

# SSHリモートログイン時はこれを利用
import matplotlib
matplotlib.use("Agg")

import sys
sys.path.append("../mylibrary")

import numpy as np
import matplotlib.pyplot as plt
import matplotConfig
import mathfunction
import scipy.misc as scm

# 識別関数の描画
def showGfunction(color, classIndex):
    x = np.linspace(-1.75, 1.75)
    y = W[classIndex-1][0] + x * W[classIndex-1][1]
    plt.plot(x, y, c=color, linewidth=1.0, linestyle="-", label = "g(" + str(classIndex) + ")")
    plt.legend(loc="lower left")
    
# 特徴空間表示
def showFeatureSpace(X, W , rho):
    plt.figure()
    filename = "feature(" + str(W) + "," + str(rho) + ")multi.png"
    
    print("==================")
    
    classSize = len(W)
    canContinue = True
    
    for i in range(len(X)):
        if X[i][2] == 1:
            plt.scatter(X[i][1], 0, c = 'green', s = 50, marker = "o")
        elif X[i][2] == 2:
            plt.scatter(X[i][1], 0, c = 'yellow', s= 50, marker = "s")
        elif X[i][2] == 3:
            plt.scatter(X[i][1], 0, c = 'orange', s= 50, marker = "x")
    
    while canContinue:
        canContinue = False
        cntIncorrectClass = 0
        
        for i in range(len(X)):
            
            g = []
            for c in range(classSize):
                g.append(mathfunction.g(X[i], W[c]))
            
            maxClass = np.nanargmax(g) + 1
            rightClass = X[i][2]
            
            print g
            if maxClass != rightClass:
                print str(rightClass) + "→" + str(maxClass)
                W[rightClass-1][0] += rho * X[i][0]
                W[rightClass-1][1] += rho * X[i][1]
                
                W[maxClass-1][0] -= rho * X[i][0]
                W[maxClass-1][1] -= rho * X[i][1]
                
                canContinue = True
                cntIncorrectClass += 1
                
        print("IncorrectClass:" + str(cntIncorrectClass))

    # 学習後識別関数の表示
    showGfunction("green",1)
    showGfunction("yellow",2)
    showGfunction("orange",3)
    
    print(scm.comb(classSize, 2))
    
    for i in range(classSize):
        for j in range(classSize):
            if i != j:
                intersection_x = (W[i][0] - W[j][0]) / (W[j][1] - W[i][1])
                intersection_y = (W[j][1]*W[i][0] - W[i][1]*W[j][0]) / (W[j][1] - W[i][1])
                plt.plot([intersection_x, intersection_x],[0, intersection_y], color = "blue", linewidth = 2, linestyle = '--')
    
    
    # intersection_x = (W[0][0] - W[1][0]) / (W[1][1] - W[0][1])
    # intersection_y = (W[1][1]*W[0][0] - W[0][1]*W[1][0]) / (W[1][1] - W[0][1])
    
    # plt.plot([intersection_x, intersection_x],[0, intersection_y], color = "blue", linewidth = 2, linestyle = '--')
    
    
    
    matplotConfig.forFeature(filename, 0)
    plt.savefig(filename) #CUIでshowは使えない

if __name__ == '__main__':
    
    # 初期値
    # X = [[1.0, 1.2, 1], [1.0, 0.2, 1], [1.0, -0.2, 1],
    #     [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2]]
    X = [[1.0, 1.2, 1], [1.0, 0.2, 1], [1.0, -0.2, 1],[1.0, 1.5, 1],
        [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2],
        [1.0, -1.63, 3], [1.0, -1.7, 3]]
        
    W = [[-7.0, 2.0],[3.0, -2.0],[10.0, -9.1]]
    rho = 3.6
    showFeatureSpace(X, W, rho)
    
    W = [[-7.0, 2.0],[3.0, -2.0],[1.0, 1,0]]
    row = 1.2
    showFeatureSpace(X, W, row)
    
    W = [[11.0, 5.0],[2.1, 3.9],[-5.0, -5.0]]
    row = 2.0
    showFeatureSpace(X, W, row)
