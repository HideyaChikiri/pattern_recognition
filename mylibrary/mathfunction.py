# -*- coding: utf-8 -*-

# 識別関数
def g(X, W):
    v = 0
    for i in range(len(W)):
        v += W[i] * X[i]
    return v
    