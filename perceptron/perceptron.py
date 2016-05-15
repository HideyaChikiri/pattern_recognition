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

# 識別関数の描画
def showGfunction(color):
    x = np.linspace(-2.5, 2.5)
    y = W[0] + x * W[1]
    plt.plot(x, y, c=color, linewidth=1.0, linestyle="-")
    
# 重み空間表示
def showWeightSpace(X, W, row):
    plt.figure()
    filename = "weight(" + str(W[1]) + "," + str(W[0]) + "," + str(row) + ").png"
    
    W_copy = list(W)
    canContinue = True
    
    plt.scatter(W[1], W[0], c = 'blue', marker = "o")
    
    while canContinue:
        canContinue = False
        for i in range(len(X)):
            
            g_value = mathfunction.g(X[i], W)
            print(str(X[i]) + ":" + str(W) + ":" + str(g_value))
            if g_value < 0 and X[i][2] == 1:
                print("1→2")
                W[0] = W[0] + row * X[i][0]
                W[1] = W[1] + row * X[i][1]
                canContinue = True
                plt.scatter(W[1], W[0], c = 'red', marker = "o")
                plt.plot([W_copy[1], W[1]], [W_copy[0], W[0]], color="red")
                W_copy = list(W)
            elif g_value > 0 and X[i][2] == 2:
                print("2→1")
                W[0] = W[0] - row * X[i][0]
                W[1] = W[1] - row * X[i][1]
                canContinue = True
                plt.scatter(W[1], W[0], c = 'red', marker = "o")
                plt.plot([W_copy[1], W[1]], [W_copy[0], W[0]], color="red")
                W_copy = list(W)
    
    # 解領域の表示
    w1 = x = np.linspace(-3, 13)
    for i in range(len(X)):
        if X[i][2] == 1:
            color = '#ffff00'
        elif X[i][2] == 2:
            color = '#00ff00'
        w0 = -X[i][1] * w1
        plt.plot(w1, w0, color, linewidth=1.0, linestyle="-")
    
    matplotConfig.forWeight(filename)
    plt.savefig(filename) #CUIでshowは使えない
    
# 特徴空間表示
def showFeatureSpace(X, W , row):
    plt.figure()
    filename = "feature(" + str(W[1]) + "," + str(W[0]) + "," + str(row) + ").png"
    
    canContinue = True
    
    showGfunction("blue")
    
    for i in range(len(X)):
        if X[i][2] == 1:
            plt.scatter(X[i][1], 0, c = 'green', s = 50, marker = "o")
        elif X[i][2] == 2:
            plt.scatter(X[i][1], 0, c = 'yellow', s= 50, marker = "s")
    
    while canContinue:
        canContinue = False
        for i in range(len(X)):
            
            g_value = mathfunction.g(X[i], W)
            print(str(X[i]) + ":" + str(W) + ":" + str(g_value))
            
            if g_value < 0 and X[i][2] == 1:
                print("1→2")
                W[0] = W[0] + row * X[i][0]
                W[1] = W[1] + row * X[i][1]
                showGfunction("red")
                canContinue = True
            elif g_value > 0 and X[i][2] == 2:
                print("2→1")
                W[0] = W[0] - row * X[i][0]
                W[1] = W[1] - row * X[i][1]
                showGfunction("red")
                canContinue = True
    
    # 学習後識別関数の表示
    showGfunction("black")
    
    matplotConfig.forFeature(filename)
    plt.savefig(filename) #CUIでshowは使えない

if __name__ == '__main__':
    
    # 初期値
    X = [[1.0, 1.2, 1], [1.0, 0.2, 1], [1.0, -0.2, 1],
        [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2]]
        
    W = [-7.0, 2.0] #W0, W1
    W_copy = list(W)
    row = 3.6
    showWeightSpace(X, W, row)
    W = list(W_copy)
    showFeatureSpace(X, W, row)
    
    W = [-7.0, 2.0] #W0, W1
    W_copy = list(W)
    row = 1.2
    showWeightSpace(X, W, row)
    W = list(W_copy)
    showFeatureSpace(X, W, row)
    
    W = [11.0, 5.0] #W0, W1
    W_copy = list(W)
    row = 2.0
    showWeightSpace(X, W, row)
    W = list(W_copy)
    showFeatureSpace(X, W, row)
