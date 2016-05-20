# -*- coding: utf-8 -*-

# SSHリモートログイン時はこれを利用
import matplotlib
matplotlib.use("Agg")

import sys
sys.path.append("../mylibrary")

import numpy as np
import matplotlib.pyplot as plt
import matplotConfig
import myfunction
import scipy.misc as scm

# 識別関数の描画
def showGfunction(color, classIndex):
    x = np.linspace(-1.75, 1.75)
    y = W[classIndex-1][0] + x * W[classIndex-1][1]
    plt.plot(x, y, c=color, linewidth=1.0, linestyle="-", label = "g(" + str(classIndex) + ")")
    plt.legend(loc="lower left")
    
# 交点とｘ軸の線分を表示(それぞれ2重に線を引いてるからあんまよくない)
def showToXaxisFromIntersection(color, classSize):
    for i in range(classSize):
        for j in range(classSize):
            if i != j:
                intersection_x = (W[i][0] - W[j][0]) / (W[j][1] - W[i][1])
                intersection_y = (W[j][1]*W[i][0] - W[i][1]*W[j][0]) / (W[j][1] - W[i][1])
                plt.plot([intersection_x, intersection_x],[0, intersection_y], color = color, linewidth = 1, linestyle = ':')
    
# 特徴空間表示
def showFeatureSpace(X, W , rho):
    plt.figure()
    filename = "feature(" + str(W) + "," + str(rho) + ")multi.png"
    
    print("======================================================================")
    classSize = len(W)
    canContinue = True
    
    for i in range(len(X)):
        if B[i] == 1:
            plt.scatter(X[i][1], 0, c = 'green', s = 50, marker = "o")
        elif B[i] == 2:
            plt.scatter(X[i][1], 0, c = 'yellow', s= 50, marker = "s")
        elif B[i] == 3:
            plt.scatter(X[i][1], 0, c = 'blue', s= 50, marker = "x")
    
    while canContinue:
        canContinue = False
        cntIncorrectClass = 0
        
        for i in range(len(X)):
            
            g = []
            for c in range(classSize):
                g.append(myfunction.g(X[i], W[c]))
            
            maxClass = np.nanargmax(g) + 1
            rightClass = B[i]
            
            print g
            if maxClass != rightClass:
                print str(rightClass) + "→" + str(maxClass)
                # 行列計算でコンパクトに
                W[rightClass-1] += rho * X[i]
                W[maxClass-1] -= rho * X[i]
                
                canContinue = True
                cntIncorrectClass += 1
                
        print("IncorrectClass:" + str(cntIncorrectClass))

    # 学習後識別関数の表示
    showGfunction("green",1)
    showGfunction("yellow",2)
    showGfunction("blue",3)
    
    showToXaxisFromIntersection("red", classSize)
    matplotConfig.forFeature(filename, 0)
    plt.savefig(filename) #CUIでshowは使えない

if __name__ == '__main__':
    
    # 初期値
    X = [np.array([1.0, 1.2]), np.array([1.0, 0.2]), np.array([1.0, -0.2]),np.array([1.0, 1.5]),
        np.array([1.0, -0.5]), np.array([1.0, -1.0]), np.array([1.0, -1.5]),
        np.array([1.0, -1.63]), np.array([1.0, -1.7])]
        
    # 教師
    B = [1, 1, 1, 1, 2, 2, 2, 3, 3]
        
    W = [np.array([-7.0, 2.0]),
        np.array([3.0, -2.0]),
        np.array([10.0, -9.1])]
    rho = 3.6
    showFeatureSpace(X, W, rho)
    
    W = [np.array([-7.0, 2.0]),
        np.array([3.0, -2.0]),
        np.array([1.0, 1.0])]
    rho = 1.2
    showFeatureSpace(X, W, rho)
    
    W = [np.array([11.0, 5.0]),
        np.array([2.1, 3.9]),
        np.array([-5.0, -5.0])]
    rho = 2.0
    showFeatureSpace(X, W, rho)
