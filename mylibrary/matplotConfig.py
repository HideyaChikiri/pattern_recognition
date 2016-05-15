# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def forWeight(filename):
    # xy軸(spine)の移動
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    ax.set_title(filename)
    ax.set_xlabel('w1')
    ax.set_ylabel('w0')
    ax.grid(True) #補助線
    
    # グラフとメモリの被りを半透明化
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

def forFeature(filename):
    # xy軸(spine)の移動
    ax = plt.gca()  # gca stands for 'get current axis'
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',-2))
    # ax.spines['left'].set_color('none')
    
    ax.set_title(filename)
    ax.set_xlabel('X')
    ax.set_ylabel('g(X)')
    ax.grid(True) #補助線
    
    # グラフとメモリの被りを半透明化
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
        