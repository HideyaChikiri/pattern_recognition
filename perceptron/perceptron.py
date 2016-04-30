# -*- coding: utf-8 -*-

# SHHリモートログイン時はこれを利用
import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

def g(X, W):
    return W[0] + X * W[1]
    
if __name__ == '__main__':
    
    X = [[1.2, 1], [0.2, 1], [-0.2, 1],
        [-0.5, 2], [-1.0, 2], [-1.5, 2]]
    W = [-5.0, 5.0] #W0, W1
    row = 0.3
    
    for i in range(len(X)):
        g_value = g(X[i][0], W)
        print(str(X[i]) + ":" + str(W) + ":" + str(g_value))
        if g_value < 0 and X[i][1] == 1:
            print("1→2")
            
        elif g_value > 0 and X[i][1] == 2:
            print("2→1")
        
        
        
        
    
    x = np.linspace(-5, 15)
    A = x
    plt.plot(x, A, color="green", linewidth=1.0, linestyle="-", label="x")
    plt.legend(loc='upper left')
    
    
    
    plt.scatter(W[1], W[0], c = 'red', marker = "o")
    
    
    
    # メモリの設定
    plt.xticks([-5, 0, +5, +10, +15])
    plt.yticks([-5, 0, +5, +10, +15])
    
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
    
    # グラフとメモリの被りを半透明化
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
    
    plt.savefig("graph.png") #CUIでshowは使えない

