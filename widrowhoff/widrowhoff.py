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
import math

# 識別関数の描画
def showG1minusG2function(color, label):
    x = np.linspace(-2.5, 2.5)
    y = (W[0][0] - W[1][0]) + x * (W[0][1] - W[1][1])
    if label:
        plt.plot(x, y, c=color, linewidth=3.0, linestyle="-" , label=label)
        plt.legend(loc="lower left")
    else:
        plt.plot(x, y, c=color, linewidth=1.0, linestyle="-")
    

# 特徴空間表示
def widrowhoff():
    
    classSize = len(B)
    epoch = 10
    filename = "linearlyseparable.png"
    
    plt.figure()
    plt.text(0, -20, "epoch=" + str(epoch), ha = 'center', va = 'bottom', size = 'xx-large')
    
    for i in range(len(X)):
        if X[i][2] == 1:
            plt.scatter(X[i][1], 0, c = 'black', s = 50, marker = "o")
        elif X[i][2] == 2:
            plt.scatter(X[i][1], 0, c = 'black', s= 50, marker = "x")
    
    showG1minusG2function("blue", "start")
    
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
                    e = g[w_c] - B[0][w_c]
                    W[w_c][0] -= rho * e * X[p][0]
                    W[w_c][1] -= rho * e * X[p][1] 
                    epsilon.append(e)
                        
                print("Xp:" + str(p) + " g:[" + str(g[0]) + "," + str(g[1]) 
                + "] B:[" + str(B[0][0]) + "," + str(B[0][1]) + "] e:["
                + str(epsilon[0]) + "," + str(epsilon[1]) + "]")
                
                # w_c : 各クラスの識別関数gに用いる重み
                for w_c in range(classSize):
                    total_epsilon +=math.fabs(epsilon[w_c])

            elif X[p][2] == 2:
                
                epsilon = []
                for w_c in range(classSize):
                    e = g[w_c] - B[1][w_c]
                    W[w_c][0] -= rho * e * X[p][0]
                    W[w_c][1] -= rho * e * X[p][1] 
                    epsilon.append(e)
                
                print("Xp:" + str(p) + " g:[" + str(g[0]) + "," + str(g[1]) 
                + "] B:[" + str(B[1][0]) + "," + str(B[1][1]) + "] e:["
                + str(epsilon[0]) + "," + str(epsilon[1]) + "]")
                
                for w_c in range(classSize):
                    total_epsilon +=math.fabs(epsilon[w_c])

                
        print("total_e:" + str(total_epsilon))
        showG1minusG2function("red", "")
        
    # 学習後識別関数の表示
    showG1minusG2function("green", "finish")
    
    matplotConfig.forFeature(filename)
    plt.savefig(filename) #CUIでshowは使えない
    
if __name__ == '__main__':
    
    # 初期値
    X = [[1.0, 1.2, 1], [1.0, 0.2, 1], [1.0, -0.2, 1],
        [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2]]
    # X = [[1.0, 1.2, 1], [1.0, 0.2, 1], [1.0, -0.2, 1],
    #     [1.0, 0.5, 2], [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2]]
        
    W = [[-7.0, 2.0], [6.0, 3.0]] #W0, W1
    rho = 0.1
    
    # 教師ベクトル
    B = [[1, 0], [0, 1]]
    
    widrowhoff()
    