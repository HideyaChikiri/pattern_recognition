# -*- coding: utf-8 -*-

# SHHリモートログイン時はこれを利用
import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

def matplotConfig():
    # xy軸(spine)の移動
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    ax.set_title('perceptron')
    ax.set_xlabel('w1')
    ax.set_ylabel('w0')
    ax.grid(True) #補助線
    
    # グラフとメモリの被りを半透明化
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

def g(X, W):
    v = 0
    for i in range(len(W)):
        v += W[i] * X[i]
    return v
    
if __name__ == '__main__':
    
    # 初期値
    # X : [x1, x2, class]
    X = [[1.0, 1.2, 1], [1.0, 0.2, 1], [1.0, -0.2, 1],
        [1.0, -0.5, 2], [1.0, -1.0, 2], [1.0, -1.5, 2]]
    W = [-16.0, -3.0] #W0, W1
    W_copy = list(W)
    row = 1.5
    canContinue = True
    
    plt.scatter(W[1], W[0], c = 'blue', marker = "o")
    
    while canContinue:
        canContinue = False
        for i in range(len(X)):
            
            g_value = g(X[i], W)
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
    
    matplotConfig()
    
    plt.savefig("graph.png") #CUIでshowは使えない

